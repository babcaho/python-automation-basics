valores = []

with open("vendas.csv", "r") as arquivo:
    for linha in arquivo:
        if linha.strip().isdigit():
            valores.append(int(linha))

total = sum(valores)
media = total / len(valores)
maior = max(valores)
menor = min(valores)

print("Total:", total)
print("Média:", media)
print("Maior valor:", maior)
print("Menor valor:", menor)
