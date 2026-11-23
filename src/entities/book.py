class Book:
    def __init__(self, id, key, title, author, year, publisher, address):
        self.id = id
        self.key = key
        self.title = title
        self.author = author
        self.year = year
        self.publisher = publisher
        self.address = address

    def __str__(self):
        reference = f"{self.title}, {self.author}, {self.year}, {self.publisher}"
        if self.address:
            reference += f", {self.address}"
        return reference
