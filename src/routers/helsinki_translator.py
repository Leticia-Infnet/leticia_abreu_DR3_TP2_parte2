import torch
from fastapi import APIRouter

# Langchain imports
from langchain_huggingface import HuggingFacePipeline

# Transformers imports
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, pipeline

# Local imports
from models.helsinki_translator import HelsinkiTranslator, ChatModel, ChatResponseModel
from .utils.latency_monitor import monitor_latency

router = APIRouter()

DEVICE = 'cuda' if torch.cuda.is_available() else 'cpu'

model_id = 'Helsinki-NLP/opus-mt-en-de'

tokenizer = AutoTokenizer.from_pretrained(model_id)

model = AutoModelForSeq2SeqLM.from_pretrained(model_id)

pipe = pipeline(
    'translation',
    model=model,
    tokenizer=tokenizer,
    device=DEVICE,
    max_new_tokens=200
)

hf = HuggingFacePipeline(pipeline=pipe)


@router.post('/helsinki')
@monitor_latency()
async def helsinki_translator(phrase: HelsinkiTranslator) -> ChatResponseModel:
    """
Realiza a tradução de um texto em inglês para alemão.
Endpoint:
    /helsinki (POST)
Args:
    phrase (HelsinkiTranslator): Objeto contendo o texto a ser traduzido
        - phrase (str): Texto em inglês para tradução
Returns:
    ChatResponseModel: Objeto contendo a tradução do texto
        - assistant (str): Texto traduzido para alemão
Exemplo:
    Request:
        {
            "phrase": "Good morning"
        }
    Response:
        {
            "assistant": "Guten Morgen"
        }
"""
    generated_text = hf.invoke(phrase.phrase)

    response = ChatModel(message=generated_text)

    return ChatResponseModel(assistant=response.message)
