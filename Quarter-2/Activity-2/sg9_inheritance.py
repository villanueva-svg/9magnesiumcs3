class Magazine:
    def __init__(self, title="", author="", issue_number=0):
        self.__title = title #Privated Attribute
        self.__author = author #Privated Attribute
        self.__issue_number = issue_number #Privated Attribute
        
    @property
    def get_issue_number(self): #Getter method for issue_number
        return self.__issue_number
    @get_issue_number.setter
    def set_issue_number(self, issue_number): #Setter method for issue_number
        if issue_number >= 0:
            self.__issue_number = issue_number
        else:
            print("Issue number must be a non-negative integer.")
    
class Book:
    def __init__(self, title="", author="", no_of_pages=0):
        self.__title = title #Privated Attribute
        self.__author = author #Privated Attribute
        self.__no_of_pages = no_of_pages #Privated Attribute

    @property
    def get_no_of_pages(self):
        return self.__no_of_pages

    @get_no_of_pages.setter
    def set_no_of_pages(self, no_of_pages):
        if no_of_pages >= 0:
            self.__no_of_pages = no_of_pages
        else:
            print("Number of pages must be a non-negative integer.")

class Publication:
    def __init__(self, title="", author=""):
        self.__title = title #Privated Attribute
        self.__author = author #Privated Attribute

    @property
    def get_title(self):
        return self.__title

    @get_title.setter
    def set_title(self, title):
        self.__title = title

    @property
    def get_author(self):
        return self.__author

    @get_author.setter
    def set_author(self, author):
        self.__author = author
        
    def display_info(self):
        print(f"Title: {self.__title}")
        print(f"Author: {self.__author}")
        
Mag1 = Magazine(title="Techt Today", author="John Smith", issue_number=5)
Mag1.display_info()

Mag2 = Magazine(title="Science Weekly", author="Lindsay Clancy", issue_number=12)
Mag2.display_info()

Book1 = Book(title="Python Programming", author="Bill Gates", no_of_pages=350)
Book1.display_info()

Book2 = Book(title="Data Science", author="Elon Musk", no_of_pages=500)
Book2.display_info()

Pub1 = Publication(title="The Great Gatsby", author="F. Scott Fitzgerald")
Pub1.display_info()

Pub2 = Publication(title="To Kill a Mockingbird", author="Harper Lee")
Pub2.display_info()