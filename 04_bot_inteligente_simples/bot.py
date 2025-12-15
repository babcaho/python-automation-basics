def classificar_texto(texto):
    positivas = ["bom", "ótimo", "excelente", "feliz"]
    negativas = ["ruim", "péssimo", "triste", "horrível"]

    texto = texto.lower()
    pontuacao = 0

    for palavra in positivas:
        if palavra in texto:
            pontuacao += 1

    for palavra in negativas:
        if palavra in texto:
            pontuacao -= 1

    if pontuacao > 0:
        return "Positivo"
    elif pontuacao < 0:
        return "Negativo"
    else:
        return "Neutro"

def main():
    frase = input("Digite uma frase: ")
    resultado = classificar_texto(frase)
    print("Classificação:", resultado)

if __name__ == "__main__":
    main()
