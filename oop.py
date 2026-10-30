# oop = Object Oriented Programming

# properties + functions
# class # template

# book title, author, isbn, price
class Book:
    # Constructor == function
    def __init__(self, title, author, isbn, price):
         self.title = title
         self.author = author
         self.isbn = isbn
         self.price = price
    def print_details(self):
        print("Title",self.title)
        print("Author",self.author)
        print("Price",self.price)
        print("________________")


    def appy_discount(self, discount):
        self.price = self.price * (1 - discount / 100)
        print("New Price is", self.price)


b1 = Book("Two rivers", "Chinua Acheni", "ISB001", 400)
b2 = Book("Big Minds", "James lee", "ISB002", 500)

b1.print_details()
b1.appy_discount(10)
b1.print_details()







