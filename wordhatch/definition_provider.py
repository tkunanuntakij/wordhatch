from abc import ABC, abstractmethod
from typing import Optional

from wordhatch.models import WordDefinition


class DefinitionProvider(ABC):
    @abstractmethod
    def get(self, word: str) -> WordDefinition: ...


class DefinitionStore(ABC):
    @abstractmethod
    def get(self, word: str) -> Optional[WordDefinition]: ...

    @abstractmethod
    def set(self, definiton: WordDefinition) -> None: ...
