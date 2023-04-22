// Yes, the code is ugly.

const puppeteer = require('puppeteer');
const ora = require('ora');
const prompt = require('prompt-sync')();
const Downloader = require('nodejs-file-downloader');

const url = "https://www.openquizzdb.org/listing.php";

async function wait(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

(async () => {
    const loading = ora('Loading page...').start();
    const browser = await puppeteer.launch({
        headless: true,
        args: ['--no-sandbox', '--disable-setuid-sandbox']
    });
    loading.text = 'Opening page...';
    const page = await browser.newPage();
    await page.goto(url);
    loading.text = 'Waiting for page to load...';
    await page.waitForSelector('footer#footer');
    loading.text = 'Preparing...';
    const allTitles = await page.evaluate(() => {
        return [...document.querySelectorAll(".mydown")].map((e) => {return [e.textContent, e.parentElement.onclick ? e.parentElement.onclick.toString()+";onclick();" : ""]});
    });
    loading.succeed('Ready!');
    console.log("Solving some quizzes...");
    for (let i = 0; i < allTitles.length; i++) {
        const title = allTitles[i][0];
        if (!title.includes("Quizz à débloquer")) {
            console.log(`❌ Will not solve ${title} because it is not a quiz to unlock.`);
            continue;
        }
        const code = allTitles[i][1];
        loading.start('Loading quiz...');
        await page.evaluate(code);
        loading.text = 'Waiting for page to load...';
        await page.waitForSelector('footer#footer');
        loading.text = 'Launching quiz...';
        await page.evaluate(() => {
            document.querySelector(".rounded-buttons").children[0].click();
        });
        loading.text = 'Waiting for page to load...';
        // wait 5 seconds for the quiz to load
        await wait(3000);
        loading.text = "Things are happening in the background, wait a little bit!";
        for (let i = 0; i < 3; i++) {
            const correctAnswerNo = await page.evaluate(() => {
                const el = document.querySelector("#rep1");
                console.log(el);
                const child = el.children[0];
                return child.onclick.toString().split("AfficherReponse(")[1].split(")")[0].split("','")[2]
            });
            const elemName = "rep"+correctAnswerNo;
            await page.evaluate((elemName) => {
                // console.log(elemName);
                const el = document.querySelector(`#${elemName}`);
                // console.log(el);
                el.children[0].click();
            }, elemName);
            await wait(4000);
            await page.evaluate(() => {
                const el = document.querySelector("#go_cha");
                el.click();
            });
            await wait(4000);
        }
        loading.text = "Done!";
        loading.succeed();
        await wait(2000);
        const href = await page.evaluate(() => {
            let link;
            document.querySelectorAll(".my_tbutton").forEach((btn) => {
                if (btn.children[0] && btn.children[0].href && btn.children[0].href.includes(".json")) {
                    link = btn.children[0].href;
                    return;
                }
            })
            return link;
        });
        const downloader = new Downloader({
            url: href,
            directory: "./",
        });
        const loader = ora('Downloading quiz...').start();
        try {
            const {filePath, downloadStatus} = await downloader.download();

            loader.succeed('Quiz downloaded!');
            console.log("Quiz downloaded to "+filePath);
            console.log(`Going back to ${url}...`);
            await page.goto(url);
            await page.waitForSelector('footer#footer');
        } catch (error) {
            loader.fail('Quiz download failed!');
        }
    }
    await browser.close();
    console.log('All done! Restart to download new quiz.');
})();
