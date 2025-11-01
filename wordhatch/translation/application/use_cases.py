from wordhatch.translation.application.ports import DefinitionProvider
from wordhatch.translation.domain.values import Word


class Translator:
    def __init__(self, definition_provider: DefinitionProvider):
        self._def = definition_provider

    async def translate(self, word: str, context: str) -> Word:
        result = await self._def.translate(word=word, context=context)
        return result
