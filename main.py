import requests

# URL da API que deseja consultar
URL_base = 'https://api.astroworldmc.com' + '/api/v1/'

endpoints = ['mobs','biomes','structures' ] 
for endpoint in endpoints:
    url = URL_base + endpoint
    resposta = requests.get(url)
    resposta.raise_for_status()
    nome =f'dados/{endpoint}.json'
    with open(nome, "w", encoding="utf-8") as arquivo:
        arquivo.write(resposta.text)
        print('escrevendo',endpoint,'em',nome)


