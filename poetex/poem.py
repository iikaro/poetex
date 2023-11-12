from enum import Enum
from typing import Optional

from pydantic import BaseModel


class TitleType(str, Enum):
    FIRST_LINE = "first_line"
    UNTITLED = "untitled"
    FIRST_VERSE = "first_verse"


class VerseType(str, Enum):
    FREE = "free"
    BLANK = "blank"
    RHYMED = "rhymed"


class Language(str, Enum):
    ENGLISH = "english"
    PORTUGUESE = "portuguese"


class PoetexBaseModel(BaseModel):
    ...


class Verse(PoetexBaseModel):
    text: str
    language: Language = Language.ENGLISH
    type: VerseType = VerseType.FREE
    syllables: Optional[int] = None

    def __str__(self) -> str:
        return self.text


class Stanza(PoetexBaseModel):
    verses: list[Verse]

    def __str__(self) -> str:
        return "\n".join([str(verse) for verse in self.verses])


class Title(PoetexBaseModel):
    text: str
    type: TitleType

    def __str__(self) -> str:
        return self.text


class Untitled(Title):
    text: str = "Untitled"
    type: TitleType = TitleType.UNTITLED


class Poem(PoetexBaseModel):
    stanzas: list[Stanza]
    title: Title = Untitled

    def __str__(self) -> str:
        return (
            str(self.title)
            + "\n\n"
            + "\n\n".join([str(stanza) for stanza in self.stanzas])
        )
