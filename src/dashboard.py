import streamlit as st
import pandas as pd
import sqlite3
import os

st.set_page_config(page_title="Flexmedia Analytics", layout="wide")

#Simula acesso 
st.sidebar.title("Área Restrita")
user = st.sidebar.text_input("Usuário")

if user:
    st.sidebar.success(f"Acesso concedido: {user}")

st.title("Dashboard Flexmedia - Métricas")
st.markdown("---")

def carregar_dados():
    try:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(base_dir,'data', 'flexmedia_totem.db')
        if not os.path.exists(db_path):
            return pd.DataFrame()
        
        conn = sqlite3.connect(db_path)
        df = pd.read_sql_query("select * from interacoes", conn)
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        conn.close()
        return df
    except:
        return pd.DataFrame()

df = carregar_dados()

if not df.empty:
    # Métricas 
    m1, m2, m3 = st.columns(3)
    m1.metric("Total de Visitas", len(df))
    m2.metric("NPS Médio", f"{round(df['nota_satisfacao'].mean(), 1)} / 5")
    m3.metric("Sentimento Predominate", df['sentimento'].mode()[0])

    # Analise
    st.subheader("Volume de Engajamento")
    df_tempo = df.set_index('timestamp').resample('min').count()
    st.line_chart(df_tempo['id'])

    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir,'models', 'metricas_ia.csv')
    col1, col2 = st.columns(2)
    with col1:
        st.write("### Performance da IA")
        metricas_ia = pd.read_csv(db_path)
        st.table(metricas_ia)

    with col2:
        st.write("Distribuição de Sentimentos")
        st.bar_chart(df['sentimento'].value_counts())
    
    st.info(f"**Informação:** O pico de interações ocorreu às {df['timestamp'].dt.hour.mode()[0]}h. O sentimento geral é {df['sentimento'].mode()[0]}." )
    
else:
    st.error("Carregando...")