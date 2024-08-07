from poetex.poetry.poem import TitleType, Verse, Stanza, Poem, Untitled, Title
from poetex.utils.constants import DOUBLE_LINE_SPACING, SINGLE_LINE_SPACING
from poetex.utils.utils import load_file_contents


def load_poem(file_path: str, title_type: TitleType = TitleType.FIRST_LINE) -> Poem:
    """
    Load poem from text file (.txt) and store it in a Poem object.

    :param file_path: Path to text file.
    :param title_type: Enum stating how the title of the poem will be extracted from the text file. Default is 'first_line', i.e., first line of the text file will be used as title and removed from the final Poem object.
    :return: Poem object.
    """
    contents = load_file_contents(file_path)
    stanzas = [Stanza(verses=[Verse(text=verse) for verse in _get_verses(stanza)]) for stanza in _get_stanzas(contents)]
    title = Untitled
    if title_type != TitleType.UNTITLED:
        title = Title(text=stanzas[0].verses[0].text, type=title_type)

    stanzas = stanzas[1:] if title_type.FIRST_LINE else stanzas

    return Poem(stanzas=stanzas, title=title)


def _get_stanzas(poem: str) -> list[str]:
    return poem.split(DOUBLE_LINE_SPACING)


def _get_verses(stanzas: str) -> list[str]:
    return stanzas.split(SINGLE_LINE_SPACING)
