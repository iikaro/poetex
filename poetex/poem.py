from enum import Enum
from typing import Optional

from pydantic import BaseModel

from poetex.constants import DOUBLE_LINE_SPACING, SINGLE_LINE_SPACING

END_OF_VERSE = "\\\\"
END_OF_STANZA = "!"


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
    type: VerseType = VerseType.FREE
    syllables: Optional[int] = None

    def __str__(self) -> str:
        return self.text


class Stanza(PoetexBaseModel):
    verses: list[Verse]

    def __str__(self) -> str:
        return "\n".join([str(verse) for verse in self.verses])

    @property
    def lines(self) -> int:
        return len(self.verses)


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
    language: Language = Language.ENGLISH

    def __str__(self) -> str:
        return (
            str(self.title)
            + "\n\n"
            + "\n\n".join([str(stanza) for stanza in self.stanzas])
        )

    @property
    def lines(self) -> int:
        return self.stanzas[0].lines

    def to_latex_verse(self) -> str:
        begin = "\\begin{verse}" + SINGLE_LINE_SPACING
        end = "\\end{verse}"

        poem_latex = [begin]
        for stanza in self.stanzas:
            for verse in stanza.verses:
                poem_latex.append(verse.text + END_OF_VERSE + SINGLE_LINE_SPACING)
            poem_latex.append(END_OF_STANZA)
            poem_latex.append(DOUBLE_LINE_SPACING)
        poem_latex.append(end)
        return "".join(poem_latex)
