import json

# carregando dados json a partir de um arquivo
with open("data.json", "r") as file:
    data = json.load(file)

# inverter os resultados
data = data[::-1]

# escrever os dados invertidos em um novo arquivo
with open("data_inverted.json", "w") as file:
    json.dump(data, file)