from typing import Optional

import pytest

from wordhatch.definition_provider import DefinitionProvider, DefinitionStore
from wordhatch.dictionary import get_definition
from wordhatch.models import WordDefinition


class FakeDefinitionProvider(DefinitionProvider):
    def __init__(self, result: WordDefinition):
        self.result = result

    def get(self, word: str) -> WordDefinition:
        return self.result


class FakeDefinitionStore(DefinitionStore):
    def __init__(self, result: Optional[WordDefinition]):
        self.result = result

    def get(self, word: str) -> Optional[WordDefinition]:
        return self.result

    def set(self, definition: WordDefinition) -> None: ...


def test_get_definition_generates_new_when_not_cached() -> None:
    test_word = "cat"
    generated_definition = WordDefinition(
        word=test_word,
        definition="four-legged evil",
    )
    definition = get_definition(
        test_word,
        FakeDefinitionProvider(generated_definition),
        FakeDefinitionStore(None),
    )
    assert definition == generated_definition


def test_get_definition_returns_cached_when_available() -> None:
    test_word = "cat"
    generated_definition = WordDefinition(
        word=test_word,
        definition="four-legged evil",
    )

    cached_definition = WordDefinition(
        word=test_word,
        definition="cached four-legged evil",
    )

    definition = get_definition(
        test_word,
        FakeDefinitionProvider(generated_definition),
        FakeDefinitionStore(cached_definition),
    )
    assert definition == cached_definition


@pytest.mark.parametrize("test_word", ["", "   ", "\n"])
def test_get_definition_raise_error_with_empty_string_input(test_word: str) -> None:
    generated_definition = WordDefinition(word="", definition="")
    cached_definition = WordDefinition(word="", definition="")
    with pytest.raises(ValueError):
        get_definition(
            test_word,
            FakeDefinitionProvider(generated_definition),
            FakeDefinitionStore(cached_definition),
        )
