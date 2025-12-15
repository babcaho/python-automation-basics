import os

arquivos = os.listdir()
extensoes = {}

for arquivo in arquivos:
    if "." in arquivo:
        ext = arquivo.split(".")[-1]
        extensoes[ext] = extensoes.get(ext, 0) + 1

with open("relatorio.txt", "w") as relatorio:
    relatorio.write("Relatório de Arquivos\n\n")
    for ext, qtd in extensoes.items():
        relatorio.write(f".{ext}: {qtd} arquivo(s)\n")

print("Relatório criado com sucesso.")
