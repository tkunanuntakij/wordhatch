import pytest

from wordhatch.translation.application.use_cases import Translator
from wordhatch.translation.domain.values import Word
from wordhatch.translation.externals.ollama_definition_provider import (
    OllamaDefinitionProvider,
)


@pytest.mark.integration
@pytest.mark.asyncio
async def test_ollama_translation() -> None:
    def_provider = OllamaDefinitionProvider()
    translator = Translator(definition_provider=def_provider)
    word = "circuitous"
    context = (
        "Taxi drivers now struggle to take people "
        "on circuitous but profitable routes, since "
        "apps such as Lyft and Uber tell them exactly"
        "where to go."
    )
    result = await translator.translate(word=word, context=context)
    assert isinstance(result, Word)
    assert result.word == word
    assert len(result.definitions) > 0
    assert isinstance(result.definitions[0].definition, str)
    assert len(result.definitions[0].definition) > 0
