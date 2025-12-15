import os

def analisar_arquivos():
    arquivos = os.listdir()
    extensoes = {}

    for arquivo in arquivos:
        if "." in arquivo:
            ext = arquivo.split(".")[-1]
            extensoes[ext] = extensoes.get(ext, 0) + 1

    return extensoes

