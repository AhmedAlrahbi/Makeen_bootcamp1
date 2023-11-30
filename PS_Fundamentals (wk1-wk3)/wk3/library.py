#ICA
class Library:
    def __init__(self):

        self.books = []

    def add_book(self,title, auth, copies):
        book = []
        book.append(title)
        book.append(auth)
        book.append(copies)

        self.books.append(book)


    def dis_books(self):
        # for i in self.books:
        #     print (i, end = " ")
        print(self.books)
    def searchBooks(self):
        search_prompt = input("Enter the book name: ")
        found = False
        for book in self.books:
            if search_prompt == book[0]:
                print("Book found - Title:", book[0], "Author:", book[1], "Copies:", book[2])
                found = True
                break

        if not found:
            print(search_prompt, "not found")


b = Library()
opt = int(input("How many books u want to add: "))
for i in range(opt):
    title = input("Enter the title: ")
    auth = input("Enter the Auther: ")
    copies = input("Enter the Copies: ")
    b.add_book(title, auth, copies)

b.dis_books()
b.searchBooks()
