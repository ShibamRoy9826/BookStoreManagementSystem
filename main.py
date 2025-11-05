import sqlite3
from tabulate import tabulate

con = sqlite3.connect("data.db")
cur = con.cursor()
maxWidthPerCol=10

def createTable():
    cur.execute("""
        create table 
            books(
            book_id integer primary key,
            title text,
            genre text,
            language text,
            author_id integer,
            price float,
            publish_year date,
            added_date date,
            stocks integer,
            status text)
    """)

def addData():
    # the data is AI generated :
    cur.execute("""
    INSERT INTO books (book_id, title, genre, language, author_id, price, publish_year, added_date, stocks, status)
    VALUES
    (1, 'To Kill a Mockingbird', 'Fiction', 'English', 1, 12.99, '1960-07-11', '2025-11-01', 10, 'Available'),
    (2, '1984', 'Dystopian', 'English', 2, 10.50, '1949-06-08', '2025-11-01', 8, 'Available'),
    (3, 'The Great Gatsby', 'Classic', 'English', 3, 11.20, '1925-04-10', '2025-11-01', 6, 'Available'),
    (4, 'One Hundred Years of Solitude', 'Magical Realism', 'Spanish', 4, 14.80, '1967-06-05', '2025-11-01', 5, 'Available'),
    (5, 'The Catcher in the Rye', 'Classic', 'English', 5, 9.99, '1951-07-16', '2025-11-01', 4, 'Available'),
    (6, 'Pride and Prejudice', 'Romance', 'English', 6, 8.50, '1813-01-28', '2025-11-01', 12, 'Available'),
    (7, 'The Hobbit', 'Fantasy', 'English', 7, 13.75, '1937-09-21', '2025-11-01', 15, 'Available'),
    (8, 'The Alchemist', 'Adventure', 'Portuguese', 8, 10.00, '1988-04-15', '2025-11-01', 7, 'Available'),
    (9, 'Les Misérables', 'Historical Fiction', 'French', 9, 15.90, '1862-03-30', '2025-11-01', 3, 'Available'),
    (10, 'Crime and Punishment', 'Psychological Fiction', 'Russian', 10, 13.40, '1866-01-01', '2025-11-01', 5, 'Available'),
    (11, 'The Da Vinci Code', 'Thriller', 'English', 11, 16.20, '2003-03-18', '2025-11-01', 9, 'Available'),
    (12, 'The Kite Runner', 'Drama', 'English', 12, 11.80, '2003-05-29', '2025-11-01', 10, 'Available'),
    (13, 'Sapiens: A Brief History of Humankind', 'Non-Fiction', 'English', 13, 18.99, '2011-06-04', '2025-11-01', 6, 'Available'),
    (14, 'Inferno', 'Thriller', 'English', 11, 14.00, '2013-05-14', '2025-11-01', 7, 'Available'),
    (15, 'The Book Thief', 'Historical Fiction', 'English', 14, 12.50, '2005-03-14', '2025-11-01', 8, 'Available'),
    (16, 'The Little Prince', 'Children', 'French', 15, 7.80, '1943-04-06', '2025-11-01', 10, 'Available'),
    (17, 'A Game of Thrones', 'Fantasy', 'English', 16, 15.00, '1996-08-06', '2025-11-01', 5, 'Available'),
    (18, 'The Subtle Art of Not Giving a F*ck', 'Self-help', 'English', 17, 12.00, '2016-09-13', '2025-11-01', 10, 'Available'),
    (19, 'Thinking, Fast and Slow', 'Psychology', 'English', 18, 14.99, '2011-10-25', '2025-11-01', 8, 'Available'),
    (20, 'Norwegian Wood', 'Romance', 'Japanese', 19, 13.50, '1987-09-04', '2025-11-01', 6, 'Available');
                """)
    con.commit()

def printTable(data:list,cols=[],trimData=True):
    newData=[]
    if(trimData):
        for row in data:
            newRow=[]
            for col in row:
                newRow.append(str(col)[:maxWidthPerCol])
            newData.append(newRow)
    # print(newData)

    if(len(cols)==0):
        for col in cur.description:
            cols.append(col[0])
    # print(cols)
    print(tabulate(newData,headers=cols,tablefmt="grid"))

def addRow(tableName,data:list): # here "data" is supposed to be a list of tuples
    dataPart=""
    for d in data:
        dataPart+=str(d)+"\n"
    con.execute(f"""
        insert into {tableName} values
        {dataPart}
    """)
    con.commit()

def printAll():
    output=cur.execute("select * from books")
    printTable(output)


# addRow("books",[(21,"The Jungle Book","Adventure","English",20,15,"19-08-1997","05-11-25",3,"Available")])

printAll()

