import json
from os import path


def get_questions():
    # Define the range of file numbers
    start_number = 1
    end_number = 280  # Update this to the last file number in your sequence

    questions = []
    reponses=[]

    total = 0
    # Iterate over the range of file numbers using a for loop
    for file_number in range(start_number, end_number + 1):
        # Generate the file name using the file number
        file_name = f"{path.realpath(path.dirname(__file__))}\quizz\openquizzdb_{file_number}.json"
        try:
            with open(file_name, 'rb') as file:
                # Load the JSON data from the file
                json_data = json.load(file)
                # Do something with the JSON data
                # For example, you can access the data using dictionary-like syntax
                try:
                    for i in range(0, 8000):
                        #print(str(json_data["quizz"]["fr"]["débutant"][i]["question"]))
                        questions.append(str(json_data["quizz"]["fr"]["debutant"][i]["question"]))
                        reponses.append(json_data["quizz"]["fr"]["debutant"][i]["propositions"])
                        total+=1

                except IndexError:
                    total-=1
                    pass


        except FileNotFoundError:
            pass
    return (questions,reponses)
"""
                try:
                    for i in range(0, 8000):
                        #print(str(json_data["quizz"]["fr"]["débutant"][i]["question"]))
                        questions.append(str(json_data["quizz"]["fr"]["confirmé"][i]["question"]))
                        total+=1

                except IndexError:
                    total-=1
                    pass

                try:
                    for i in range(0, 8000):
                        #print(str(json_data["quizz"]["fr"]["débutant"][i]["question"]))
                        questions.append(str(json_data["quizz"]["fr"]["expert"][i]["question"]))
                        total+=1

                except IndexError:
                    total-=1
                    pass
"""