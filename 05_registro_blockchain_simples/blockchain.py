import hashlib
import time

class Bloco:
    def __init__(self, indice, dados, hash_anterior):
        self.indice = indice
        self.timestamp = time.time()
        self.dados = dados
        self.hash_anterior = hash_anterior
        self.hash = self.calcular_hash()

    def calcular_hash(self):
        conteudo = f"{self.indice}{self.timestamp}{self.dados}{self.hash_anterior}"
        return hashlib.sha256(conteudo.encode()).hexdigest()

def criar_blockchain():
    blockchain = []

    bloco_genesis = Bloco(0, "Bloco Inicial", "0")
    blockchain.append(bloco_genesis)

    for i in range(1, 4):
        novo_bloco = Bloco(i, f"Transação {i}", blockchain[-1].hash)
        blockchain.append(novo_bloco)

    return blockchain

def main():
    blockchain = criar_blockchain()

    for bloco in blockchain:
        print("Índice:", bloco.indice)
        print("Dados:", bloco.dados)
        print("Hash:", bloco.hash)
        print("Hash anterior:", bloco.hash_anterior)
        print("-" * 30)

if __name__ == "__main__":
    main()

