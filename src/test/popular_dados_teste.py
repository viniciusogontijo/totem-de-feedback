import random
import time
import joblib
import os
import pandas as pd
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from backend.registrar_evento import registrar_evento
from backend.analisar_texto import analisar_sentimento_nlp, gerar_resposta_automatizada

def gerar_dados_simulados(quantidade):
    try:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        model_path = os.path.join(base_dir, '..', 'models', 'classificador_toque.pkl')
        modelo_ia = joblib.load(model_path)
        print("Modelo de IA carregado")
    except Exception as e:
        print(f"Erro ao carregar modelo de IA:{e}")
        modelo_ia = None

    for i in range(quantidade):
        print(f"Capturando interação simulada {i + 1} de {quantidade}...")
        
        duracao = round(random.uniform(0.1, 10.0), 2)
        nota = random.randint(1, 5)

        comentarios = [
            "Amei a exposição!",
            "Muito confuso o caminho.",
            "Espaço agradável.",
            "Faltou informação nas placas.",
            "Adorei a interatividade do totem.",
            "Poderia ter mais opções de lanches.",
            "Experiência fantástica, voltarei com a família!",
            "Não consegui achar o banheiro."
        ]
        texto = random.choice(comentarios)
        tipo_ia = "Padrão"
        if modelo_ia is not None:
            entrada_ia = pd.DataFrame([[duracao]], columns=['duracao'])
            tipo_ia = "Longo" if modelo_ia.predict(entrada_ia)[0] == 1 else "Curto"

        sentimento = analisar_sentimento_nlp(texto)
        sucesso = registrar_evento(tipo_ia, duracao, nota, texto, sentimento)
        
        if sucesso:
            resposta = gerar_resposta_automatizada(sentimento)
            print(f"  -> Totem diria: {resposta}")
        else:
            print("  -> Erro ao salvar no banco.")
            
        time.sleep(0.5)

        print("Simulação concluída")

if __name__ == "__main__":
    QTD_INTERACOES = 100 
    gerar_dados_simulados(QTD_INTERACOES)