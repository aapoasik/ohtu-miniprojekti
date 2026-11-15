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
        return f"{self.title}, {self.author}, {self.year}, {self.journal}"