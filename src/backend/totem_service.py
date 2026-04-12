from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from registrar_evento import registrar_evento
from detecta_service import detectar_presenca
from analisar_texto import analisar_sentimento_nlp, gerar_resposta_automatizada
import joblib
import os
import pandas as pd

app = FastAPI(title="API Totem Flexmedia")

try:
    base_dir = os.path.dirname(os.path.abspath(__file__))
    models_path = os.path.normpath(os.path.join(base_dir, '..', 'models'))
    models_pkl_path = os.path.join(models_path, 'classificador_toque.pkl')
    modelo_ia = joblib.load(models_pkl_path)
    print("Status: Sensores Online.") #simula entrda de dados via leitor esp32
except Exception as e:
    print("Erro: Modelo não inicializado. {e}")
    modelo_ia = None

class InteracaoUsuario(BaseModel):
    nota: int
    texto: str
    duracao: float

@app.post("/processar_interacao")
def processar_interacao(dados: InteracaoUsuario):
    try:
        tipo_ia = "Padrão"
        if modelo_ia is not None:
            entrada_ia = pd.DataFrame([[dados.duracao]], columns=['duracao'])
            tipo_ia = "Longo" if modelo_ia.predict(entrada_ia)[0] == 1 else "Curto"

        # Análise de sentimento nlp
        sentimento = analisar_sentimento_nlp(dados.texto) if dados.texto else "Neutro"

        # Registrar no banco
        sucesso = registrar_evento(tipo_ia, dados.duracao, dados.nota, dados.texto, sentimento)

        if not sucesso:
            raise HTTPException(status_code=500, detail="Erro ao registrar, tente mais tarde.")
        
        resposta_totem = gerar_resposta_automatizada(sentimento)

        return {
            "status": "sucesso",
            "tipo_toque": tipo_ia,
            "sentimento": sentimento,
            "resposta_totem": resposta_totem
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro no servidor")


@app.get("/verificar_presenca")
def verificar_presenca(modo_teste: bool = False):
    try:
        if modo_teste:
            
            base_dir = os.path.dirname(os.path.abspath(__file__))
            arquivo_teste = os.path.normpath(os.path.join(base_dir, '..', 'img', 'image.png'))
            alguem_presente = detectar_presenca(arquivo_teste)
        else:
            alguem_presente = detectar_presenca()
        
        return{
            "status": "sucesso",
            "alguem_presente": alguem_presente
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro no sensor: {str(e)}")