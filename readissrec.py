import pymongo
from tkinter import *

def r_issrec_function():
    root = Tk()
    root.title("Read From ISS_REC")
    root.geometry("700x300")
    frame = Frame(root)
    frame.pack()
    text=Text(frame, height = 1920,width = 1080)
    text.pack()
    client = pymongo.MongoClient("mongodb://localhost:27017")
    db = client.student_lib_DB
    collection = db.issrec
    try:
        memCol = db.issrec.find({},{"_id": 0})
        i=1
        text.delete('1.0', END)
        text.insert(END,"\n All data in ISS_REC Collection \n")
        for iss in memCol:
            text.insert(END,'\n'+str(iss))
            i=i+1
    except Exception:
        text.insert(END,"\nERROR\n")
    
    root.mainloop()
