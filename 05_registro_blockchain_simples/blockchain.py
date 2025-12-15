import hashlib
import time

class Bloco:
    def __init__(self, indice, dados, hash_anterior):
        self.indice = indice
        self.timestamp = time.time()
        self.dados = dados
        self.hash_anterior = hash_anterior
        self.hash = self.gerar_hash()

    def gerar_hash(self):
        conteudo = f"{self.indice}{self.timestamp}{self.dados}{self.hash_anterior}"
        return hashlib.sha256(conteudo.encode()).hexdigest()

blockchain = []

bloco_genesis = Bloco(0, "Bloco Inicial", "0")
blockchain.append(bloco_genesis)

bloco_1 = Bloco(1, "Transação A", bloco_genesis.hash)
blockchain.append(bloco_1)

for bloco in blockchain:
    print(bloco.indice, bloco.dados, bloco.hash)
