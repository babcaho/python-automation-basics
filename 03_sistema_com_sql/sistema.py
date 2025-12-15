import sqlite3

def criar_tabela(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT
        )
    """)

def inserir_usuario(cursor, nome):
    cursor.execute("INSERT INTO usuarios (nome) VALUES (?)", (nome,))

def listar_usuarios(cursor):
    cursor.execute("SELECT * FROM usuarios")
    return cursor.fetchall()

def main():
    conexao = sqlite3.connect("usuarios.db")
    cursor = conexao.cursor()

    criar_tabela(cursor)

    inserir_usuario(cursor, "Maria")
    inserir_usuario(cursor, "João")
    inserir_usuario(cursor, "Ana")

    conexao.commit()

    usuarios = listar_usuarios(cursor)
    print("Usuários cadastrados:")
    for u in usuarios:
        print(u)

    conexao.close()

if __name__ == "__main__":
    main()
