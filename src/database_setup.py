import sqlite3
import os

def inicializar_banco():
    if not os.path.exists('data'):
        os.makedirs('data')
    
    conn = sqlite3.connect('data/flexmedia_totem.db')
    cursor = conn.cursor()

    cursor.execute('''
        create table if not exists interacoes (
                   id integer primary key autoincrement, 
                   timestamp datetime default current_timestamp, 
                   tipo_interacao text,
                   duracao_segundos real,
                   nota_satisfacao integer,
                   feedback_texto text)
    ''')
    conn.commit()
    conn.close()
    print("Banco de dados configurado em data/flexmedia_totem.db")

if __name__ == "__main__":
    inicializar_banco()