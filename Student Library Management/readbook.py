import pymongo
from tkinter import *

def r_book_function():
    root = Tk()
    root.title("Read From Book")
    root.geometry("700x300")
    frame = Frame(root)
    frame.pack()
    text=Text(frame, height = 1920,width = 1080)
    text.pack()
    client = pymongo.MongoClient("mongodb://localhost:27017")
    db = client.student_lib_DB
    collection = db.book
    try:
        memCol = db.book.find({},{"_id": 0})
        i=1
        text.delete('1.0', END)
        text.insert(END,"\n All data in Book Collection \n")
        for bk in memCol:
            text.insert(END,'\n'+str(bk))
            i=i+1
    except Exception:
        text.insert(END,"\nERROR\n")
    
    root.mainloop()
