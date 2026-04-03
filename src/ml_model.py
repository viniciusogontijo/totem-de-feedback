from sklearn.tree import DecisionTreeClassifier
import pandas as pd
import joblib
import os

def treinar_classificador_simples():
    data = {
        'duracao': [0.5, 0.8, 1.2, 3.5, 5.0, 4.2, 0.2, 6.1],
        'tipo': [0, 0, 0, 1, 1, 1, 0, 1]
    }

    df = pd.DataFrame(data)
    x = df[['duracao']]
    y = df['tipo']

    model = DecisionTreeClassifier()
    model.fit(x, y)

    print("Modelo treinado com sucesso!")

    if not os.path.exists('models'):
        os.makedirs('models')
        print("Pasta modelos criada.")
    
    caminho_arquivo = 'models/classificador_toque.pkl'
    joblib.dump(model, caminho_arquivo)
    print(f"modelo salvo em: {caminho_arquivo}")

    return model

if __name__ == "__main__":
    modelo_teste = treinar_classificador_simples()