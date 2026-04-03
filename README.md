#Tótem de Feedback Inteligente#

A Flexmedia busca transformar espaços físicos em ambientes inteligentes, utilizando IA e sensores para medir engajamento e oferecer experiências personalizadas.
**O Problema:** A dificuldade de coletar e analisar o sentimento dos visitantes de forma automática e em tempo real em espaços culturais ou comerciais.
**A Solução:** Um Tótem Inteligente que utiliza Processamento de Linguagem Natural (NLP) e Visão Computacional para interpretar feedbacks, classificar emoções e gerar dashboards analíticos para a gestão do espaço.

##Tecnologias Utilizadas## 
Para garantir a viabilidade técnica e a integração exigida, as seguintes tecnologias foram selecionadas:
**Linguagem:** Python (pela versatilidade em IA e tratamento de dados).
**Inteligência Artificial:** Bibliotecas *TextBlob* ou *Scikit-learn* para análise de sentimento e *OpenCV* para detecção de presença ou expressões.
**Banco de Dados:** *SQLite* para armazenamento estruturado local, facilitando a portabilidade do protótipo.
**Interface/Dashboard:** *Streamlit*, permitindo criar uma interface web interativa de forma ágil.
**Hardware (Opcional/Simulado):** *Microcontrolador ESP32* com sensor infravermelho para detectar a aproximação física do usuário.

##Arquitetura da Solução##
A arquitetura segue um pipeline de dados linear e eficiente, garantindo que a informação flua desde a captura até o insight final.
**Coleta (Input):** Captura de texto via interface ou presença via sensor ESP32.
**Processamento:** Limpeza de dados e aplicação de modelos de IA para classificação de sentimento.
**Armazenamento:** Registro da interação, nota e categoria de sentimento no banco SQL.
**Visualização:** Geração de gráficos de engajamento e métricas de satisfação em tempo real.

##Estratégia de Coleta de Dados##
A coleta será baseada em eventos de interação.
**Dados Iniciais:** Serão utilizados dados simulados e exemplos fictícios para validar a arquitetura antes da implementação final.
**Métricas:** O sistema registrará o horário da visita, a nota de satisfação (1-5) e o conteúdo textual do feedback.

##Segurança e Privacidade##
Alinhado com as necessidades da Flexmedia, o projeto adotará estratégias de proteção:
**Anonimização:** Não serão coletados dados sensíveis ou identificadores pessoais (como nomes ou documentos).
**Integridade:** Validação de entradas para evitar registros corrompidos no banco de dados.

##Plano de Desenvolvimento##
O desenvolvimento será dividido em módulos:
###Fase 1### 
Estruturação do Banco de Dados e lógica de armazenamento.
###Fase 2### 
Implementação dos modelos de IA e análise de padrões.
###Fase 3:### 
Desenvolvimento da interface visual e dashboard de métricas 
###Fase 4:### 
Integração final, testes com dados simulados e gravação do vídeo.
