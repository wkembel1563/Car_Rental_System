# Robert Kembel
# Amanda La
# Alberto Arriaga

from tkinter import *
from tkinter import ttk
import sqlite3

# TODO: format phone number input on tab1
# TODO: display query purpose info to user for each query
# TODO: for each query, print all rows involved and their quantity
# TODO: can add drop down menu's to select type/model/category etc.
# TODO: AFTER DONE. tweak justification of boxes to make it look better

################################
# CONSTS - to index grid position
# 	   arrays below
ROW = 0
COL = 1

####################
# MAIN WINDOW SETUP
root = Tk()
root.title('Car Rental Database')
root.geometry("600x300")

############
# TAB SETUP
# to add a new tab, create it with ttk.Frame and
# 	then use tab_parent.add() to add it to the window
# to put stuff in the tab, do the same thing we learned in class,
# 	just reference the name of your tab instead of 'root'
# 	when creating labels etc.
tab_parent = ttk.Notebook(root)   # Notebook method returns a parent tab
				  # all tabs you click on will be nested in this 'host' tab

# TAB 1
tab1 = ttk.Frame(tab_parent) 	  	  # initialize as subtabs as part of parent tab
tab_parent.add(tab1, text='Add Customer') # embed the tabs in the parent and give each a name

# TAB 2
tab2 = ttk.Frame(tab_parent)
tab_parent.add(tab2, text='Add Vehicle')

# TAB 3
tab3 = ttk.Frame(tab_parent)
tab_parent.add(tab3, text='Tab3')

tab_parent.pack(expand=1, fill='both')    # pack the parent to properly display the tabs


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


def insert_vehicle():
    insertdb = sqlite3.connect('cars.db')
    insertcursor = insertdb.cursor()
    insertcursor.execute("INSERT INTO VEHICLE VALUES(:VehicleID, :Description, :Year, :Type, :Category)",{
                            'VehicleID': vIdEntry.get(),
                            'Description': descEntry.get(),
			    'Year': yearEntry.get(),
			    'Type': typeEntry.get(),
			    'Category': catEntry.get()
    })

    insertdb.commit()

    # close db connection
    insertdb.close()



# GUI components for root window
####################################
# TAB1 GRID POSITIONS - ADD CUSTOMER
nameLabelPos  = [0,0] # row - col
nameEntryPos  = [0,1]
phoneLabelPos = [1,0]
phoneEntryPos = [1,1]
t1SubmitBtnPos  = [2,0,2,10,10,100] # row - col - columnspan - pady - padx - ipadx

# TAB1 labels/entries
CustID = Entry(tab1, width =30)
CustIDlabel = Label(tab1,text='CustID')
Name 		= Entry(tab1, width = 30)
Namelabel 	= Label(tab1, text='Name')
Phone 		= Entry(tab1, width = 30)
Phonelabel 	= Label(tab1, text = 'Phone')

CustID.grid(row = 3, column =1, padx=  20)
CustIDlabel.grid(row=3,column=0)
Name.grid(row = nameEntryPos[ROW], column = nameEntryPos[COL])
Namelabel.grid(row = nameLabelPos[ROW], column = nameLabelPos[COL])
Phone.grid(row = phoneEntryPos[ROW], column = phoneEntryPos[COL])
Phonelabel.grid(row = phoneLabelPos[ROW], column = phoneLabelPos[COL])

#submit
t1submitbutton = Button(tab1, text = 'Add Customer', command = insert_customer)
t1submitbutton.grid(row = t1SubmitBtnPos[0], column=t1SubmitBtnPos[1], columnspan = t1SubmitBtnPos[2], pady = t1SubmitBtnPos[3], padx = t1SubmitBtnPos[4], ipadx=t1SubmitBtnPos[5])

#TAB1 input query
def input_query():
    conn = sqlite3.connect('cars.db')
    c = conn.cursor()
    # TODO case - total amount showed when null / not
    c.execute("SELECT C.CustID, C.Name, R.TotalAmount,CASE WHEN R.PaymentDate != 'NULL' THEN '$0.00' END FROM CUSTOMER AS C JOIN RENTAL R ON R.CustID = C.CustID WHERE C.CustID=? OR C.Name = ?",(CustID.get(),Name.get(),) )
    records = c.fetchall()
    print(records)

input_query_button = Button(tab1, text = 'Search Customer', command = input_query)
input_query_button.grid(row = 4, column = 0 , columnspan = 2, pady=10, padx=10 , ipadx=100 )

#######################################
# TAB2 GRID POSITIONS - ADD NEW VEHICLE
vIdLabelPos  = [0,0]
vIdEntryPos  = [0,1]
descLabelPos = [1,0]
descEntryPos = [1,1]
yearLabelPos = [2,0]
yearEntryPos = [2,1]
typeLabelPos = [3,0]
typeEntryPos = [3,1]
catLabelPos  = [4,0]
catEntryPos  = [4,1]
t2SubmitBtnPos = [5,0,2,10,10,100] # row - col - columnspan - pady - padx - ipadx

# TAB2 labels/entries
vIdEntry  = Entry(tab2, justify=LEFT, width = 30)
vIdLabel  = Label(tab2, text = 'Vehicle ID: ')
descEntry = Entry(tab2, justify=LEFT, width = 50)
descLabel = Label(tab2, text = 'Description: ')
yearEntry = Entry(tab2, justify=LEFT, width = 4)
yearLabel = Label(tab2, text = 'Year: ')
typeEntry = Entry(tab2, justify=LEFT, width = 1)
typeLabel = Label(tab2, text = 'Type (1 - 6): ')
catEntry  = Entry(tab2, justify=LEFT, width = 1)
catLabel  = Label(tab2, text = 'Category (0 or 1): ')

vIdLabel.grid(row  = vIdLabelPos[ROW],  column = vIdLabelPos[COL])
vIdEntry.grid(row  = vIdEntryPos[ROW],  column = vIdEntryPos[COL], sticky = W)
descLabel.grid(row = descLabelPos[ROW], column = descLabelPos[COL])
descEntry.grid(row = descEntryPos[ROW], column = descEntryPos[COL], sticky = W)
yearLabel.grid(row = yearLabelPos[ROW], column = yearLabelPos[COL])
yearEntry.grid(row = yearEntryPos[ROW], column = yearEntryPos[COL], sticky = W)
typeLabel.grid(row = typeLabelPos[ROW], column = typeLabelPos[COL])
typeEntry.grid(row = typeEntryPos[ROW], column = typeEntryPos[COL], sticky = W)
catLabel.grid(row  = catLabelPos[ROW],  column = catLabelPos[COL])
catEntry.grid(row  = catEntryPos[ROW],  column = catEntryPos[COL], sticky = W)

#submit
t2submitbutton = Button(tab2, text = 'Add Vehicle', command = insert_vehicle)
t2submitbutton.grid(row = t2SubmitBtnPos[0], column=t2SubmitBtnPos[1], columnspan = t2SubmitBtnPos[2], pady = t2SubmitBtnPos[3], padx = t2SubmitBtnPos[4], ipadx=t2SubmitBtnPos[5])


root.mainloop()
