import os

arquivos = os.listdir()
extensoes = {}

for arquivo in arquivos:
    if "." in arquivo:
        ext = arquivo.split(".")[-1]
        extensoes[ext] = extensoes.get(ext, 0) + 1

print("Resumo dos arquivos:")
for ext, qtd in extensoes.items():
    print(f".{ext}: {qtd} arquivo(s)")
