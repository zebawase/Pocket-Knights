# import library
from tkinter import *
from tkinter import ttk
import sqlite3  as db

from tkcalendar import DateEntry
import numpy as np
import matplotlib.pyplot as plt


# intial function for database config
def init():
    # connection object
    connectionObjn = db.connect("expenseTracker.db")
    # create cursor()
    curr = connectionObjn.cursor()
    # sql query....for create table into database
    query = '''
    create table if not exists expenses (
        date string,
        name string,
        Quantity string,
        expense number
        )
    '''
    # execute query...
    curr.execute(query)
    connectionObjn.commit()


# submit data................
def submitexpense():
    # get values from gui components
    values = [dateEntry.get(), Name.get(), Quantity.get(), Expense.get()]
    print(values)
    Etable.insert('', 'end', values=values)

    # get connection object
    connectionObjn = db.connect("expenseTracker.db")
    curr = connectionObjn.cursor()

    # sql query for insert data into database
    query = '''
    INSERT INTO expenses VALUES 
    (?, ?, ?, ?)
    '''

    # execute sql query through cursor
    curr.execute(query, (dateEntry.get(), Name.get(), Quantity.get(), Expense.get()))
    connectionObjn.commit()


# function for view data
def viewexpense():
    connectionObjn = db.connect("expenseTracker.db")
    curr = connectionObjn.cursor()

    # sql query for get data from database
    query = '''
     select * from expenses
    '''
    total = '''
    select sum(expense) from expenses
    '''

    # execute query..................
    curr.execute(query)
    rows = curr.fetchall()
    curr.execute(total)
    amount = curr.fetchall()[0]
    print(rows)
    print(amount)

    # set data into GUI grid
    l = Label(right, text="Date\t  Name\t  Quantity\t  Expense", font=('arial', 15, 'bold'), bg="pale green", fg="black")
    l.grid(row=0, column=6, padx=7, pady=7)

    st = ""
    for i in rows:
        for j in i:
            st += str(j) + '\t'
        st += '\n'
    print(st)
    l = Label(right, text=st, font=('arial', 12))
    l.grid(row=2, column=6, padx=7, pady=7)


init()  # call init..funtion.........

# window form GUI .............

root = Tk()
root.title(" Expense tracker")
root.config(bg="black")
root.geometry()
# root.attributes('-fullscreen', True)
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))

# -----------------------------------------
# make two FRame(GUI container)....left and right
left = Frame(root, bg='snow3', width=w / 2, height=h, )
right = Frame(root, bg='white', width=w / 2, height=h, padx=0, pady=0)
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

left.grid(row=0, column=0, sticky="e")
right.grid(row=1, column=0, sticky="w")
# ----------------------------------------

#  GUI :Graphic USER INterface
# define  LABEL /input box / button
dateLabel = Label(left, text="Date", font=('arial', 15, 'bold'), bg="snow3", fg="black", width=12)
dateLabel.grid(row=0, column=0, padx=7, pady=7)

dateEntry = DateEntry(left, width=12, font=('arial', 15, 'bold'))
dateEntry.grid(row=0, column=1, padx=7, pady=7)

Name = StringVar()
nameLabel = Label(left, text="Name", font=('arial', 15, 'bold'), bg="snow3", fg="black", width=12)
nameLabel.grid(row=1, column=0, padx=7, pady=7)

NameEntry = Entry(left, textvariable=Name, font=('arial', 15, 'bold'))
NameEntry.grid(row=1, column=1, padx=7, pady=7)

Quantity = StringVar()
titleLabel = Label(left, text="Quantity", font=('arial', 15, 'bold'), bg="snow3", fg="black", width=12)
titleLabel.grid(row=2, column=0, padx=7, pady=7)


titleEntry = Entry(left, textvariable=Quantity, font=('arial', 15, 'bold'))
titleEntry.grid(row=2, column=1, padx=7, pady=7)

Expense = IntVar()
expenseLabel = Label(left, text="Expense", font=('arial', 15, 'bold'), bg="snow3", fg="black", width=12)
expenseLabel.grid(row=3, column=0, padx=7, pady=7)

expenseEntry = Entry(left, textvariable=Expense, font=('arial', 15, 'bold'))
expenseEntry.grid(row=3, column=1, padx=7, pady=7)

submitbtn = Button(left, command=submitexpense, text="Submit", font=('arial', 15, 'bold'), bg="black", fg="white",
                   width=12)
submitbtn.grid(row=4, column=0, padx=13, pady=13)

viewtn = Button(right, command=viewexpense, text="View expenses", font=('arial', 15, 'bold'), bg="pale green",
                fg="black", width=12)
viewtn.grid(row=0, column=0, padx=1, pady=1)

# all saved expenses--------------
Elist = ['Date', 'Name', 'Quantity', 'Expense']
Etable = ttk.Treeview(left, column=Elist, show='headings', height=7)
for c in Elist:
    Etable.heading(c, text=c.title())
Etable.grid(row=5, column=0, padx=7, pady=7, columnspan=3)


def graph():
    #Graph
    # x-coordinates of left sides of bars
    left = [1, 2, 3, 4]
    # heights of bars
    height = [2400, 1500, 3600, 900]
    # labels for bars
    tick_label = ['1st', '2nd', '3rd', '4th']

    # plotting a bar chart
    plt.bar(left, height, tick_label=tick_label,width=0.8, color=['blue'])

    # naming the x-axis
    plt.xlabel('TIME')
    # naming the y-axis
    plt.ylabel('Expenditure')
    # plot title
    plt.title('Monthly Expenses')
    # function to show the plot
    plt.show()

graphbtn = Button(right,command=graph, text="View Graph", font=('arial', 15, 'bold'), bg="pale green",
                fg="black", width=12)
graphbtn.grid(row=10, column=0, padx=1, pady=1)                

mainloop()
