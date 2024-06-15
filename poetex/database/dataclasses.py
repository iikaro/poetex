from poetex.poetry.poem import PoetexBaseModel, Language


class PoemBibTexData(PoetexBaseModel):
    author: str
    title: str
    date: str
    book_title: str
    publisher: str
    year: str
    editor: str
    volume: str
    number: str
    series: str
    pages: str
    address: str
    edition: str
    month: str
    note: str
    key: str
    source: str
    url: str


class PoemMetaData(PoetexBaseModel):
    isbn_10: str
    isbn_13: str
    doi: str
    genres: list[str]
    language: Language


class PoemData(PoemBibTexData, PoemMetaData):
    ...
