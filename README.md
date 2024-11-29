# Interagindo com LLMs através de API

Parte 2 do Teste de Performance 2 da disciplina Desenvolvimento de Data-Driven Apps com Python

## Clonando o respositório

```
git clone https://github.com/Leticia-Infnet/leticia_abreu_DR3_TP2_parte2.git
```

## Instalando dependências

```
pip install -r requirements.txt
```

⚠️ATENÇÃO⚠️

A biblioteca torch não está listada no requirements.txt. Isso porque as bibliotecas do Pytorch tem suportes específicos para o tipo de OS e arquitetura (CUDA ou CPU) do seu computador. Acesse este [link](https://pytorch.org/) para instalar a versão certa para sua máquina

## Criando arquivo .env

Na raíz do seu projeto, crie um arquivo .env com sua chave do Gemini no seguinte formato: GOOGLE_API_KEY = MINHA_API_KEY

## Ativando o server uvicorn

1. Da raíz do projeto, digite:

```
python ./src/main.py
```

## Requisições para o server

Se você seguiu todos os passos, o servirdor estará rodando em http://127.0.0.1:8000. Faça requisições através da sua ferramenta preferida (Postman, HTTPie, curl, lib request). Para saber detalhes sobre a API, confira a [documentação](docs).
