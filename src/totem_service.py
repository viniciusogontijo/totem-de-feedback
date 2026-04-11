import random
import time
import joblib
import os
import pandas as pd

from registrar_evento import registrar_evento
from detecta_service import detectar_presenca
from analisar_texto import analisar_sentimento_nlp, gerar_resposta_automatizada

def executar_totem(modo_teste=False):

    ARQUIVO_TESTE = "img/image.png"

    try:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(base_dir,'models', 'classificador_toque.pkl')
        modelo_ia = joblib.load(db_path)
        print("Status: Sensores Online.") #simula entrda de dados via leitor esp32
    except:
        print("Erro: Modelo não inicializado.")
        return
    
    # verificando presença via mediapipe se tiver alguém segue no fluxo de ativação do totem
    if modo_teste:
        alguem_presente = detectar_presenca(ARQUIVO_TESTE)
    else:
        alguem_presente = detectar_presenca()
    
    if not alguem_presente:
        print("Ninguém detectado.")
        return

    for i in range(3):
        print(f"Capturando interação {i + 1}...")
        duracao = round(random.uniform(0.1, 10.0), 2)
        nota = random.randint(1, 5)

        comentarios = [
            "Amei a exposição!",
            "Muito confuso o caminho.",
            "Espaço agradável.",
            "Faltou informação nas placas."
        ]
        texto = random.choice(comentarios)

        #Predição IA
        entrada_ia = pd.DataFrame([[duracao]], columns=['duracao'])
        tipo_ia = "Longo" if modelo_ia.predict(entrada_ia)[0] == 1 else "Curto"

        sentimento = analisar_sentimento_nlp(texto)

        #Analise de sentimento nlp simulado
        registrar_evento(tipo_ia, duracao, nota, "Interação automatizada", sentimento)
        resposta = gerar_resposta_automatizada(sentimento)
        print(f"Totem diz: {resposta}")
        time.sleep(0.5)

if __name__ == "__main__":
    TESTE_SEM_CAM = True
    print("Simulando interações no totem...")
    executar_totem(modo_teste= TESTE_SEM_CAM)
