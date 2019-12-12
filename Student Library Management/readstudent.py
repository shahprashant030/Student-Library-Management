import pymongo
from tkinter import *


def r_student_function():
    root = Tk()
    root.title("Read From Student")
    root.geometry("700x300")
    frame = Frame(root)
    frame.pack()
    text=Text(frame, height = 1920,width = 1080)
    text.pack()
    client = pymongo.MongoClient("mongodb://localhost:27017")
    db = client.student_lib_DB
    collection = db.student
    try:
        studCol = db.student.find({},{"_id": 0})
        i=1
        text.delete('1.0', END)
        text.insert(END,"\n All data in Student Collection \n")
        for stud in studCol:
            text.insert(END,'\n'+str(stud))
            i=i+1
    except Exception:
        text.insert(END,"\nERROR\n")
    
    root.mainloop()
