class Library:
    def __init__(self , lsit,name):
        self.bookslist = lsit
        self.name = name
        self.lenDict  ={}

    def displayBooks(self):
        print(f"we have follosint books in the library {self.name}")
        for book in self.bookslist:
            print(book)


    def landBook(self , user , book):
        if book not in self.lenDict.keys():
            self.lenDict.update({book:user})
            print("Lender - books basedata has been updated . you can take book")
        else:
            print(f"book is already being used by {self.lenDict[book]}")

    def addBook(self,book):
        self.bookslist.append(book)
        print("book has been been added book list ")



    def returnBook(self,book):
        self.lenDict.pop(book)

if __name__ == '__main__':
    sachin = Library(["python" , "java" , "cpp" , "maths" , "algorithms"],"dhakad")

    while(True):
        print(f"Welcome to the {sachin.name} library . Enter your choice to continue")
        print("1. Display book")
        print("2. Land a  book")
        print("3. Add a book")
        print("4. Return a book")

        user_choice = input()
        if user_choice not in ['1','2','3','4']:
            print("please Enter a vaid option")
            continue
        else:
            user_choice = int(user_choice)
        if user_choice==1:
            sachin.displayBooks()
        elif user_choice==2:
            book = input("Enter the name of the book you want to land :- ")
            user = input("Enter your name ")
            sachin.landBook(user,book)
        elif user_choice == 3:
            book = input("Enter the name of the book you want to add :- ")
            sachin.addBook(book)

        elif user_choice == 4:
            book = input("Enter the name of the book you want to return book :- ")
            sachin.returnBook(book)

        else:
            print("not a valide option")


        print("Press q to quit and c to continue")
        user_choice2 = ""
        while(user_choice2!="c" and user_choice2!="q"):
            user_choice2 = input()
            if user_choice2== "q":
                exit()
            elif user_choice == "c":
                continue




