import json
import os

with open(f"{os.path.realpath(os.path.dirname(__file__))}\quizz\openquizzdb_83.json", "r", encoding="utf-8") as file:
    data = json.load(file)

redacteur = data["fournisseur"]
theme = data["categorie-nom-slogan"]["fr"]["slogan"]
