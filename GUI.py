# Robert Kembel
# Amanda La
# Alberto Arriaga

from tkinter import *
from tkinter import ttk
import sqlite3

####################
# MAIN WINDOW SETUP
root = Tk()
root.title('Car Rental Database')
root.geometry("500x500")

############
# TAB SETUP
# to add a new tab, create it with ttk.Frame and
# 	then use tab_parent.add() to add it to the window 
# to put stuff in the tab, do the same thing we learned in class,
# 	just reference the name of your tab instead of 'root'
# 	when creating labels etc. 
tab_parent = ttk.Notebook(root)   # Notebook method returns a parent tab 
				  # all tabs you click on will be nested in this 'host' tab

tab1 = ttk.Frame(tab_parent) 	  # initialize as subtabs as part of parent tab 
tab2 = ttk.Frame(tab_parent) 
tab3 = ttk.Frame(tab_parent)  	  

tab_parent.add(tab1, text='Tab1') # embed the tabs in the parent and give each a name 
tab_parent.add(tab2, text='Tab2')
tab_parent.add(tab3, text='Tab3')

tab_parent.pack(expand=1, fill='both') # pack the parent to properly display the tabs


# TODO - i just put the database name that i have now
#connct to DB

database = sqlite3.connect('cars.db')
print("Connected to DB")

#create cursor
cursor = database.cursor()

# TODO not working for NULL CustID
def insert_customer():

    insertdb = sqlite3.connect('cars.db')
    insertcursor = insertdb.cursor()
    insertcursor.execute("INSERT INTO CUSTOMER VALUES(:CustID, :Name, :Phone)",{
                            'CustID': CustID.get(),
                            'Name': Name.get(),
                            'Phone': Phone.get()
    })
    insertdb.commit()

#def insert_vehicle():




#GUI components for root window

CustID = Entry(tab1, width =30)
CustID.grid(row = 0, column =1, padx=  20)
CustIDlabel = Label(tab1,text='CustID')
CustIDlabel.grid(row=0,column=0)
Name = Entry(tab1, width = 30)
Name.grid(row=1, column = 1)
Namelabel = Label(tab1, text='Name')
Namelabel.grid(row=1,column=0)
Phone = Entry(tab1, width = 30)
Phone.grid(row=2, column=1)
Phonelabel = Label(tab1, text = 'Phone')
Phonelabel.grid(row=2,column=0)

#submit
submitbutton = Button(tab1, text = 'Add Customer', command = insert_customer)
submitbutton.grid(row = 3, column=0, columnspan = 2, pady = 10, padx = 10, ipadx=100)

root.mainloop()
