import os
from datetime import datetime

def analisar_arquivos():
    arquivos = os.listdir()
    extensoes = {}

    for arquivo in arquivos:
        if "." in arquivo:
            ext = arquivo.split(".")[-1]
            extensoes[ext] = extensoes.get(ext, 0) + 1

    return extensoes

def gerar_relatorio(resultado):
    data = datetime.now().strftime("%d/%m/%Y %H:%M")

    with open("relatorio.txt", "w") as relatorio:
        relatorio.write(f"Relatório de Arquivos\n")
        relatorio.write(f"Gerado em: {data}\n\n")

        for ext, qtd in resultado.items():
            relatorio.write(f".{ext}: {qtd} arquivo(s)\n")

    print("Relatório criado com sucesso.")

def main():
    print("Analisando arquivos da pasta...")
    resultado = analisar_arquivos()
    gerar_relatorio(resultado)

if __name__ == "__main__":
    main()


