from pydantic import BaseModel


class FakeLLMModel(BaseModel):
    phrase: str


class ChatResponseModel(BaseModel):
    assistant: str


class ChatModel(BaseModel):
    message: str
