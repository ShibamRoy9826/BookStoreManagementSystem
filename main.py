import sqlite3
from tabulate import tabulate

con = sqlite3.connect("data.db")
cur = con.cursor()
maxWidthPerCol=30 # for the column trim functionality

# Functions
def createTable():
    """
    Creates required tables, namely books and authors.
    We kept them in 2 different tables so that we can store multiple authors for the same book.
    """

    cur.execute("""
        create table if not exists
            books(
                book_id integer primary key autoincrement,
                title text,
                genre text,
                language text,
                price float,
                publish_year date,
                added_date date,
                stocks integer
            )
    """)

    cur.execute("""
    create table if not exists
        authors(
            book_id integer,
            name text,
            foreign key (book_id) references books(book_id)
        )
    """)


def addData():
    """
    Adds some data so that we can test these functions. NOT TO BE INCLUDED IN THE FINAL PROJECT,
    ONLY FOR TESTING PURPOSES
    And the prices are in USD, shouldn't be a problem though, cause its only for testing anyways
    """

    # the data is AI generated, so it could be wrong, but who cares
    """Insert 10 sample books with authors for testing."""
    sample_books = [
        # (title, genre, language, price, publish_year, added_date, stocks, [authors])
        ("To Kill a Mockingbird", "Fiction", "English", 12.99, "1960-07-11", "2025-11-01", 10, ["Harper Lee"]),
        ("1984", "Dystopian", "English", 10.50, "1949-06-08", "2025-11-01", 8, ["George Orwell"]),
        ("The Great Gatsby", "Classic", "English", 11.20, "1925-04-10", "2025-11-01", 6, ["F. Scott Fitzgerald"]),
        ("One Hundred Years of Solitude", "Magical Realism", "Spanish", 14.80, "1967-06-05", "2025-11-01", 5, ["Gabriel García Márquez"]),
        ("Pride and Prejudice", "Romance", "English", 8.50, "1813-01-28", "2025-11-01", 12, ["Jane Austen"]),
        ("The Hobbit", "Fantasy", "English", 13.75, "1937-09-21", "2025-11-01", 15, ["J.R.R. Tolkien"]),
        ("The Alchemist", "Adventure", "Portuguese", 10.00, "1988-04-15", "2025-11-01", 7, ["Paulo Coelho"]),
        ("The Da Vinci Code", "Thriller", "English", 16.20, "2003-03-18", "2025-11-01", 9, ["Dan Brown"]),
        ("The Book Thief", "Historical Fiction", "English", 12.50, "2005-03-14", "2025-11-01", 8, ["Markus Zusak"]),
        ("Good Omens", "Fantasy", "English", 13.99, "1990-05-01", "2025-11-01", 10, ["Neil Gaiman", "Terry Pratchett"]),
    ]

    for (title, genre, language, price, publish_year, added_date, stocks, authors) in sample_books:
        data = [title, genre, language, price, publish_year, added_date, stocks]
        addBook(data, authors)

    con.commit()

def printTable(data:list,cols=[],trimData=True):
    """
    if trimData is not set to False explicitly, it trims the column width so that everything is visible in the screen.
    This function basically just prints whatever data is passed to it, in the form of a table that we see in SQL.
    It uses the tabulate module to accomplish that.
    """
    newData=[]
    if(trimData):
        for row in data:
            newRow=[]
            for col in row:
                newRow.append(str(col)[:maxWidthPerCol])
            newData.append(newRow)
    else:
        newData=data

    if(len(cols)==0):
        for col in cur.description:
            cols.append(col[0])
    print(tabulate(newData,headers=cols,tablefmt="grid"))

def addBook(data:list,authors:list): 
    """
    This function adds a new book to the "books" table.
    It takes all the data for a new row as a list, and adds that to the "books" table.
    Additionally, it also takes an authors list, and for each author it creates a new entry in the "authors" table which use the book_id column of "books" as a foreign key.
    """
    cur.execute("""
        insert into books (title, genre, language, price, publish_year, added_date, stocks)
        values
        (?,?,?,?,?,?,?)
    """,data)

    bookId=cur.lastrowid

    for author in authors:
        cur.execute("""
            insert into authors (book_id, name)
            values 
            (?,?)
        """,(bookId,author))
    con.commit()

def deleteBook(bookId):
    """
    Deletes a particular book entry in the "books" table along with its respective "authors" entry
    """
    cur.execute("""
        delete from books
        where book_id=?
    """,(bookId,))
    cur.execute("""
        delete from authors
        where book_id=?
    """,(bookId,))

    con.commit()

def printAll(trimData=True):
    """
    Prints the entire table as a grid
    """
    output=cur.execute("select * from books")
    printTable(output,trimData=trimData)

def incrementStock(bookId):
    """
    Increments the stock of a particular book by 1
    """
    cur.execute("""
        update books 
        set stocks=stocks+1
        where book_id=?
    """,(bookId,))

def decrementStock(bookId):
    """
    Decrements the stock of a particular book by 1
    """
    cur.execute("""
        update books 
        set stocks=stocks-1
        where book_id=?
    """,(bookId,))

def setStock(bookId,value):
    """
    Sets the stock of a particular book to a certain value
    """
    cur.execute("""
        update books 
        set stocks=?
        where book_id=?
    """,(value,bookId))

def getAuthor(bookId):
    """
    Returns the author for a particular book
    """
    cur.execute("""
        select name from authors
        where book_id=?
    """,(bookId,))
    return cur.fetchall()



# Frontend
# To be updated


