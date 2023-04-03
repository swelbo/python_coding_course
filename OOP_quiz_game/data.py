import requests

api = "https://opentdb.com/api.php?amount=50&type=boolean"

r = requests.get(api)

question_data = r.json()["results"]

print(question_data)