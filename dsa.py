import json

# Abrir o arquivo JSON existente
try:
    with open("cfg.json", "r") as json_file:
        data = json.load(json_file)
except:
    data = {}
    data["estrategias"] = []

while True:
    p = input("1- ADICIONAR \n2- REMOVER \n3- Visualizar \n4- EDITAR \n")

#-------------------------------
    if p=='1':

        nome = input("Nome da estratégia (ou 'q' para sair): ")
        if nome == 'q':
            break

        pv = int(input("Repetições de preto e vermelho: "))
        vermelho = int(input("Vermelho: "))
        preto = int(input("Preto: "))

        estrategia = {"nome":nome ,"PV": pv, "preto": preto, "vermelho": vermelho }
        data["estrategias"].append(estrategia)

        with open("cfg.json", "w") as json_file:
            json.dump(data, json_file, indent=4)
        print(f"{nome} adicionada com sucesso!")

#-------------------------------
    if p=='2':
        nome = input("Nome da estratégia que deseja remover (ou 'q' para sair): ")
        if nome == 'q':
            break

        for i, estrategia in enumerate(data["estrategias"]):
            if estrategia["nome"] == nome:

                del data["estrategias"][i]
                with open("cfg.json", "w") as json_file:
                    json.dump(data, json_file, indent=4)
                print(f"{nome} removida com sucesso!")
                break
        else:
            print(f"{nome} não encontrada.")

#-------------------------------
    if p=='3':
        for i in data["estrategias"]:
            print(i)

    if p=='4':
        nome = input("Novo campo ")
        if nome == 'q':
            break
        serach_estrategia = input("Nome da estratégia que deseja editar: ")
        conteudo= input("Digite o conteudo do campo: ")

        # Procurando pela pessoa desejada
        for estrategia in data["estrategias"]:
            if estrategia["nome"] == serach_estrategia:
                # Adicionando o novo campo
                estrategia[nome] = conteudo

        # Escrevendo as alterações de volta para o arquivo JSON
        with open("cfg.json", "w") as json_file:
            json.dump(data, json_file, indent=4)