import requests

req = requests.get("https://swapi.dev/api/people/1/")

person = req.json()


print(person['name'])
