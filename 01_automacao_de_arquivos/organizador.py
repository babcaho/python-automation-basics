import os

def analisar_arquivos():
    arquivos = os.listdir()
    extensoes = {}

    for arquivo in arquivos:
        if "." in arquivo:
            ext = arquivo.split(".")[-1]
            extensoes[ext] = extensoes.get(ext, 0) + 1

    return extensoes
resultado = analisar_arquivos()

print("Resumo dos arquivos:")
for ext, qtd in resultado.items():
    print(f".{ext}: {qtd} arquivo(s)")

