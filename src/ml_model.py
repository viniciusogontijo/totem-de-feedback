from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score
import pandas as pd
import joblib
import os

def treinar_classificador_simples():
    data = {
        'duracao': [0.5, 0.8, 1.2, 3.5, 5.0, 4.2, 0.2, 6.1, 0.4, 7.0, 0.9, 5.5] * 10,
        'tipo': [0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1] * 10
    }

    df = pd.DataFrame(data)
    x = df[['duracao']]
    y = df['tipo']

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

    model = DecisionTreeClassifier()
    model.fit(x_train, y_train)

    y_pred = model.predict(x_test)
    acc = accuracy_score(y_test, y_pred)
    prec = precision_score(y_test, y_pred)

    print(f"Modelo treinado com sucesso, acurácia: {acc:.2f} | precisão: {prec:.2f}")

    if not os.path.exists('models'):
        os.makedirs('models')
        print("Pasta modelos criada.")
    
    caminho_arquivo = 'models/classificador_toque.pkl'
    joblib.dump(model, caminho_arquivo)
    print(f"modelo salvo em: {caminho_arquivo}")

    metrics = pd.DataFrame({'metrica': ['Acurácia', 'Precisão'], 'valor':[acc, prec]})
    metrics.to_csv('models/metricas_ia.csv', index=False)

    return model

if __name__ == "__main__":
    modelo_teste = treinar_classificador_simples()