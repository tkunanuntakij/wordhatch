import pytest
from typing import Callable, Optional
from wordhatch.dictionary import get_definition
from wordhatch.models import WordDefinition


def get_fake_definition_generator(
    result: WordDefinition,
) -> Callable[[str], WordDefinition]:
    def fake_definition_generator(w: str) -> WordDefinition:
        return result

    return fake_definition_generator


def get_fake_cache_store(
    result: Optional[WordDefinition],
) -> Callable[[str], Optional[WordDefinition]]:
    def fake_cache_store(w: str) -> Optional[WordDefinition]:
        return result

    return fake_cache_store


def test_get_definition_generates_new_when_not_cached() -> None:
    test_word = "cat"
    generated_definition = WordDefinition(
        word=test_word,
        definition="four-legged evil",
    )
    definition = get_definition(
        test_word,
        get_fake_definition_generator(generated_definition),
        get_fake_cache_store(None),
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
        get_fake_definition_generator(generated_definition),
        get_fake_cache_store(cached_definition),
    )
    assert definition == cached_definition


@pytest.mark.parametrize('test_word', ['', '   ', '\n'])
def test_get_definition_raise_error_with_empty_string_input(test_word: str) -> None:
    generated_definition = WordDefinition(word="", definition="")
    cached_definition = WordDefinition(word="", definition="")
    with pytest.raises(ValueError):
        get_definition(
            test_word,
            get_fake_definition_generator(generated_definition),
            get_fake_cache_store(cached_definition),
        )
