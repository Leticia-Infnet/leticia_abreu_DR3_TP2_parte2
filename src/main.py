import os
import uvicorn
from fastapi import FastAPI
from routers.fake_llm import router as FakeLLMRouter
from routers.gemini_translator import router as GeminiTranslator
from routers.helsinki_translator import router as HelsinkiTranslator

app = FastAPI()

app.include_router(router=FakeLLMRouter,
                   prefix='/fake',
                   tags=['fake'])

app.include_router(router=GeminiTranslator,
                   prefix='/translate',
                   tags=['translate'])

app.include_router(router=HelsinkiTranslator,
                   prefix='/translate',
                   tags=['translate'])


@app.post('/status')
def check_status():
    return {'message': 'O servirdor está rodando!'}


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000)
