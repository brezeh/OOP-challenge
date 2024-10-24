#assignment 3 breze howard

#creating class and attributes
class Book():
    def __init__(self, title, author, pages, genre):
        self.title = title
        self.author = author
        self.pages = pages
        self.read = False
        self.genre = genre
        self.purchasecount = 0

    def description(self):
        print("title:", self.title)
        print("author:", self.author)
        print("pages:", self.pages)
        print("genre", self.genre)
        print()

    def markasread(self):
        self.read = True
        print(f"You've marked '{self.title}' as read.")
    
    def __str__(self):
        return f"{self.title} - {self.author} - {self.pages} - {self.purchasecount} purchases"
    
#create two book objects
book1 = Book("Pride and Prejudice", "Jane Austen", 432, "Classic")
book2 = Book("Moby-Dick", "Herman Melville", 635, "Classic")

#printing descriptions
print(book1.description())
print(book2.description())

#mark first book as read
book1.markasread()

#part 2 - creating class and attributes to buy the books, view the purchased books, mark books as already read, display and filter by genre, and view the top 3 purchased books
class EbookReader():
    def __init__(self):
        self.availablebooks = [
            Book("Pride and Prejudice", "Jane Austen", 432, "Classic"),
            Book("Moby-Dick", "Herman Melville", 635, "Classic"),
            Book("The Adventures of Sherlock Holmes", "Arthur Conan Doyle", 307, "Mystery"),
            Book("Frankenstein", "Mary Shelley", 280, "Horror")
        ]
        self.purchasedbooks = []
        self.loadpurchases()

    def buybook(self, title):
        for book in self.availablebooks:
            if book.title.lower() == title.lower():
                book.purchasecount += 1
                self.purchasedbooks.append(book)
                print(f"You have purchased '{book.title}'.")
                self.savepurchases()
                return
        print("Book not found.")

    def viewpurchasedbooks(self):
        if not self.purchasedbooks:
            print("You have no purchased books.")
            return
        print("Your purchased books:")
        for book in self.purchasedbooks:
            print(book.description())

    def readbook(self, title):
        for book in self.purchasedbooks:
            if book.title.lower() == title.lower():
                if not book.read:
                    book.markasread()
                else:
                    print(f"You have already read '{book.title}'.")
                return
        print("Book not found in your purchases.")

    def displaygenre(self):
        genres = {book.genre for book in self.availablebooks}
        print("avalible genres: ")
        for genre in genres:
            print(genre)
    
    def filterbygenres(self, genre):
        print(f"books in the genre '{genre}':")
        found = False
        for book in self.availablebooks:
            if book.genre.lower() == genre.lower():
                found = True
                print(book.description())
        if not found:
            print("No books found in this genre.")

    def toppurchasedbooks(self):
        topbooks = sorted(self.availablebooks, key=lambda x: x.purchasecount, reverse=True)[:3]
        print("Top 3 purchased books: ")
        for book in topbooks:
            print(book)
        
    def searchbyauthor(self, author):
        found = False
        for book in self.availablebooks:
            if book.author.lower() == author.lower():
                print(book.description())
                found = True
        if not found:
            print("No books found by this author.")

    def searchbytitle(self, title):
        sortedbooks = sorted(self.availablebooks, key=lambda x: x.title.lower())
        low, high = 0, len(sortedbooks) - 1
        while low <= high:
            mid = (low + high) // 2
            if sortedbooks[mid].title.lower() == title.lower():
                print(sortedbooks[mid].description())
                return
            elif sortedbooks[mid].title.lower() < title.lower():
                low = mid + 1
            else:
                high = mid - 1
        print("Book not found.")

    def savepurchases(self):
        with open('purchasedbooks.txt', 'w') as file:
            for book in self.purchasedbooks:
                file.write(f"{book.title}\n")
    
    def loadpurchases(self):
        try:
            with open('purchasedbooks.txt', 'r') as file:
                titles = file.read().splitlines()
                for title in titles:
                    self.buybook(title)
        except FileNotFoundError:
            print("No previous purchases found.")

def main():
    reader = EbookReader()

    #display the avalable genre
    reader.displaygenre()

    #buying books
    reader.buybook("Pride and Prejudice")
    reader.buybook("Moby-Dick")
    reader.buybook("Pride and Prejudice")  #buying the same book again to test purchase count
    reader.buybook("Frankenstein")

    #view purchased books
    reader.viewpurchasedbooks()

    #reading a book
    reader.readbook("Pride and Prejudice")

    #reading the same book again
    reader.readbook("Pride and Prejudice")

    #display the top purchased books
    reader.toppurchasedbooks()

    #filtering by genre
    reader.filterbygenres("Classic")

    #searching by author
    reader.searchbyauthor("Jane Austen")

    #searching by title
    reader.searchbytitle("Moby-Dick")

#call the function
main()