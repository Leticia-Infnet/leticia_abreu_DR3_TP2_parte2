Aqui está a documentação da sua API em Markdown:

# 📡 Documentação da API de Tradução e Geração de Texto

## 🚀 Visão Geral

Esta API oferece três serviços principais:

- Geração de texto com LLM Fake
- Tradução usando Gemini (Inglês para Francês)
- Tradução usando Helsinki (Inglês para Alemão)

## 🔧 Configuração

### Dependências Principais

- FastAPI
- Langchain
- Transformers
- Hugging Face
- Google Generative AI

## 📊 Endpoints

### 1. Status do Servidor

- **URL**: `/status`
- **Método**: POST
- **Descrição**: Verifica o status do servidor
- **Resposta de Exemplo**:
  ```json
  {
    "message": "O servirdor está rodando!"
  }
  ```

### 2. Gerador de Texto Fake LLM

- **URL**: `/fake/fakellm`
- **Método**: POST
- **Descrição**: Gera texto aleatório usando um LLM simulado
- **Payload**:
  ```json
  {
    "phrase": "string"
  }
  ```
- **Resposta de Exemplo**:
  ```json
  {
    "assistant": "Dois mais dois é igual à quatro"
  }
  ```

### 3. Tradutor Gemini

- **URL**: `/translate/gemini`
- **Método**: POST
- **Descrição**: Traduz texto do inglês para o francês
- **Payload**:
  ```json
  {
    "phrase": "Hello, how are you?"
  }
  ```
- **Resposta de Exemplo**:
  ```json
  {
    "assistant": "Bonjour comment allez-vous?"
  }
  ```

### 4. Tradutor Helsinki

- **URL**: `/translate/helsinki`
- **Método**: POST
- **Descrição**: Traduz texto do inglês para o alemão
- **Payload**:
  ```json
  {
    "phrase": "Good morning"
  }
  ```
- **Resposta de Exemplo**:
  ```json
  {
    "assistant": "Guten Morgen"
  }
  ```

## 🛠 Configurações Técnicas

### Gemini Translator

- **Modelo**: Gemini 1.5 Flash
- **Temperatura**: 0.3
- **Máximo de Tokens**: 200
- **Timeout**: 10 segundos

### Helsinki Translator

- **Modelo**: Helsinki-NLP/opus-mt-en-de
- **Dispositivo**: CUDA (se disponível), senão CPU
- **Máximo de Novos Tokens**: 200

## 🔒 Segurança

- Utiliza variáveis de ambiente para chaves de API
- Suporta cache de LLM em memória

## 📈 Monitoramento

- Monitoramento de latência implementado para endpoints de tradução

## 🚧 Considerações

- As traduções são geradas por modelos de IA
- A qualidade pode variar dependendo da complexidade do texto
