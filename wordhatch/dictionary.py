from wordhatch.definition_provider import DefinitionProvider, DefinitionStore
from wordhatch.models import WordDefinition


def get_definition(
    word: str,
    def_provider: DefinitionProvider,
    def_store: DefinitionStore,
) -> WordDefinition:
    if not word or not word.strip():
        raise ValueError("Word cannot be empty string or white spaces.")
    word_definiton = def_store.get(word)
    if word_definiton is None:
        word_definiton = def_provider.get(word)
    return word_definiton
