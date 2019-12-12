import pymongo
from tkinter import *
def d_iss_function():
    root = Tk()
    root.title("Delete From ISS_REC")
    root.geometry("700x300")
    def deleteiss():
        client = pymongo.MongoClient("mongodb://localhost:27017")
        db = client.student_lib_DB
        collection = db.issrec
        try:
            d_criteria_i = e0.get()
            db.issrec.delete_many({"iss_id":d_criteria_i})
            l1 = Label(root, text="\nDeletion Successful\n")
            l1.grid(row=3,column=1)
        except Exception:
            l2 = Label(root, text="\nERROR\n")
            l2.grid(row=3,column=1)
    
    l0= Label(root, text="Enter ISS ID to delete")
    l0.grid(row=0, sticky=E)
    
    e0 = Entry(root)
    e0.grid(row=0, column=1)
    
    b1= Button(root, text='Delete', command=deleteiss)
    b1.grid(row=2, column=1, sticky=N, pady=4)

    root.mainloop()


