import sqlite3

def conectar_bd():
    conexao = sqlite3.connect('senhas.db')
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS senhas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            senha TEXT NOT NULL
        )
    """)
    conexao.commit()
    return conexao

def salvar_senha(senha):
    conexao = conectar_bd()
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO senhas (senha) VALUES (?)", (senha,))
    conexao.commit()
    conexao.close()
    print("Senha salva com sucesso!")

def excluir_senha_id(id_senha):
    conexao = conectar_bd()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM senhas WHERE id = ?", (id_senha,))
    conexao.commit()
    conexao.close()
    print(f"Senha com ID {id_senha} excluída com sucesso!")
