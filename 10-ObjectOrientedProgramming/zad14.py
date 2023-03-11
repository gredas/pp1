class Book():
    def __init__(self,title,author,pages):
        self.open = False
        self.title = title
        self.author = author
        self.pages = pages
        self.current_page = 1
    def bopen(self):
        self.open = True
    def close(self):
        self.open = False
    def next_page(self):
        if self.open:
            if self.pages == self.current_page:
                print('no more pages')
            else:
                self.current_page += 1
        else:
            print('the book is closed')
    def previous_page(self):
        if self.open:
            if 1 == self.current_page:
                print('no more pages')
            else:
                self.current_page -= 1
        else:
            print('the book is closed')
    def status(self):
        print(f'{self.title}, {self.author}, {self.pages}, {self.current_page}')
book = Book('zmierch','ktos',10)
book.bopen()
book.status()
book.next_page()
book.next_page()
book.next_page()
book.next_page()
book.status()
book.close()
book.next_page()
