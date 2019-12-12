import pymongo
from tkinter import *
def d_book_function():
    root = Tk()
    root.title("Delete From Book")
    root.geometry("700x300")
    def deletebook():
        client = pymongo.MongoClient("mongodb://localhost:27017")
        db = client.student_lib_DB
        collection = db.book
        try:
            d_criteria_b = e0.get()
            db.book.delete_many({"book_no":d_criteria_b})
            l1 = Label(root, text="\nDeletion Successful\n")
            l1.grid(row=3,column=1)
        except Exception:
            l2 = Label(root, text="\nERROR\n")
            l2.grid(row=3,column=1)
    
    l0= Label(root, text="Enter book number to delete")
    l0.grid(row=0, sticky=E)
    
    e0 = Entry(root)
    e0.grid(row=0, column=1)
    
    b1= Button(root, text='Delete', command=deletebook)
    b1.grid(row=2, column=1, sticky=N, pady=4)

    root.mainloop()


