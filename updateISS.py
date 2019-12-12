import pymongo
from tkinter import *
def u_issrec_function():
    root = Tk()
    root.title("Update ISS_REC")
    root.geometry("700x300")
    def updateissrec():
        client = pymongo.MongoClient("mongodb://localhost:27017")
        db = client.student_lib_DB
        collection = db.issrec
        try:
            criteria_i = e0.get()
            i_update_iss_id = e1.get()
            i_update_iss_date = e2.get()
            i_update_mem_no = e3.get()
            i_update_book_no = e4.get()

            db.issrec.update_one(
                {"iss_id": criteria_i},
                {
                    "$set": {
                        "iss_id": i_update_iss_id,
                        "iss_date":i_update_iss_date,
                        "mem_no":i_update_mem_no,
                        "book_no":i_update_book_no
                    }
                }
            )
            lx= Label(root, text="Records Updated Successfully")
            lx.grid(row=8, column=2, sticky=N)
        except Exception:
            lx= Label(root, text="ERROR")
            lx.grid(row=8, column=2, sticky=N)

    l0= Label(root, text="Enter ISS id to update")
    l1= Label(root, text="ISS ID")
    l2= Label(root, text="ISS Date")
    l3= Label(root, text="Membership Number")
    l4= Label(root, text="Book Number")

    l0.grid(row=0, column=1, sticky=N)
    l1.grid(row=3, sticky=E)
    l2.grid(row=4, sticky=E)
    l3.grid(row=5, sticky=E)
    l4.grid(row=6, sticky=E)

    e0 = Entry(root)
    e1 = Entry(root)
    e2 = Entry(root)
    e3 = Entry(root)
    e4 = Entry(root)

    e0.grid(row=0, column=2)
    e1.grid(row=3, column=1)
    e2.grid(row=4, column=1)
    e3.grid(row=5, column=1)
    e4.grid(row=6, column=1)

    def changeissrec():
        lm= Label(root, text="Enter the records to be updated:")
        lm.grid(row=2, column=2, sticky=N)
        b2= Button(root, text='Update', command=updateissrec)
        b2.grid(row=7, column=3, sticky=W, pady=4)

    b1= Button(root, text='Okay', command=changeissrec)
    b1.grid(row=1, column=3, sticky=W, pady=4)
    
    root.mainloop()


