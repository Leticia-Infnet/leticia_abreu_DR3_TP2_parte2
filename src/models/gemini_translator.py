from pydantic import BaseModel


class GeminiTranslator(BaseModel):
    phrase: str


class ChatModel(BaseModel):
    message: str


class ChatResponseModel(BaseModel):
    assistant: str
