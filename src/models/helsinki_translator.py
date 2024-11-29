from pydantic import BaseModel


class HelsinkiTranslator(BaseModel):
    phrase: str


class ChatModel(BaseModel):
    message: str


class ChatResponseModel(BaseModel):
    assistant: str
