# Robert Kembel
# Amanda La
# Alberto Arriaga

from tkinter import *
from tkinter import ttk
# from tkcalendar import Calendar
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
root.geometry("650x400")
records = []

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
tab1 = ttk.Frame(tab_parent) 	  	  # initialize subtabs as part of parent tab
tab_parent.add(tab1, text='Add Customer') # embed tabs in parent and give each a name

# TAB 2
tab2 = ttk.Frame(tab_parent)
tab_parent.add(tab2, text='Add Vehicle')

# TAB 3
tab3 = ttk.Frame(tab_parent)
tab_parent.add(tab3, text='New Rental')

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


def check_for_vehicle():
    global freeVList
    global freeVEntry
    global freeVString
    global records
    insertdb = sqlite3.connect('cars.db')
    insertcursor = insertdb.cursor()

    # TODO: calculate quantity 
    # Get rental dates to check for free cars
    startD = sDateEntry.get()
    returnD = rDateEntry.get()

    # Query for cars free on those days 
    one   = "SELECT V.Description, V.Year, V.VehicleID, V.Type, V.Category " 
    two   = "FROM VEHICLE V WHERE V.VehicleID NOT IN (SELECT D.VehicleID FROM RENTAL D) OR V.VehicleID IN " 
    three = "(SELECT R.VehicleID FROM RENTAL R WHERE CASE WHEN R.StartDate <= ? THEN R.ReturnDate <= ? END "
    four  = "OR R.StartDate >= ?);" 
    fullquery = one + two + three + four 
    insertcursor.execute(fullquery, (startD, startD, returnD)) 

    # Update dropdown menu 
    records = insertcursor.fetchall()
    for record in records:
        freeVList.append(record[0])
    menu = freeVEntry["menu"] 
    menu.delete(0, "end") 
    for string in freeVList:
        menu.add_command(label=string, command=lambda value=string: freeVString.set(value)) 

    # close db connection
    insertdb.close()
    

def insert_rental(): 
    global records
    global car 
    insertdb = sqlite3.connect('cars.db')
    insertcursor = insertdb.cursor()

    # get vehicle id of selection 
    vid = ""
    car = freeVString.get()
    for record in records:
        if record[0] == car:
            vid = record[2]
            break
            
	
    # Insert rental record in db 
    insertString = "INSERT INTO RENTAL VALUES(:CustID, :VehicleID, :StartDate, :OrderDate, :RentalType, :Qty, :ReturnDate, :TotalAmount, :PaymentDate)"
    insertcursor.execute(insertString,{
                            'CustID'     : t3CustID.get(),
                            'VehicleID'  : vid, 
                            'StartDate'  : sDateEntry.get(),
        		    'OrderDate'  : oDateEntry.get(),
        		    'RentalType' : rentalTypeVar.get(),
        		    'Qty'        : 0, 
        		    'ReturnDate' : rDateEntry.get(), 
        		    'TotalAmount': amntDueEntry.get(), 
        		    'PaymentDate': pDateEntry.get() 
    })

    one = "UPDATE RENTAL SET Qty = CASE WHEN RentalType = 1 THEN "
    two = "(JULIANDAY(ReturnDate) - JULIANDAY(StartDate)) "
    three = "WHEN RentalType = 7 THEN (JULIANDAY(ReturnDate) - JULIANDAY(StartDate))/7 END;"
    update = one + two + three
    insertcursor.execute(update)

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
    x = CustID.get()
    y = Name.get()
    c.execute("SELECT C.CustID, C.Name, R.TotalAmount,CASE WHEN R.PaymentDate != 'NULL' THEN '$0.00'END FROM CUSTOMER AS C JOIN RENTAL R ON R.CustID = C.CustID WHERE (C.CustID=? or C.CustID IS NULL) OR (C.Name = ?) ",(x,y,) )
    if x =='' or y=='':
        c.execute("SELECT C.CustID, C.Name, R.TotalAmount,CASE WHEN R.PaymentDate != 'NULL' THEN '$0.00'END FROM CUSTOMER AS C JOIN RENTAL R ON R.CustID = C.CustID")
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

#######################################
# TAB3 GRID POSITIONS - ADD NEW RENTAL 
t3CustIDlabelPos  = [0,0] # customer id 
t3CustIDPos       = [0,1]  
oDateLabelPos  = [1,0]  # order date 
oDateEntryPos  = [1,1]
sDateLabelPos  = [2,0]  # start date 
sDateEntryPos  = [2,1]
rDateLabelPos  = [3,0]  # return date
rDateEntryPos  = [3,1]
t3CheckBtnPos = [4,0,2,10,10,100] # row - col - columnspan - pady - padx - ipadx
pDateLabelPos  = [5,0]  # payment date
pDateEntryPos  = [5,1]
rTypeLabelPos  = [6,0]  # rental type
rTypeDailyPos  = [6,1]
rTypeWeeklyPos = [7,1]
# qtyLabelPos    = [8,0]  # quantity 
# qtyEntryPos    = [8,1]
freeVLabelPos  = [8,0]	# display free vehicle choices 
freeVEntryPos  = [8,1]
amntDueLabelPos  = [9,0]  # total amount due
amntDueEntryPos  = [9,1]
t3SubmitBtnPos = [10,0,2,10,10,100] # row - col - columnspan - pady - padx - ipadx


