class Author:
    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        return list({contract.book for contract in self.contracts()})  # Remove duplicates

    def sign_contract(self, book, date, royalties):
        if not isinstance(book, Book):
            raise Exception("Must be a Book instance")
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts())

    def __repr__(self):
        return f"<Author name='{self.name}'>"


class Book:
    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        return list({contract.author for contract in self.contracts()})

    def __repr__(self):
        return f"<Book title='{self.title}'>"



class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        self.author = author if isinstance(author, Author) else self._raise_type_error()
        self.book = book if isinstance(book, Book) else self._raise_type_error()
        self.date = date if isinstance(date, str) else self._raise_type_error()
        self.royalties = royalties if isinstance(royalties, int) else self._raise_type_error()
        Contract.all.append(self)

    def _raise_type_error(self):
        raise Exception("Invalid argument type for Contract")

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]

    def __repr__(self):
        return f"<Contract {self.author.name} x {self.book.title} ({self.date}, {self.royalties}%)>"