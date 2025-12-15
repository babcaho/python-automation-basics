def ler_dados():
    valores = []

    with open("vendas.csv", "r") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            if linha.isdigit():
                valores.append(int(linha))

    return valores

def analisar(valores):
    total = sum(valores)
    media = total / len(valores)
    maior = max(valores)
    menor = min(valores)

    return total, media, maior, menor

def main():
    valores = ler_dados()
    total, media, maior, menor = analisar(valores)

    print("Resumo das Vendas")
    print("-----------------")
    print(f"Total: {total}")
    print(f"Média: {media}")
    print(f"Maior venda: {maior}")
    print(f"Menor venda: {menor}")

if __name__ == "__main__":
    main()
