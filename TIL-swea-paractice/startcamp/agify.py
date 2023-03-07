import requests

url = 'https://api.agify.io/?name=jun'

response = requests.get(url) 
print(response.json()['name'])