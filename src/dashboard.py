import streamlit as st
import pandas as pd
import sqlite3
import os

st.set_page_config(page_title="Flexmedia Dashboard", layout="wide")
st.title("Dashboard Flexmedia - Métricas")

def carregar_dados():
    try:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(base_dir,'data', 'flexmedia_totem.db')
        if not os.path.exists(db_path):
            return pd.DataFrame()
        
        conn = sqlite3.connect(db_path)
        df = pd.read_sql_query("select * from interacoes", conn)
        conn.close()
        return df
    except:
        return pd.DataFrame()

df = carregar_dados()

if not df.empty:
    col1, col2 = st.columns(2)

    with col1:
        st.metric("Total de Ativações", len(df))
        st.write("### Histórico de Decisões da IA")
        st.dataframe(df.sort_values(by='timestamp', ascending=False), use_container_width=True)

    with col2:
        st.metric("Média de Satifação", f"{round(df['nota_satisfacao'].mean(), 1)} / 5")
        st.write("### Volume por Tipo de Interação")
        st.bar_chart(df['tipo_interacao'].value_counts())
    
else:
    st.warning("Banco de dados não encontrado ou vazio. Execute os de simulação primeiro.")