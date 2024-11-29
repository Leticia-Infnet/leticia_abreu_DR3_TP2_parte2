import os
from fastapi import APIRouter
from dotenv import load_dotenv

# Imports langchain
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

# Imports locais
from models.gemini_translator import GeminiTranslator, ChatModel, ChatResponseModel
from .utils.latency_monitor import monitor_latency

load_dotenv(os.path.abspath(os.path.join('.', '.env')))

api_key = os.environ.get('GOOGLE_API_KEY')

router = APIRouter()

llm = ChatGoogleGenerativeAI(
    api_key=api_key,
    verbose=False,
    model='gemini-1.5-flash',
    temperature=0.3,
    max_tokens=200,
    top_p=0.85,
    timeout=10,
    max_retries=2,
    transport='grpc'
)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful assistant that translates English to French.",
        ),
        ("human", "{input}"),
    ]
)

chain = prompt | llm


@router.post('/gemini')
@monitor_latency()
async def gemini_translator(phrase: GeminiTranslator) -> ChatResponseModel:
    """
Endpoint para tradução de texto do inglês para o francês utilizando o modelo Gemini.
Este endpoint recebe uma frase como entrada e retorna sua tradução processada pelo modelo Gemini.
Args:
    phrase (GeminiTranslator): Objeto JSON contendo a frase a ser traduzida
        Formato esperado: {"phrase": "texto a ser traduzido"}
Returns:
    ChatResponseModel: Objeto JSON contendo a tradução gerada
        Formato retornado: {"assistant": "texto traduzido"}
Example:
    Request:
        POST /translate/gemini
        {
            "phrase": "Hello, how are you?"
        }
    Response:
        {
            "assistant": "Bonjour comment allez-vous?"
        }
Note:
    Este endpoint é monitorado para latência através do decorador @monitor_latency()
"""
    generated_text = chain.invoke({
        "input": phrase.phrase,
    })

    response = ChatModel(message=generated_text.content)

    return ChatResponseModel(assistant=response.message)
