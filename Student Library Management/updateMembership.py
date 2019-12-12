import pymongo
from tkinter import *
def u_membership_function():
    root = Tk()
    root.title("Update Membership")
    root.geometry("700x300")
    def updatemembership():
        client = pymongo.MongoClient("mongodb://localhost:27017")
        db = client.student_lib_DB
        collection = db.membership
        try:
            criteria_m = e0.get()
            m_update_std_id = e1.get()
            m_update_mem_no = e2.get()
            
            db.membership.update_one(
                {"std_id": criteria_m},
                {
                    "$set": {
                        "std_id":m_update_std_id,
                        "mem_no":m_update_mem_no,
                    }
                }
            )
            lx= Label(root, text="Records Updated Successfully")
            lx.grid(row=8, column=2, sticky=N)
        except Exception:
            lx= Label(root, text="ERROR")
            lx.grid(row=8, column=2, sticky=N)

    l0= Label(root, text="Enter student id to update")
    l1= Label(root, text="Student Id")
    l2= Label(root, text="Membership Number")
    
    l0.grid(row=0, column=1, sticky=N)
    l1.grid(row=3, sticky=E)
    l2.grid(row=4, sticky=E)
    
    e0 = Entry(root)
    e1 = Entry(root)
    e2 = Entry(root)
    
    e0.grid(row=0, column=2)
    e1.grid(row=3, column=1)
    e2.grid(row=4, column=1)
    
    def changemembership():
        lm= Label(root, text="Enter the records to be updated:")
        lm.grid(row=2, column=2, sticky=N)
        b2= Button(root, text='Update', command=updatemembership)
        b2.grid(row=7, column=3, sticky=W, pady=4)

    b1= Button(root, text='Okay', command=changemembership)
    b1.grid(row=1, column=3, sticky=W, pady=4)
    
    root.mainloop()


