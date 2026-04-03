# Totem de Feedback Inteligente

A Flexmedia busca transformar espaços físicos em ambientes inteligentes, utilizando IA e sensores para medir engajamento e oferecer experiências personalizadas.

## 🚩 O Problema
A dificuldade de coletar e analisar o sentimento dos visitantes de forma automática e em tempo real em espaços culturais ou comerciais.

## 💡 A Solução
Um Totem Inteligente que utiliza Processamento de Linguagem Natural (NLP) e Visão Computacional para interpretar feedbacks, classificar emoções e gerar dashboards analíticos para a gestão do espaço.

### 🛠 Tecnologias Utilizadas
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

### 🏗 Arquitetura da Solução
A arquitetura segue um pipeline de dados linear e eficiente:

**Coleta (Input):** Captura de texto via interface ou detecção de presença via sensor ESP32.

**Processamento:** Limpeza de dados e aplicação de modelos de IA para classificação de sentimento.

**Armazenamento:** Registro da interação, nota e categoria de sentimento no banco SQL.

**Visualização:** Geração de gráficos de engajamento e métricas de satisfação em tempo real.

### 📊 Estratégia de Coleta de Dados
A coleta será baseada em eventos de interação.

**Dados Iniciais:** Serão utilizados dados simulados e exemplos fictícios para validar a arquitetura antes da implementação final.

**Métricas:** O sistema registrará o horário da visita, a nota de satisfação (1-5) e o conteúdo textual do feedback.

### 🔒 Segurança e Privacidade
Alinhado com as diretrizes da Flexmedia, o projeto adota:

**Anonimização:** Não são coletados dados sensíveis ou identificadores pessoais (LGPD friendly).

**Integridade:** Validação de entradas para evitar registros corrompidos no banco de dados.

### 🧠 Lógica de Machine Learning
O modelo utiliza a Duração do Toque como feature para classificar a interação em dois tipos:

**Toque Curto:** Geralmente associado a seleções rápidas.

**Toque Longo:** Pode indicar dúvida ou uma interação específica configurada no totem.

### 🛠️ Tecnologias Utilizadas
**Linguagem:** Python 3.x

**Banco de Dados:** SQLite (SQL)

**IA/ML:** Scikit-Learn (Decision Tree Classifier)

**Dashboard:** Streamlit

**Manipulação de Dados:** Pandas

### 📂 Estrutura do Projeto
flexmedia-totem/
├── src/                    # Código-fonte do projeto
|   ├── data/               # Banco de dados SQLite (.db)
|   ├── models/             # Modelos de ML treinados (.pkl)
│   ├── database_setup.py   # Configuração inicial do banco SQL
│   ├── ml_model.py         # Treinamento do modelo de Machine Learning
│   ├── totem_service.py    # Simulação de sensores e integração com IA
│   └── dashboard.py        # Interface visual com Streamlit
├── requeridos.txt          # Dependências do projeto
└── README.md               # Documentação

### ⚙️ Como Executar o Projeto
**Instalar Dependências:** python -m pip install -r requeridos.txt
**Inicializar o Banco de Dados:** python src/database_setup.py
**Treinar a Inteligência Artificial:** python src/ml_model.py
**Simular Interações do Totem:** python src/totem_service.py
**Iniciar o Dashboard:** streamlit run src/dashboard.py
_O dashboard abrirá automaticamente no seu navegador padrão (geralmente em http://localhost:8501)_
