# Totem de Feedback Inteligente

A Flexmedia busca transformar espaços físicos em ambientes inteligentes, utilizando IA e sensores para medir engajamento e oferecer experiências personalizadas.

🚩 ## O Problema

A dificuldade de coletar e analisar o sentimento dos visitantes de forma automática e em tempo real em espaços culturais ou comerciais.

💡 ## A Solução

Um Totem Inteligente que utiliza Processamento de Linguagem Natural (NLP) e Visão Computacional para interpretar feedbacks, classificar emoções e gerar dashboards analíticos para a gestão do espaço.

🛠 ## Tecnologias Utilizadas
Para garantir a viabilidade técnica e a integração exigida, as seguintes tecnologias foram selecionadas:

**Linguagem:** 
_Python_ (pela versatilidade em IA e tratamento de dados).

**Inteligência Artificial:**
_TextBlob_ ou _Scikit-learn_ (Análise de sentimento).
_OpenCV_ (Detecção de presença e expressões).

**Banco de Dados:** 
_SQLite_ (Armazenamento estruturado local e portabilidade).

**Interface/Dashboard:** 
_Streamlit_ (Interface web interativa e ágil).

**Hardware (Opcional/Simulado):** 
Microcontrolador _ESP32_ com sensor infravermelho.

🏗 Arquitetura da Solução
A arquitetura segue um pipeline de dados linear e eficiente:

Coleta (Input): Captura de texto via interface ou detecção de presença via sensor ESP32.

Processamento: Limpeza de dados e aplicação de modelos de IA para classificação de sentimento.

Armazenamento: Registro da interação, nota e categoria de sentimento no banco SQL.

Visualização: Geração de gráficos de engajamento e métricas de satisfação em tempo real.

📊 Estratégia de Coleta de Dados
A coleta será baseada em eventos de interação.

Dados Iniciais: Serão utilizados dados simulados e exemplos fictícios para validar a arquitetura antes da implementação final.

Métricas: O sistema registrará o horário da visita, a nota de satisfação (1-5) e o conteúdo textual do feedback.

🔒 Segurança e Privacidade
Alinhado com as diretrizes da Flexmedia, o projeto adota:

Anonimização: Não são coletados dados sensíveis ou identificadores pessoais (LGPD friendly).

Integridade: Validação de entradas para evitar registros corrompidos no banco de dados.
