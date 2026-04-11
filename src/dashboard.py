import streamlit as st
import pandas as pd
import sqlite3
import os
import plotly.express as px # Adicionado para o gráfico de pizza

st.set_page_config(page_title="Flexmedia Analytics", layout="wide")

# Simula acesso 
st.sidebar.title("Área Restrita")
user = st.sidebar.text_input("Usuário")

if user:
    st.sidebar.success(f"Acesso concedido: {user}")

st.title("Dashboard Flexmedia - Métricas")
st.markdown("---")

def carregar_dados():
    try:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        # Garante que o caminho aponte para a pasta 'data' na raiz do projeto
        db_path = os.path.join(base_dir, 'data', 'flexmedia_totem.db')
        
        if not os.path.exists(db_path):
            return pd.DataFrame()
        
        conn = sqlite3.connect(db_path)
        df = pd.read_sql_query("select * from interacoes", conn)
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        conn.close()
        return df
    except Exception as e:
        st.error(f"Erro ao carregar banco: {e}")
        return pd.DataFrame()

df = carregar_dados()

if not df.empty:
    # Métricas Principais
    m1, m2, m3 = st.columns(3)
    m1.metric("Total de Visitas", len(df))
    m2.metric("NPS Médio", f"{round(df['nota_satisfacao'].mean(), 1)} / 5")
    
    # Prevenção de erro caso não haja sentimentos ainda
    sentimento_comum = df['sentimento'].mode()[0] if not df['sentimento'].empty else "N/A"
    m3.metric("Sentimento Predominante", sentimento_comum)

    # Análise Temporal
    st.subheader("Volume de Engajamento")
    df_tempo = df.set_index('timestamp').resample('min').count()
    st.line_chart(df_tempo['id'])

    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.write("### Performance da IA")
        base_dir = os.path.dirname(os.path.abspath(__file__))
        path_ia = os.path.join(base_dir, 'models', 'metricas_ia.csv')
        
        if os.path.exists(path_ia):
            metricas_ia = pd.read_csv(path_ia)
            st.table(metricas_ia)
        else:
            st.warning("Métricas de IA não encontradas. Execute ml_model.py.")

    with col2:
        st.write("### Distribuição de Sentimentos")
        st.bar_chart(df['sentimento'].value_counts())
    
    with col3:
        st.write("### Engajamento por Tipo de Toque")
        # CORREÇÃO: Usando Plotly Express para o gráfico de pizza
        fig = px.pie(df, names='tipo_interacao', hole=0.3)
        st.plotly_chart(fig, use_container_width=True)

    st.info(f"**Informação:** O sentimento geral predominante é {sentimento_comum}.")
    
    st.markdown("---")
    st.subheader("Análise de Correlação (Insight)")
    chart_data = df[['duracao_segundos', 'nota_satisfacao']]
    st.scatter_chart(chart_data, x='duracao_segundos', y='nota_satisfacao')
    
    st.info("""
        1. **Engajamento:** Toques longos tendem a estar associados a feedbacks mais detalhados.
        2. **Presença:** O sistema de visão computacional (MediaPipe) otimizou a coleta.
        3. **Sentimento:** A IA de NLP (LeIA) identifica nuances além da nota numérica.
        """)
    
    st.markdown("### Últimos Feedbacks Processados")
    st.dataframe(df[['timestamp', 'feedback_texto', 'sentimento', 'nota_satisfacao']].tail(10), use_container_width=True)
    
else:
    st.warning("Aguardando registros de interações no banco de dados...")
