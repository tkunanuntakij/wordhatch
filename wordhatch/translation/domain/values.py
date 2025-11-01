from dataclasses import dataclass


@dataclass(frozen=True)
class Definition:
    definition: str


@dataclass(frozen=True)
class Word:
    word: str
    definitions: list[Definition]
