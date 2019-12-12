import pymongo
from tkinter import *

from insertstudent import *
from insertmembership import *
from insertbook import *
from insertissrec import *

from readstudent import *
from readmembership import *
from readbook import *
from readissrec import *


from updateStudent import *
from updateMembership import *
from updateBook import *
from updateISS import *

from deletestudent import *
from deletemembership import *
from deletebook import *
from deleteiss import *

root = Tk()
# Title of the window
root.title("MongoDB Project")
root.geometry("900x300")

Top = Frame(root, width=900, height=50, bd=8, relief="raise")
Top.pack(side=TOP)

txt_title = Label(Top, width=900, font=('times new roman', 24), text = "Student Library Management System")
txt_title.pack()

def createDB():
    client = pymongo.MongoClient("mongodb://localhost:27017")

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def insertstudent():
    i_student_function()

def insertmembership():
    i_membership_function()

def insertbook():
    i_book_function()

def insertissrec():
    i_issrec_function()

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def Readstudent():
    r_student_function()

def Readmembership():
    r_membership_function()

def Readbook():
    r_book_function()

def Readissrec():
    r_issrec_function()

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def updateStudent():
    u_student_function()

def updateMembership():
    u_membership_function()
    
def updateBook():
    u_book_function()

def updateISS():
    u_issrec_function()

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def deletestudent():
    d_student_function()

def deletemembership():
    d_membership_function()

def deletebook():
    d_book_function()

def deleteiss():
    d_iss_function()

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

bconnection = Button(root, text = "Connect to database", command = createDB)
bconnection.pack()
#--------------------------------------------------------------------------
bs_insert = Button(root, text = "Insert Student", command = insertstudent)
bs_insert.place(x = 100,y = 100)

bs_read = Button(root, text = "Read Student", command = Readstudent)
bs_read.place(x = 300,y = 100)

bs_update = Button(root, text = "Update Student", command = updateStudent)
bs_update.place(x = 500,y = 100)

bs_delete = Button(root, text = "Delete from Student", command = deletestudent)
bs_delete.place(x = 700,y = 100)
#--------------------------------------------------------------------------
bm_insert = Button(root, text = "Insert Membership", command = insertmembership)
bm_insert.place(x = 100,y = 150)

bm_read = Button(root, text = "Read Membership", command = Readmembership)
bm_read.place(x = 300,y = 150)

bm_update = Button(root, text = "Update Membership", command = updateMembership)
bm_update.place(x = 500,y = 150)

bm_delete = Button(root, text = "Delete from Membership", command = deletemembership)
bm_delete.place(x = 700,y = 150)
#--------------------------------------------------------------------------
bb_insert = Button(root, text = "Insert Book", command = insertbook)
bb_insert.place(x = 100,y = 200)

bb_read = Button(root, text = "Read Book", command = Readbook)
bb_read.place(x = 300,y = 200)

bb_update = Button(root, text = "Update Book", command = updateBook)
bb_update.place(x = 500,y = 200)

bb_delete = Button(root, text = "Delete from Book", command = deletebook)
bb_delete.place(x = 700,y = 200)
#--------------------------------------------------------------------------
bi_insert = Button(root, text = "Insert ISS_REC", command = insertissrec)
bi_insert.place(x = 100,y = 250)

bi_read = Button(root, text = "Read ISS_REC", command = Readissrec)
bi_read.place(x = 300,y = 250)

bi_update = Button(root, text = "Update ISS_REC", command = updateISS)
bi_update.place(x = 500,y = 250)

bi_delete = Button(root, text = "Delete from ISS_REC", command = deleteiss)
bi_delete.place(x = 700,y = 250)
#--------------------------------------------------------------------------

root.mainloop()
