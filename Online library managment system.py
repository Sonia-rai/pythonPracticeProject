# Create a class- Library
# Attribute/Methods in class:
# Displaybook()- To display book
# Lendbook()-To Lend a book to user
# Addbook()-To add a book in library
# Returnbook()-To return the book in library
# Create a object and pass following parameter in constructor
# object_name= Library(list_of_book,library_name)
# After that create a mani function and run an infinite while loop
# which asks the users for their input -lend,display,add or return


class Library:
    def __init__(self, book_lists, library_name):
        self.book_lists = book_lists
        self.library_name = library_name
        self.lendDict = {}

    def Lendbook(self, user, book):

        self.user = user
        self.book = book
        if book not in self.lendDict.keys():
            self.lendDict.update({book: user})
            print(f"The book is successfully issued to {user} ")
            print({book.upper(): user})
        else:
            print(f"The book is been issued to {self.lendDict[book]}")

    def Displaybook(self):
        # to display the book
        print("The following books are available in the Library :")
        for book in self.book_lists:
            print(book)

    def Addbook(self, book):
        self.book_lists.append(book)
        print("Book added successfully")

    def Returnbook(self, book):
        self.lendDict.pop(book)


if __name__ == "__main__":
    lst=["WINGS OF FIRE", "GOOSEBUMPS","THE STORY OF LIFE ", "THREE MEN IN A BOAT",
         "RICH DADDY POOR DADDY"]
    SoniaLibrary = Library(lst, "LEARN & FUN")

    print("=" * 150)
    print(f"\t\t\t\t\t\t\t\t\t\t\t\t\t\tWELCOME TO {SoniaLibrary.library_name} DIGITAL LIBRARY ")
    print("=" * 150)

    while True:
        print("ENTER FOLLOWING CODE TO PERFORM TASK ")
        print("1-TO DISPLAY THE BOOK ")
        print("2-TO LEND THE BOOK ")
        print("3-TO ADD THE BOOK ")
        print("4-TO RETURN THE BOOK ")

        user_input = int(input())

        if user_input == 1:
            SoniaLibrary.Displaybook()

        elif user_input == 2:
            user = input("Enter your name:")
            book = input("Enter the name of book you wanna lend:")

            if book.upper() in lst:
                SoniaLibrary.Lendbook(user, book)
            else:
                print(f"{book} Not Available in Library,KINDLY ENTER ANOTHER BOOK")
        elif user_input == 3:
            book = input("Enter the name of book which you wanna donate:")
            SoniaLibrary.Addbook(book.upper())

        elif user_input == 4:
           book = input("Enter the name of book you wanna return:".capitalize())
           if book.upper() in lst:
              SoniaLibrary.Returnbook(book)
              print("The Book Returned successfully!!")
           else:
               print(f"{book} is Not Available in Library")
        else:
            print("Please,Enter valid keyword!!!")
            continue
        print("Press q to quit and c to continue")
        user_choice2 = ""

        while (user_choice2 != "c" and user_choice2 != "q"):
            user_choice2 = input()
            if user_choice2 == "q":
                exit()

            elif user_choice2 == "c":
                continue
