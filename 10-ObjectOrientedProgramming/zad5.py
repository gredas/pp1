class Book:
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages
    def open(self):
        print('The book is open')
    def close(self):
        print('The book is closed')
    def next_page(self):
        print('U swiped page')
class Telephone:
    def __init__(self,number,direction,time):
        self.number = number
        self.direction = direction
        self.time = time
    def call(self):
        print('start calling')
    def deny(self):
        print('denied calling')
    def check_number(self):
        print(f'the number is {self.number}')
class Students:
    def __init__(self,city,number,year):
        self.city = city
        self.number = number
        self.year = year
    def number(self):
        print(f'The number is {self.number}')
    
book = Book('raz','dwa',232)
print(book.title)
book.open()
book.close()
book.next_page()
telephone = Telephone(123,124,125)
telephone.check_number()