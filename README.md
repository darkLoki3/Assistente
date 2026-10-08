# Assistente Virtual Kidy / Kidy Virtual Assistant

## PT-BR | Português (Brasil)

### Descrição
Este repositório contém um projeto de assistente virtual em Python, desenvolvido para interagir com o usuário por meio de conversa em linguagem natural. O sistema utiliza classificação de intenções para decidir como responder e também inclui integrações com funcionalidades como clima, localização, navegação e um fluxo específico para atendimento do projeto Kidy.

### Objetivo do projeto
O objetivo principal é criar uma base para um assistente inteligente que possa:

- responder perguntas simples e conversas gerais;
- identificar a intenção do usuário;
- buscar informações como clima e localização;
- abrir conteúdos no navegador;
- apoiar o fluxo de avaliação do projeto Kidy.

### Funcionalidades
- Conversa em linguagem natural;
- Classificação de intenções;
- Respostas personalizadas;
- Consulta de clima;
- Busca de localização;
- Abertura de páginas no navegador;
- Fluxo de execução para avaliação Kidy.

### Roadmap


<!-- ROADMAP_PROGRESS_PT_START -->
**Progresso: 13%**
███░░░░░░░░░░░░░░░░░ 13%

Milestone atual: **v1.0**
- Concluídas: 1
- Total: 8
<!-- ROADMAP_PROGRESS_PT_END -->


### Estrutura do projeto

```text
Assistente/
├── assistant_functions/
│   ├── __init__.py
│   ├── Abrir_Navegador.py
│   ├── acordar.py
│   ├── Fala_Escuta.py
│   ├── localizacao.py
│   ├── resposta.py
│   ├── similar.py
│   └── weather.py
├── intent_classification/
│   ├── data.csv
│   └── intent_classification.py
├── database.py
├── fluxo_kidy.py
├── main.py
├── pyproject.toml
├── README.md
├── requirements.txt
├── sensor_kidy.py
├── SECURITY.md
├── voz.py
├── teste/
│   ├── div_test.py
│   ├── soma_test.py
│   ├── test_database.py
│   ├── test_fluxo_kidy_sensor.py
│   └── test_fluxo_kidy.py
└── webhook-listener/
```

### Requisitos
- Python 3.10 ou superior;
- pip instalado;
- ambiente virtual recomendado.

### Instalação
1. Clone o repositório:

```bash
git clone https://github.com/darkLoki3/Assistente.git
cd Assistente
```

2. Crie um ambiente virtual:

```bash
python -m venv .venv
source .venv/bin/activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

### Como executar
Para iniciar o assistente principal:

```bash
python main.py
```

Para executar o fluxo Kidy:

```bash
python main.py --kidy-flow
```

### Fluxo de funcionamento
1. O usuário digita uma mensagem;
2. o arquivo `main.py` chama o método `Assistant.responde()`;
3. o classificador de intenções identifica a intenção;
4. a resposta correta é direcionada para a função adequada;
5. o assistente retorna a resposta ou executa a ação solicitada.

### Como testar
O projeto já inclui testes em `teste/`.

```bash
pytest
```

---

## EN | English

### Description
This repository contains a Python virtual assistant project designed to interact with users through natural language conversations. The system uses intent classification to decide how to respond and also includes integrations for weather, location, browser access, and a specific flow for the Kidy project.

### Project goal
The main goal is to create a foundation for an intelligent assistant that can:

- answer simple questions and general conversations;
- identify the user intent;
- fetch information such as weather and location;
- open content in the browser;
- support the Kidy evaluation workflow.

### Features
- Natural language conversation;
- Intent classification;
- Personalized responses;
- Weather lookup;
- Location search;
- Browser access;
- Kidy workflow execution.


### Roadmap
<!-- ROADMAP_PROGRESS_EN_START -->
**Progress: 13%**
███░░░░░░░░░░░░░░░░░ 13%

Current milestone: **v1.0**
- Completed: 1
- Total: 8
<!-- ROADMAP_PROGRESS_EN_END -->

### Project structure

```text
Assistente/
├── assistant_functions/
│   ├── __init__.py
│   ├── Abrir_Navegador.py
│   ├── acordar.py
│   ├── Fala_Escuta.py
│   ├── localizacao.py
│   ├── resposta.py
│   ├── similar.py
│   └── weather.py
├── intent_classification/
│   ├── data.csv
│   └── intent_classification.py
├── database.py
├── fluxo_kidy.py
├── main.py
├── pyproject.toml
├── README.md
├── requirements.txt
├── sensor_kidy.py
├── SECURITY.md
├── voz.py
├── teste/
│   ├── div_test.py
│   ├── soma_test.py
│   ├── test_database.py
│   ├── test_fluxo_kidy_sensor.py
│   └── test_fluxo_kidy.py
└── webhook-listener/
```

### Requirements
- Python 3.10 or higher;
- pip installed;
- a virtual environment is recommended.

### Installation
1. Clone the repository:

```bash
git clone https://github.com/darkLoki3/Assistente.git
cd Assistente
```

2. Create a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

### How to run
To start the main assistant:

```bash
python main.py
```

To run the Kidy flow:

```bash
python main.py --kidy-flow
```

### Workflow
1. The user enters a message;
2. `main.py` calls `Assistant.responde()`;
3. the intent classifier identifies the intention;
4. the appropriate function is called;
5. the assistant returns the answer or executes the requested action.

### Testing
The project already includes tests in the `teste/` folder.

```bash
pytest
```

### Author
Felipe Carvalho
