from models.fake_llm import FakeLLMModel, ChatResponseModel, ChatModel
from fastapi import APIRouter
from langchain_community.llms.fake import FakeListLLM

router = APIRouter()


llm = FakeListLLM(responses=['Os mamíferos marsupiais possuem dois úteros',
                             'Papagaios e araras fazem parte da família dos psitacídeos',
                             'Dois mais dois é igual à quatro',
                             'Um minuto equivale à 60 segundos'],
                  verbose=True)


@router.post('/fakellm')
def fake_llm_response(phrase: FakeLLMModel) -> ChatResponseModel:
    generated_text = llm.invoke(phrase.phrase)

    response = ChatModel(message=generated_text)

    return ChatResponseModel(assistant=response.message)
