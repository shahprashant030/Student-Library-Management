import pymongo
from tkinter import *
def i_membership_function():
    root = Tk()
    root.title("Insert Into Membership")
    root.geometry("700x300")
    def insertmembership():
        client = pymongo.MongoClient("mongodb://localhost:27017")
        db = client.student_lib_DB
        collection = db.membership
        label = Label(root, text="\nInserted data successfully\n")
        label.grid(row=5,column=3)
        studentId = e1.get()
        membershipNo = e2.get()
        db.membership.insert_one(
            {
                "std_id":studentId,
                "mem_no":membershipNo                
        })

    
    
    l1= Label(root, text="Student Id")
    l2= Label(root, text="Membership No.")

    l1.grid(row=0, sticky=E)
    l2.grid(row=1, sticky=E)

    e1 = Entry(root)
    e2 = Entry(root)

    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)

    b1= Button(root, text='Insert', command=insertmembership)

    b1.grid(row=5, column=1, sticky=W, pady=4)

    root.mainloop()


