import streamlit as st
import time
import requests

st.set_page_config(page_title="Totem Flexmedia", page_icon="🤖", layout="centered")

URL_API_INTERACAO = "http://127.0.0.1:8000/processar_interacao"
URL_API_SENSOR = "http://127.0.0.1:8000/verificar_presenca"

st.title("Totem Inteligente Flexmedia")
if 'visitante_presente' not in st.session_state:
    st.session_state.visitante_presente = False

st.sidebar.header("Painel de Controle do Totem")
mode_teste = st.sidebar.checkbox("Modo Teste (Usar imagem estática)", value=True)

st.markdown("### Sensor de Aproximação")

if st.button("Simular Aproximação de Visitante", type="primary", use_container_width=True):
    with st.spinner("Ativando sensor de visão computacional..."):
        try:
            resposta_sensor = requests.get(f"{URL_API_SENSOR}?modo_teste={mode_teste}")
            if resposta_sensor.status_code == 200:
                dados_sensor = resposta_sensor.json()

                if dados_sensor['alguem_presente']:
                    st.session_state.visitante_presente = True
                    st.session_state.start_time = time.time()
                    st.success("Visitante detectado! Tela Liberada.")
                else:
                    st.session_state.visitante_presente = True
                    st.warning("Ninguém detectado.")
        except requests.exceptions.ConnectionError:
            st.error("Erro de conexão com o sensor.")


if st.session_state.visitante_presente:
    st.title("Bem-vindo(a) à Exposição!")
    st.markdown("Sua opinião nos ajuda a criar experiências cada vez melhores.")

    with st.form("feedback_form", clear_on_submit=True):
        nota = st.slider("Como você avalia sua experiência hoje?", min_value=1, max_value=5, value=5)
        texto_feedback = st.text_area("Conte-nos mais sobre sua visita (opcional):")
        submitted = st.form_submit_button("Enviar Feedback", use_container_width=True)
        
        if submitted:
            duracao = round(time.time() - st.session_state.start_time, 2)

            payload = {
                "nota": nota,
                "texto": texto_feedback if texto_feedback else "Sem comentário",
                "duracao": duracao
            }
            try:
                response = requests.post(URL_API_INTERACAO, json = payload)

                if response.status_code == 200:
                    dados_response = response.json()
                    st.success("Feedback processado com sucesso!")
                    st.info(f"🤖 **O Totem diz:** {dados_response['resposta_totem']}")
                else:
                    st.error("Erro no processamento do servidor.")
            except requests.exceptions.ConnectionError:
                st.error("Servidor offline.")


