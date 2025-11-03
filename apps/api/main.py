from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from apps.api.dto import TranslationRequestData
from wordhatch.translation.application.use_cases import Translator
from wordhatch.translation.domain.values import Word
from wordhatch.translation.externals.ollama_definition_provider import (
    OllamaDefinitionProvider,
)

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def hello_world() -> dict[str, str]:
    return {"msg": "Hello World"}


@app.post("/definitions")
async def translate(data: TranslationRequestData) -> Word:
    print(data)
    translator = Translator(definition_provider=OllamaDefinitionProvider())
    result = await translator.translate(**data.model_dump())
    return result
