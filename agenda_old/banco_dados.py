import sqlite3
from contato import Contato

def cria_db():
    conn = sqlite3.connect('agenda.db')

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE contatos(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            telefone TEXT
        )
    """)

    print('Banco de dados e tabelas criadas com sucesso!')

    conn.close()

def insert_contato(contato):
    conn = sqlite3.connect('agenda.db')

    cursor = conn.cursor()

    lista = [(contato.nome, contato.email, contato.telefone)]

    if contato.id_contato:
        cursor.execute("""
            UPTADE contatos
            SET 
            nome = ?,
            telefone = ?
            WHERE id = ?""", (contato.nome, contato.telefone, contato.id_contato))
    else:
        cursor.executemany("""
            INSERT INTO contatos(nome, email, telefone) 
            VALUES(?, ?, ?)""", lista)

    conn.commit()

    print('Dados salvos com sucesso!')

    conn.close()

def select_contato():
    conn = sqlite3.connect('agenda.db')

    cursor = conn.cursor()

    contatos = []

    cursor.execute("""
        SELECT id, nome, email, telefone FROM contatos
    """)

    for linha in cursor.fetchall():
        contatos.append(Contato(id_contato = linha[0], nome = linha[1],
        email = linha[2], telefone = linha[3]))

    conn.close()

    return linha


def busca_nome(nome):
    conn = sqlite3.connect('agenda.db')

    cursor = conn.cursor()

    contatos = []

    cursor.execute("""
        SELECT id, nome, email, telefone FROM contatos WHERE nome = ?
    """, [nome])

    for linha in cursor.fetchall():
        contatos.append(Contato(id_contato = linha[0], nome = linha[1],
        email = linha[2], telefone = linha[3]))

    conn.close()

    return contatos

def busca_email(email):
    conn = sqlite3.connect('agenda.db')

    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, nome, email, telefone FROM contatos WHERE email = ?""", [email])

    contato = None

    for linha in cursor.fetchall():
        contato = Contato(id_contato = linha[0], nome = linha[1],
        email = linha[2], telefone = linha[3])

    conn.close()

    return contato

def delete_contato(contato):
    conn = sqlite3.connect('agenda.db')

    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM contatos WHERE id = ?;""", [contato.id_contato])

    conn.commit()
    conn.close()

    print('Contato removido com sucesso.')