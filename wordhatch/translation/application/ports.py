from typing import Protocol

from wordhatch.translation.domain.values import Word


class DefinitionProvider(Protocol):
    async def translate(self, word: str, context: str) -> Word: ...
