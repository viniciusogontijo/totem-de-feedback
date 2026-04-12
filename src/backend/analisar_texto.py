from LeIA import SentimentIntensityAnalyzer

senti = SentimentIntensityAnalyzer()

def analisar_sentimento_nlp(texto):
    score = senti.polarity_scores(texto)['compound']

    print(f"Score: {score} | Texto: {texto}")
    
    if score >= 0.05:
        return "Positivo"
    elif score <= -0.05:
        return "Negativo"
    else:
        return "Neutro"

def gerar_resposta_automatizada(sentimento):
    if sentimento == "Positivo":
        return "Ficamos felizes com sua visita! Não deixe de conferir a ala principal."
    elif sentimento == "Negativo":
        return "Lamentamos a experiência. Sua sugestões foram enviadas à curadoria."
    return "Obrigado pela sua participação!"