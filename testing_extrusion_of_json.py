import json
import random

with open("quizz\openquizzdb_83.json", "r", encoding="utf-8") as file:
    data = json.load(file)

print(data)