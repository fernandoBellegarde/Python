url = "https://viacep.com.br/ws/04729030/json/"
import requests


r = requests.get(url)
print (r.json()['regiao'])
print (r.json())