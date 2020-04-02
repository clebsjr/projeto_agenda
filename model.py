from connection import connection_db
from contextlib import closing

model_table = 'contato'


def insert(contato):
    with closing(connection_db()) as conn:
        with closing(conn.cursor()) as c:
            sql = f"""
                    INSERT INTO {model_table} (nome, email, telefone)
                    VALUES (?,?,?)"""

            c.execute(sql, (contato.nome, contato.email, contato.telefone))
            conn.commit()


def update(contato):
    with closing(connection_db()) as conn:
        with closing(conn.cursor()) as c:
            sql = f"""
                    UPDATE {model_table} SET
                                        nome = ?,
                                        email = ?,
                                        telefone = ?
                    WHERE id = ?"""

            c.execute(sql, (contato.nome, contato.email, contato.telefone, contato.id))
            conn.commit()


def select_all():
    with closing(connection_db()) as conn:
        with closing(conn.cursor()) as c:
            sql = f'SELECT * FROM {model_table}'
            c.execute(sql)
            return c.fetchall()


def delete(id):
    with closing(connection_db()) as conn:
        with closing(conn.cursor()) as c:
            sql = f'DELETE FROM {model_table} WHERE id = ?'
            c.execute(sql, (id,))
            conn.commit()


def select_one(id):
    with closing(connection_db()) as conn:
        with closing(conn.cursor()) as c:
            sql = f'SELECT * FROM {model_table} WHERE id = ?'
            c.execute(sql, (id,))
            return c.fetchone()