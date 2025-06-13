class Library:
    book_list=[]

    @classmethod
    def entry_book(cls, book):
        cls.book_list.append(book)

    @classmethod
    def borrow_book(cls):
        try:
            id=int(input("Enter the Book_ID to Borrow: "))
        except:
            print(f"Please Enter a Valid Book_ID")
            return

        for b in cls.book_list:
            if b.get_book_id() == id:
                b.borrow()
                return  
        print(f"There is no book with ID Number: {id}")
    
    @classmethod
    def return_book(cls):
        try:
            id=int(input("Enter the Book_ID to Return: "))
        except:
            print(f"Please Enter a Valid Book_ID")
            return

        for b in cls.book_list:
            if b.get_book_id() == id:
                b.return_b()
                return
            
        print(f"Sorry, There is no book with ID Number: {id}")

    @classmethod
    def view_all_info(cls):
        print(f"Full Book List:")
        
        for book in Library.book_list:
            print(
f"""Book_ID = {book.get_book_id()}; Title = {book.get_title()};    Author = {book.get_author()};  Availability = {'Yes' if book.get_avail() else 'No'}""")


class Book:
    def __init__(self, book_id, title, author, availability):
        self.__book_id=book_id
        self.__title=title
        self.__author=author
        self.__avail=availability
    
        Library.entry_book(self)

    def borrow(self):
        if self.__avail:
            self.__avail=False
            print(f"Borrowing request successful. Book Name: \"{self.__title}\"")
        else:
            print(f"Your requested book \"{self.__title}\" is not available for borrowing")
        
    def return_b(self):
        if self.__avail == False:
            self.__avail=True
            print(f"Returning request successful. Book Name: {self.__title}")
        else:
            print(f"Your returning book \"{self.__title}\" is not borrowed yet")
    
    def get_book_id(self):
        return self.__book_id
    def get_title(self):
        return self.__title
    def get_author(self):
        return self.__author
    def get_avail(self):
        return self.__avail

Book(101, "Atomic Habits", "James Clear", True)
Book(102, "Deep Work", "Cal Newport", True)
Book(103, "The Alchemist", "Paulo Coelho", True)
Book(104, "Think and Grow Rich", "Napoleon Hill", True)
Book(105, "The Power of Now", "Eckhart Tolle", True)
Book(106, "Rich Dad Poor Dad", "Robert T. Kiyosaki", True)
Book(107, "Can't Hurt Me", "David Goggins", True)

while(1):
    print(f"""
    +-----------------------------------------------------------+
    |                   Welcome To Library                      |        
    +-----------------------------------------------------------+
    | 1. View All Books                                         |
    | 2. Borrow Book                                            |
    | 3. Return Book                                            |
    | 4. Exit                                                   |
    +-----------------------------------------------------------+
    """)

    try:
        op= int(input("Choose Your Option: "))
        print("\n")

        if op==1:
            Library.view_all_info()
        elif op==2:
            Library.borrow_book()
        elif op==3:
            Library.return_book()
        elif op==4:
            break
        else:
            print(f"Invalid Option. Try Again Carefully.")        
    except ValueError:
        print(f"Choose Option Between 1 to 4")