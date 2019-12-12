import pymongo
from tkinter import *
def i_book_function():
    root = Tk()
    root.title("Insert Into Book")
    root.geometry("700x300")
    def insertbook():
        client = pymongo.MongoClient("mongodb://localhost:27017")
        db = client.student_lib_DB
        collection = db.book
        label = Label(root, text="\nInserted data successfully\n")
        label.grid(row=5,column=3)
        bookNo = e1.get()
        bookName = e2.get()
        bookAuthor = e3.get()
        db.book.insert_one(
            {
                "book_no": bookNo,
                "book_name":bookName,
                "author":bookAuthor,
        })
    
    
    l1= Label(root, text="Book No")
    l2= Label(root, text="Book Name")
    l3= Label(root, text="Author")

    l1.grid(row=0, sticky=E)
    l2.grid(row=1, sticky=E)
    l3.grid(row=2, sticky=E)

    e1 = Entry(root)
    e2 = Entry(root)
    e3 = Entry(root)

    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    e3.grid(row=2, column=1)

    b1= Button(root, text='Insert', command=insertbook)

    b1.grid(row=5, column=1, sticky=W, pady=4)

    root.mainloop()


