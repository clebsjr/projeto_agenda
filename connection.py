import sqlite3
from sqlite3 import Error
from contextlib import closing

db_name = 'agenda.db'
model_table = 'contato'


def connection_db():
    try:
        conn = sqlite3.connect(db_name)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table():
    with closing(connection_db()) as conn, closing(conn.cursor()) as c:
        sql = f""" CREATE TABLE IF NOT EXISTS {model_table} (
                                        id integer PRIMARY KEY AUTOINCREMENT,
                                        nome text NOT NULL,
                                        email text NOT NULL,
                                        telefone text NOT NULL
                                    ); """
        c.execute(sql)
        conn.commit()


if __name__ == '__main__':
    create_table()
