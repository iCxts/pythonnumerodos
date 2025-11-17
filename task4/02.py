'''
You are tasked with designing a system for managing a library of books. The system should include the following classes:

    LibraryItem (Base Class): • This will be the base class for all items in the library (e.g., books, magazines).
    • It should have the following attributes:
    title: The title of the item.
    author: The author (or authors) of the item.
    publication_year: The year the item was published.
    • It should have a method get_item_info() that will display the information of the item

    Book (Subclass of LibraryItem):
    • This class represents a book in the library.
    • It should inherit from LibraryItem and add the following attribute:
    genre: The genre of the book (e.g., fiction, non-fiction).
    • Implement the get_item_info() method to display the book’s details, including the genre

    Magazine (Subclass of LibraryItem):
    • This class represents a magazine in the library.
    • It should inherit from LibraryItem and add the following attributes:
    issue_number: The issue number of the magazine.
    • Implement the get_item_info() method to display the magazine’s details, including the issue number.

Requirements:

    Write the class LibraryItem as an base class with the method get_item_info().
    Write the Book and Magazine subclasses to inherit from LibraryItem and override the get_item_info() method.
    Create objects of Book and Magazine, then call their get_item_info() method to display their details.

'''

class LibraryItem:
    def __init__(self, title: str, author: str, publication_year: int) -> None:
        self.title = str(title)
        self.author = str(author)
        self.publication_year = int(publication_year)
    
    def get_item_info(self) -> None:
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Year of Publication: {self.publication_year}")

class Book(LibraryItem):
    def __init__(self, title: str, author: str, publication_year: int, genre: str) -> None:
        super().__init__(title, author, publication_year)
        self.genre = str(genre)
 
    def get_item_info(self) -> None:
        super().get_item_info()
        print(f'Genre: {self.genre}')

class Magazine(LibraryItem):
    def __init__(self, title: str, author: str, publication_year: int, issue_number: int) -> None:
        super().__init__(title, author, publication_year)
        self.issue_number = int(issue_number)
        

    def get_item_info(self) -> None:
        super().get_item_info()
        print(f'Issue Number: {self.issue_number}')
