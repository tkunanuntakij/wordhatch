from langchain.chat_models import init_chat_model
from pydantic import BaseModel, Field

from wordhatch.translation.application.ports import DefinitionProvider
from wordhatch.translation.domain.values import Definition, Word


class OllamaDefinitionResponse(BaseModel):
    word: str = Field(description="The word of interest.")
    definition: str = Field(description="The definition of the word of interest.")


class OllamaDefinitionProvider(DefinitionProvider):
    def __init__(self, model: str = "ollama:llama3.2"):
        self._llm = init_chat_model(
            model=model,
            system_prompt="You are a helpful assistant that help provide definition to a requested word.",
            temperature=0,
        ).with_structured_output(OllamaDefinitionResponse)

    async def translate(self, word: str, context: str) -> Word:
        messages = [
            {"role": "user", "content": f"word: {word}\ncontext: {context}"},
        ]
        result = await self._llm.ainvoke(messages)
        if isinstance(result, BaseModel):
            result = OllamaDefinitionResponse.model_validate(result.model_dump())
            return Word(
                word=result.word, definitions=[Definition(definition=result.definition)]
            )
        return Word(word=word, definitions=[])
