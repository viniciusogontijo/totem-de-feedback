import sqlite3
import random
import time
import os

def registrar_evento(tipo, duracao, nota, texto):
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir,'data', 'flexmedia_totem.db')
    print(db_path)

    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        texto_limpo = texto.strip() if texto else "Sem comentário"

        query = "insert into interacoes (tipo_interacao, duracao_segundos, nota_satisfacao, feedback_texto) values(?, ?, ?, ?)"

        cursor.execute(query, (tipo, duracao, nota, texto_limpo))
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f"Erro ao salvar:{e}")
        return False
    
if __name__ == "__main__":
    print("Simulando interações no totem...")
    for _ in range(5):
        tipo = random.choice(["Curto", "Longo"])
        duracao = round(random.uniform(1.0, 15.0), 2)
        nota = random.randint(1, 5)
        registrar_evento(tipo, duracao, nota, "Feedback automático via sensor")
        time.sleep(0.5)
    print("simulação concluída.")