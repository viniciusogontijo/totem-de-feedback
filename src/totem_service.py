import random
import time
import joblib
import os
import pandas as pd

from registrar_evento import registrar_evento

try:
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir,'models', 'classificador_toque.pkl')

    modelo_ia = joblib.load(db_path)
except:
    print("Erro: Modelo não encontrado! Rode o ml_model.py primeiro.")
    exit()

def registrar_evento_ia(duracao, nota, texto):
    X_novo = pd.DataFrame([[duracao]], columns=['duracao'])
    predicao = modelo_ia.predict(X_novo)
    tipo_ia = "Longo" if predicao[0] == 1 else "Curto"

    return registrar_evento(tipo_ia, duracao, nota, texto)

if __name__ == "__main__":
    print("Simulando interações no totem...")
    for _ in range(5):
        duracao = round(random.uniform(1.0, 15.0), 2)
        nota = random.randint(1, 5)
        registrar_evento_ia(duracao, nota, "Interação via IA")
        time.sleep(0.5)
    print("simulação concluída.")
