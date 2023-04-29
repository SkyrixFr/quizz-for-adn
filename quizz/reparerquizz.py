import os
index = {"\xa0" : " "} 

for i in range(0, 300):
    try:
        fichier=open(f"quizz\openquizzdb_{i}.json", "r", encoding="utf-8")
        dest = open(f"quizz\\repared_openquizzdb_{i}.json", "w", encoding="utf-8")
        contenu=fichier.read() #Lit tout le fichier d'un coup

        for cle in index:    
            contenu=contenu.replace(cle, index[cle])
        dest.write(contenu)
        fichier.close()
        dest.close()
        os.remove(f"quizz\\openquizzdb_{i}.json")
        os.rename(f"quizz\\repared_openquizzdb_{i}.json", f"quizz\\openquizzdb_{i}.json")
    except:
        print("file does not exist")