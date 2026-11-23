class Article:
    def __init__(self, id, key, title, author, year,
                 journal, pages, volume, month, doi):
        self.id = id
        self.key = key
        self.title = title
        self.author = author
        self.year = year
        self.journal = journal
        self.pages = pages
        self.volume = volume
        self.month = month
        self.doi = doi

    def __str__(self):
        reference = f"{self.title}, {self.author}, {self.year}, {self.journal}"
        if self.pages:
            reference += f", pages: {self.pages}"
        if self.volume:
            reference += f", volume: {self.volume}"
        if self.month:
            reference += f", {self.month}"
        if self.doi:
            reference += f", doi: {self.doi}"
        return reference