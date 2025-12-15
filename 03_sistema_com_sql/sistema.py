import sqlite3

conexao = sqlite3.connect("dados.db")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY,
    nome TEXT
)
""")

cursor.execute("INSERT INTO usuarios (nome) VALUES ('Maria')")
cursor.execute("INSERT INTO usuarios (nome) VALUES ('João')")

conexao.commit()

cursor.execute("SELECT * FROM usuarios")
usuarios = cursor.fetchall()

for u in usuarios:
    print(u)

conexao.close()
