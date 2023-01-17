import requests
import json

try:
    with open("cfg.json", "r") as json_file:
        data = json.load(json_file)
except:
    data = {}
    data["estrategias"] = []

info = json.loads(
    '''{
            "nome": "teste",
            "total": 5,
            "1": "PV-5",
            "2": "red-2",
            "3": "black-1",
            "4": "",
            "5": ""
        }'''
)

sequence = []
aux = []
for z, estrategia in enumerate(data["estrategias"]):
    aux = []
    for i in range(5):
        valores= data["estrategias"][z][f'{i+1}'].split('-')
        # valores= info[f'{i+1}'].split('-')
        
        try:
            print('VALORES 1')
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


def sequence_in_list(sequence, lst):
    for i in range(len(lst)-len(sequence)+1):
        if lst[i:i+len(sequence)] == sequence:
            return True
    return False


# Verifique se a resposta foi bem-sucedida
if response.status_code == 200:
    # Armazene o conteúdo da resposta
    data = response.json()
    for i in range(int(len(sequence))):
        records = data['records'][:len(sequence[i])]
        print(records)
        print('------------------')

        data_in =[]
        result = records[::-1]
        
        aux=[]

        for j in range(int(len(result))):
            aux.append(result[j]['color'])
            # print(aux)

        # print(result)
        # print('------------------')
        estrategia = set(sequence[i])
        aux= set(aux)
        print(aux)
        print(estrategia)

        # comparando as listas
        if aux == estrategia:
            print("As listas são iguais")
        else:
            print("As listas são diferentes")
        
        # # Verifique a cor dos 60 primeiros registros
        # for j in range(int(valores[1])):
        #     result = records[::-1][j]
        #     data_in.append(result['color'])
        #     print(result)

        #     if int(valores[1])>=j:
        #         print(f"Cor {j+1}: {result['color']} \nValor: {result['roll']}\n------------")

                # print(info[f'{i+1}'])
                
                
else:
    # Exiba o código de status da resposta e a mensagem de erro (se houver)
    print("Erro ao consumir API:", response.status_code, response.reason)

data_invertido= set(data_in)

# for i in  range(int(len(sequence))):
#     estrategia = set(sequence[i])

#     # comparando as listas
#     if data_invertido == estrategia:
#         print("As listas são iguais")
#     else:
#         print("As listas são diferentes")