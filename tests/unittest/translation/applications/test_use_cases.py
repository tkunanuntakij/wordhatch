import pytest

from wordhatch.translation.application.ports import DefinitionProvider
from wordhatch.translation.application.use_cases import Translator
from wordhatch.translation.domain.values import Definition, Word


class FakeDefinitionProvider(DefinitionProvider):
    def __init__(self, result: Word):
        self.result = result

    async def translate(self, word: str, context: str) -> Word:
        return self.result


@pytest.mark.asyncio
async def test_translate() -> None:
    expected_result = Word(
        word="circuitous",
        definitions=[
            Definition(
                definition=(
                    "indirect, roundabout, or not taking the most straightforward path"
                )
            )
        ],
    )
    definition_provider = FakeDefinitionProvider(result=expected_result)
    translator = Translator(definition_provider=definition_provider)

    result = await translator.translate(
        word="circuitous",
        context=(
            "Taxi drivers now struggle to take people "
            "on circuitous but profitable routes, since "
            "apps such as Lyft and Uber tell them exactly"
            "where to go."
        ),
    )
    assert isinstance(result, Word)
