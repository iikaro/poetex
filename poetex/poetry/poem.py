from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field

from poetex.utils.constants import (
    DOUBLE_LINE_SPACING,
    SINGLE_LINE_SPACING,
    END_OF_VERSE,
    END_OF_STANZA,
)


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
    title: Title = Field(default_factory=Untitled)
    language: Language = Language.ENGLISH

    def __str__(self) -> str:
        return str(self.title) + "\n\n" + "\n\n".join([str(stanza) for stanza in self.stanzas])

    @property
    def lines(self) -> int:
        return self.stanzas[0].lines

    def __len__(self):
        return len(self.stanzas)

    def is_last_stanza(self, index: int) -> bool:
        if index == len(self) - 1:
            return True
        return False

    def is_last_verse(self, stanza_index, verse_index: int) -> bool:
        if verse_index == len(self.stanzas[stanza_index].verses) - 1:
            return True
        return False

    def to_latex_verse(self) -> str:
        begin = "\\begin{verse}" + SINGLE_LINE_SPACING
        end = "\\end{verse}"

        poem_latex = [begin]
        for stanza_index, stanza in enumerate(self.stanzas):
            for verse_index, verse in enumerate(stanza.verses):
                # Add verse
                poem_latex.append(verse.text)
                # Add double line spacing LaTeX command if the poem continues to the next stanza (\\)
                if not self.is_last_verse(stanza_index, verse_index):
                    poem_latex.append(END_OF_VERSE)
                # Add single line spacing to string (\n)
                poem_latex.append(SINGLE_LINE_SPACING)

            # Add LaTeX command to finish stanza (!)
            if not self.is_last_stanza(stanza_index):
                poem_latex.append(END_OF_STANZA)

            # Add double line spacing (\n\n)
            poem_latex.append(DOUBLE_LINE_SPACING)

        poem_latex.append(end)
        return "".join(poem_latex)
