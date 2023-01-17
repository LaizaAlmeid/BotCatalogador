import requests
import json

try:
    with open("cfg.json", "r") as json_file:
        data = json.load(json_file)
except:
    data = {}
    data["estrategias"] = []

sequence = []
aux = []
for z, estrategia in enumerate(data["estrategias"]):
    aux = []
    for i in range(5):
        valores= data["estrategias"][z][f'{i+1}'].split('-')
        # valores= info[f'{i+1}'].split('-')
        
        try:
            print('VALORES:')
            print(valores[1])
            for j in range(int(valores[1])):
                aux.append(valores[0])
                # print(aux)
        except:
            print('SEM REGISTRO')
    sequence.append(aux)
    print(sequence)
    print(f'Total: {data["estrategias"][z]["total"]}')
    print('-----------------------------------------------')



# Defina a URL da API e os parâmetros de consulta (se houver)
url = "https://blaze.com/api/roulette_games/history"


# Faça uma solicitação GET à API e obtenha a resposta
response = requests.get(url)


# Verifique se a resposta foi bem-sucedida
if response.status_code == 200:
    # Armazene o conteúdo da resposta
    data = response.json()

    # Otimizado via chatgpt
    for i in range(int(len(sequence))):
        redata = response.json()
        records = data['records'][:len(sequence[i])]
        records_reversed = records[::-1]
        colors = [record['color'] for record in records_reversed]
        strategy_set = set(sequence[i])
        colors_set = set(colors)

        if colors_set == strategy_set:
            print("As listas são iguais")
        else:
            print("As listas são diferentes")
                    
                
else:
    # Exiba o código de status da resposta e a mensagem de erro (se houver)
    print("Erro ao consumir API:", response.status_code, response.reason)

