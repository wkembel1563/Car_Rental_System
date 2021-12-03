# Robert Kembel
# Amanda La
# Alberto Arriaga

from tkinter import *
from tkinter import ttk
import sqlite3

# TODO: format phone number input on tab1 
# TODO: display query purpose info to user for each query 
# TODO: for each query, print all rows involved and their quantity

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

################################
# CONSTS - to index arrays below
ROW = 0
COL = 1

####################################
# TAB1 GRID POSITIONS - ADD CUSTOMER 
nameLabelPos = [0,0] # row - col
nameEntryPos = [0,1]
phoneLabelPos = [1,0]
phoneEntryPos = [1,1]
submitBtnPos = [2,0,2,10,10,100] # row - col - columnspan - pady - padx - ipadx

####################################
# TAB2 GRID POSITIONS - ADD NEW VEHICLE

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
    insertcursor.execute("INSERT INTO CUSTOMER(Name, Phone) VALUES(:Name, :Phone)",{
                            #'CustID': CustID.get(),
                            'Name': Name.get(),
                            'Phone': Phone.get()
    })

    insertdb.commit()

    # close db connection 
    insertdb.close() 
	

#def insert_vehicle():




#GUI components for root window

# CustID = Entry(tab1, width =30)
# CustID.grid(row = 0, column =1, padx=  20)
# CustIDlabel = Label(tab1,text='CustID')
# CustIDlabel.grid(row=0,column=0)
Name 		= Entry(tab1, width = 30)
Namelabel 	= Label(tab1, text='Name')
Phone 		= Entry(tab1, width = 30)
Phonelabel 	= Label(tab1, text = 'Phone')
Name.grid(row = nameEntryPos[ROW], column = nameEntryPos[COL])
Namelabel.grid(row = nameLabelPos[ROW], column = nameLabelPos[COL]) 
Phone.grid(row = phoneEntryPos[ROW], column = phoneEntryPos[COL])
Phonelabel.grid(row = phoneLabelPos[ROW], column = phoneLabelPos[COL])

#submit
submitbutton = Button(tab1, text = 'Add Customer', command = insert_customer)
submitbutton.grid(row = submitBtnPos[0], column=submitBtnPos[1], columnspan = submitBtnPos[2], pady = submitBtnPos[3], padx = submitBtnPos[4], ipadx=submitBtnPos[5])

root.mainloop()
