import random
import time
import joblib
import os

from registrar_evento import registrar_evento
from detecta_service import detectar_presenca

def classificar_sentimento_simulado(nota):
    #simulaça de nlp só para demonstra o fluxo de analise)
    if nota >= 4: return "Positivo"
    if nota <= 2: return "Negativo"
    return "Neutro"

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

        #Predição IA
        tipo_ia = "Longo" if modelo_ia.predict([[duracao]])[0] == 1 else "Curto"

        #Analise de sentimento nlp simulado
        sentimento = classificar_sentimento_simulado(nota)
        registrar_evento(tipo_ia, duracao, nota, "Interação automatizada", sentimento)
        time.sleep(0.5)

if __name__ == "__main__":
    TESTE_SEM_CAM = True
    print("Simulando interações no totem...")
    executar_totem(modo_teste= TESTE_SEM_CAM)
