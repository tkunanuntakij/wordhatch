from typing import Callable, Optional
from wordhatch.models import WordDefinition


def get_definition(
    word: str,
    definition_generator: Callable[[str], WordDefinition],
    cache_store: Callable[[str], Optional[WordDefinition]],
) -> WordDefinition:
    if not word or not word.strip():
        raise ValueError("Word cannot be empty string or white spaces.")
    word_definiton = cache_store(word)
    if word_definiton is None:
        word_definiton = definition_generator(word)
    return word_definiton
