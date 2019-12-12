import pymongo
from tkinter import *
def d_student_function():
    root = Tk()
    root.title("Delete From Student")
    root.geometry("700x300")
    def deletestudent():
        client = pymongo.MongoClient("mongodb://localhost:27017")
        db = client.student_lib_DB
        collection = db.student
        try:
            d_criteria_s = e0.get()
            db.student.delete_many({"std_id":d_criteria_s})
            l1 = Label(root, text="\nDeletion Successful\n")
            l1.grid(row=3,column=1)
        except Exception:
            l2 = Label(root, text="\nERROR\n")
            l2.grid(row=3,column=1)
    
    l0= Label(root, text="Enter student id to delete")
    l0.grid(row=0, sticky=E)
    
    e0 = Entry(root)
    e0.grid(row=0, column=1)
    
    b1= Button(root, text='Delete', command=deletestudent)
    b1.grid(row=2, column=1, sticky=N, pady=4)

    root.mainloop()


