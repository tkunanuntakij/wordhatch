from pydantic import BaseModel


class TranslationRequestData(BaseModel):
    word: str
    context: str
