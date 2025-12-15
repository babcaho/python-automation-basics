positivas = ["bom", "ótimo", "excelente", "feliz"]
negativas = ["ruim", "péssimo", "triste", "horrível"]

texto = input("Digite uma frase: ").lower()

if any(p in texto for p in positivas):
    print("Classificação: Positiva")
elif any(n in texto for n in negativas):
    print("Classificação: Negativa")
else:
    print("Classificação: Neutra")
