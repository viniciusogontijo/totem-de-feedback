import sqlite3
import os

def inicializar_banco():
    if not os.path.exists('data'):
        os.makedirs('data')
    
    conn = sqlite3.connect('data/flexmedia_totem.db')
    cursor = conn.cursor()

    cursor.execute(''' create table if not exists totens (
                   id integer primary key autoincrement,
                   localizacao text not null,
                   modelo text)''')

    cursor.execute('''
                   create table if not exists interacoes (
                   id integer primary key autoincrement, 
                   timestamp datetime default current_timestamp, 
                   tipo_interacao text not null,
                   duracao_segundos real check(duracao_segundos >= 0),
                   nota_satisfacao integer not null check(nota_satisfacao between 1 and 5),
                   sentimento text,
                   feedback_texto text,
                   totem_id integer,
                   foreign key (totem_id) references totens(id))
            ''')
    
    cursor.execute("insert or ignore into totens (id, localizacao, modelo) values(1, 'Entrada Principal', 'Flex-V1')")

    conn.commit()
    conn.close()
    print("Banco de dados configurado em data/flexmedia_totem.db")

if __name__ == "__main__":
    inicializar_banco()