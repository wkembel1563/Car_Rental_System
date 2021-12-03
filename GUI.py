# Robert Kembel
# Amanda La
# Alberto Arriaga


from tkinter import *
import sqlite3

root = Tk()
root.title('Car Rental Database')
root.geometry("500x500")



# TODO - i just put the database name that i have now
#connct to DB
database = sqlite3.connect('cars')
print("Connected to DB")

#create cursor
cursor = database.cursor()


def insert_customer():

    insertdb = sqlite3.connect('cars')
    insertcursor = insertdb.cursor()
    insertcursor.execute("INSERT INTO CUSTOMER VALUES(:CustID, :Name, :Phone)",{
                            'CustID': CustID.get(),
                            'Name': Name.get(),
                            'Phone': Phone.get()
    })
    insertdb.commit()

#def insert_vehicle():




#GUI components for root window

CustID = Entry(root, width =30)
CustID.grid(row = 0, column =1, padx=  20)
CustIDlabel = Label(root,text='CustID')
CustIDlabel.grid(row=0,column=0)
Name = Entry(root, width = 30)
Name.grid(row=1, column = 1)
Namelabel = Label(root, text='Name')
Namelabel.grid(row=1,column=0)
Phone = Entry(root, width = 30)
Phone.grid(row=2, column=1)
Phonelabel = Label(root, text = 'Phone')
Phonelabel.grid(row=2,column=0)

root.mainloop()
