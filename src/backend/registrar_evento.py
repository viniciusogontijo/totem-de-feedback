import sqlite3
import os
import re

def limpar_texto(texto):
    return re.sub(r'[^\w\s,.!?]', '', texto)

def registrar_evento(tipo, duracao, nota, texto, sentimento="Neutro", totem_id= 1):
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, '..', 'data', 'flexmedia_totem.db')
    print(db_path)

    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        texto_limpo = limpar_texto(texto) if texto else "Sem comentário"

        query = "insert into interacoes (tipo_interacao, duracao_segundos, nota_satisfacao, sentimento, feedback_texto, totem_id) values(?, ?, ?, ?, ?, ?)"

        cursor.execute(query, (tipo, duracao, nota, sentimento, texto_limpo, totem_id))
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f"Erro ao salvar:{e}")
        return False
