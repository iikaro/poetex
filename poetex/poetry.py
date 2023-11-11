from poetex.poem import TitleType, Verse, Stanza, Poem, Untitled, Title

DOUBLE_LINE_SPACING = '\n\n'
SINGLE_LINE_SPACING = '\n'


def load_file_contents(file_path: str) -> str:
    with open(file_path, 'r', encoding="utf-8") as file:
        contents = file.read()
    return contents


def load_poem(file_path: str, title_type: TitleType = TitleType.FIRST_LINE) -> Poem:
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
