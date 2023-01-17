import json


info = json.loads(
    '''{
        "preto": "0321",
        "vermelho": "2",
        "PV": "553221",
        "branco": "233"
    }'''
)

# jsonobj = json.dumps(info, separators=(',',':'))


# with open("cfg.json", "r") as json_file:
#     data = json.load(json_file)

# with open("cfg.json", "a") as json_file:
#     json.dump(info, json_file,separators=(',',':'))


# with open("cfg.json", encoding='utf-8') as estrategias:
#         dados = json.load(estrategias)
#         print(len(dados)) 

# print(dados)

# for i in dados:
#     print(i['PV']) 

import requests
# Defina a URL da API e os parâmetros de consulta (se houver)
url = "https://blaze.com/api/roulette_games/history"
params = {"param1": "value1", "param2": "value2"}

# Faça uma solicitação GET à API e obtenha a resposta
response = requests.get(url)
# response = requests.get(url, params=params)

# Verifique se a resposta foi bem-sucedida
if response.status_code == 200:
    # Exiba o conteúdo da resposta
    data = response.json()
    print(data['records'][0]['color'])

    for i, sinais in data:
        pass
else:
    # Exiba o código de status da resposta e a mensagem de erro (se houver)
    print("Erro ao consumir API:", response.status_code, response.reason)
