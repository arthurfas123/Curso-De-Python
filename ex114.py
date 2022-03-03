import requests

url = 'http://www.pudim.com.br'
try:
    site = requests.get(url=url)
    print('\033[36mO site Pudim esta acessivel!')
except:
    print('\033[31mO site pudim não esta disponivel!')
