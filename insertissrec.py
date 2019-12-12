import pymongo
from tkinter import *
def i_issrec_function():
    root = Tk()
    root.title("Insert Into ISS_REC")
    root.geometry("700x300")
    def insertissrec():
        client = pymongo.MongoClient("mongodb://localhost:27017")
        db = client.student_lib_DB
        collection = db.issrec
        label = Label(root, text="\nInserted data successfully\n")
        label.grid(row=5,column=3)
        issId = e1.get()
        issDate = e2.get()
        membershipNo = e3.get()
        bookNo = e4.get()
        db.issrec.insert_one(
            {
                "iss_id": issId,
                "iss_date":issDate,
                "mem_no":membershipNo,
                "book_no":bookNo
        })
    
    
    l1= Label(root, text="ISS Id")
    l2= Label(root, text="ISS Date")
    l3= Label(root, text="Membership Number")
    l4= Label(root, text="Book Number")

    l1.grid(row=0, sticky=E)
    l2.grid(row=1, sticky=E)
    l3.grid(row=2, sticky=E)
    l4.grid(row=3, sticky=E)

    e1 = Entry(root)
    e2 = Entry(root)
    e3 = Entry(root)
    e4 = Entry(root)

    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    e3.grid(row=2, column=1)
    e4.grid(row=3, column=1)

    b1= Button(root, text='Insert', command=insertissrec)

    b1.grid(row=5, column=1, sticky=W, pady=4)

    root.mainloop()


