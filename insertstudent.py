import pymongo
from tkinter import *
def i_student_function():
    root = Tk()
    root.title("Insert Into Student")
    root.geometry("700x300")
    def insertstudent():
        client = pymongo.MongoClient("mongodb://localhost:27017")
        db = client.student_lib_DB
        collection = db.student
        label = Label(root, text="\nInserted data successfully\n")
        label.grid(row=5,column=3)
        studentId = e1.get()
        studentName = e2.get()
        studentAge = e3.get()
        studentCountry = e4.get()
        db.student.insert_one(
            {
                "std_id":studentId,
                "name":studentName,
                "age":studentAge,
                "country":studentCountry
        })
    
    
    l1= Label(root, text="Student Id")
    l2= Label(root, text="Student Name")
    l3= Label(root, text="Student Age")
    l4= Label(root, text="Student Country")

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

    b1= Button(root, text='Insert', command=insertstudent)

    b1.grid(row=5, column=1, sticky=W, pady=4)

    root.mainloop()


