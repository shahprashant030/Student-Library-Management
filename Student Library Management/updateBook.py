import pymongo
from tkinter import *
def u_book_function():
    root = Tk()
    root.title("Update Book")
    root.geometry("700x300")
    def updatebook():
        client = pymongo.MongoClient("mongodb://localhost:27017")
        db = client.student_lib_DB
        collection = db.book
        try:
            criteria_b = e0.get()
            b_update_book_no = e1.get()
            b_update_book_name = e2.get()
            b_update_author = e3.get()
            
            db.book.update_one(
                {"book_no": criteria_b},
                {
                    "$set": {
                    "book_no":b_update_book_no,
                    "book_name" :b_update_book_name,
                    "author":b_update_author
                    }
                }
            )
            lx= Label(root, text="Records Updated Successfully")
            lx.grid(row=8, column=2, sticky=N)
        except Exception:
            lx= Label(root, text="ERROR")
            lx.grid(row=8, column=2, sticky=N)

    l0= Label(root, text="Enter book number to update")
    l1= Label(root, text="Book No")
    l2= Label(root, text="Book Name")
    l3= Label(root, text="Author")

    l0.grid(row=0, column=1, sticky=N)
    l1.grid(row=3, sticky=E)
    l2.grid(row=4, sticky=E)
    l3.grid(row=5, sticky=E)

    e0 = Entry(root)
    e1 = Entry(root)
    e2 = Entry(root)
    e3 = Entry(root)

    e0.grid(row=0, column=2)
    e1.grid(row=3, column=1)
    e2.grid(row=4, column=1)
    e3.grid(row=5, column=1)

    def changebook():
        lm= Label(root, text="Enter the records to be updated:")
        lm.grid(row=2, column=2, sticky=N)
        b2= Button(root, text='Update', command=updatebook)
        b2.grid(row=7, column=3, sticky=W, pady=4)

    b1= Button(root, text='Okay', command=changebook)
    b1.grid(row=1, column=3, sticky=W, pady=4)
    
    root.mainloop()