# TAB3 labels/entriesj
rentalTypeVar = IntVar()  # tracks value of rental type radio button 

t3CustIDlabel = Label(tab3, text = 'Customer ID: ')
t3CustID      = Entry(tab3, justify=LEFT, width = 30)
oDateLabel    = Label(tab3, text = 'Order Date: ')
oDateEntry    = Entry(tab3, justify=LEFT, width = 9) 
sDateLabel    = Label(tab3, text = 'Start Date: ')
sDateEntry    = Entry(tab3, justify=LEFT, width = 9)
rDateLabel    = Label(tab3, text = 'Return Date: ')
rDateEntry    = Entry(tab3, justify=LEFT, width = 9)
pDateLabel    = Label(tab3, text = 'Payment Date: ')
pDateEntry    = Entry(tab3, justify=LEFT, width = 9) 
rTypeLabel    = Label(tab3, text = 'Rental Type: ')
rTypeDaily    = Radiobutton(tab3, justify=LEFT, text="Daily", padx = 10, variable=rentalTypeVar, value = 1)
rTypeWeekly   = Radiobutton(tab3, justify=LEFT, text="Weekly",padx = 10, variable=rentalTypeVar, value = 7)
# qtyLabel      = Label(tab3, text = 'Quantity (# Days or Weeks): ')
# qtyEntry      = Entry(tab3, justify=LEFT, width = 5)
freeVLabel    = Label(tab3, text = 'Free Vehicles: ')
freeVList     = ["NULL"] 
freeVString   = StringVar(root)
freeVString.set("")
freeVEntry    = OptionMenu(tab3, freeVString, *freeVList)
amntDueLabel  = Label(tab3, text = 'AmountDue: ')
amntDueEntry  = Entry(tab3, justify=LEFT, width = 10)

t3CustIDlabel.grid(row = t3CustIDlabelPos[ROW], column = t3CustIDlabelPos[COL], sticky = W)
t3CustID.grid(row    = t3CustIDPos[ROW],   column = t3CustIDPos[COL],   sticky = W)
oDateLabel.grid(row  = oDateLabelPos[ROW], column = oDateLabelPos[COL], sticky = W)
oDateEntry.grid(row  = oDateEntryPos[ROW], column = oDateEntryPos[COL], sticky = W)
sDateLabel.grid(row  = sDateLabelPos[ROW], column = sDateLabelPos[COL], sticky = W)
sDateEntry.grid(row  = sDateEntryPos[ROW], column = sDateEntryPos[COL], sticky = W)
rDateLabel.grid(row  = rDateLabelPos[ROW], column = rDateLabelPos[COL], sticky = W)
rDateEntry.grid(row  = rDateEntryPos[ROW], column = rDateEntryPos[COL], sticky = W)
pDateLabel.grid(row  = pDateLabelPos[ROW], column = pDateLabelPos[COL], sticky = W)
pDateEntry.grid(row  = pDateEntryPos[ROW], column = pDateEntryPos[COL], sticky = W)
rTypeLabel.grid(row  = rTypeLabelPos[ROW], column = rTypeLabelPos[COL], sticky = W)
rTypeDaily.grid(row  = rTypeDailyPos[ROW], column = rTypeDailyPos[COL], sticky = W)
rTypeWeekly.grid(row = rTypeWeeklyPos[ROW], column = rTypeWeeklyPos[COL], sticky = W)
# qtyLabel.grid(row    = qtyLabelPos[ROW],   column = qtyLabelPos[COL],   sticky = W)
# qtyEntry.grid(row    = qtyEntryPos[ROW],   column = qtyEntryPos[COL],   sticky = W)     
freeVLabel.grid(row  = freeVLabelPos[ROW], column = freeVLabelPos[COL], sticky = W)   
freeVEntry.grid(row  = freeVEntryPos[ROW], column = freeVEntryPos[COL], sticky = W)   
amntDueLabel.grid(row = amntDueLabelPos[ROW], column = amntDueLabelPos[COL], sticky = W) 
amntDueEntry.grid(row = amntDueEntryPos[ROW], column = amntDueEntryPos[COL], sticky = W) 

#submit
t3checkbutton = Button(tab3, text = 'Check for Free Vehicle', command = check_for_vehicle)
t3checkbutton.grid(row = t3CheckBtnPos[0], column=t3CheckBtnPos[1], columnspan = t3CheckBtnPos[2], pady = t3CheckBtnPos[3], padx = t3CheckBtnPos[4], ipadx=t3CheckBtnPos[5])
t3submitbutton = Button(tab3, text = 'Create Rental', command = insert_rental)
t3submitbutton.grid(row = t3SubmitBtnPos[0], column=t3SubmitBtnPos[1], columnspan = t3SubmitBtnPos[2], pady = t3SubmitBtnPos[3], padx = t3SubmitBtnPos[4], ipadx=t3SubmitBtnPos[5])

root.mainloop()
