import pymongo
from tkinter import *
def u_student_function():
    root = Tk()
    root.title("Update Student")
    root.geometry("700x300")
    def updatestudent():
        client = pymongo.MongoClient("mongodb://localhost:27017")
        db = client.student_lib_DB
        collection = db.student
        try:
            criteria_s = e0.get()
            s_update_std_id = e1.get()
            s_update_name = e2.get()
            s_update_age = e3.get()
            s_update_country = e4.get()

            db.student.update_one(
                {"std_id": criteria_s},
                {
                    "$set": {
                        "std_id":s_update_std_id,
                        "name" :s_update_name,
                        "age":s_update_age,
                        "country":s_update_country
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
    l2= Label(root, text="Student Name")
    l3= Label(root, text="Student Age")
    l4= Label(root, text="Student Country")

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

    def changestudent():
        lm= Label(root, text="Enter the records to be updated:")
        lm.grid(row=2, column=2, sticky=N)
        b2= Button(root, text='Update', command=updatestudent)
        b2.grid(row=7, column=3, sticky=W, pady=4)

    b1= Button(root, text='Okay', command=changestudent)
    b1.grid(row=1, column=3, sticky=W, pady=4)
    
    root.mainloop()


