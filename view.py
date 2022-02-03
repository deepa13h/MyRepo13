from tkinter import ttk

import tkinter as tk

import sqlite3
from tkinter.messagebox import NO


def connect():

    con1 = sqlite3.connect("storedb.db")

    cur1 = con1.cursor()

    cur1.execute("CREATE TABLE IF NOT EXISTS table1(id INTEGER PRIMARY KEY, First TEXT, Surname TEXT)")

    con1.commit()

    con1.close()


def View():

    con1 = sqlite3.connect("storedb.db")

    cur1 = con1.cursor()

    cur1.execute("SELECT * FROM inventory")

    rows = cur1.fetchall()    

    for row in rows:

        print(row) 

        tree.insert("", tk.END, values=row)        

    con1.close()


# connect to the database

connect() 

root = tk.Tk()

tree = ttk.Treeview(root, column=("c1", "c2", "c3","c4","c5","c6","c7","c8","c9","c10","c11"), show='headings',)

tree.column("#1", anchor=tk.CENTER,width=20)
tree.heading("#1", text="ID")

tree.column("#2", anchor=tk.CENTER,width=90)
tree.heading("#2", text="Product Name")

tree.column("#3", anchor=tk.CENTER,width=90)
tree.heading("#3", text="Stock")

tree.column("#4", anchor=tk.CENTER,width=90)
tree.heading("#4", text="Cost")

tree.column("#5", anchor=tk.CENTER,width=90)
tree.heading("#5", text="Selling Price")

tree.column("#6", anchor=tk.CENTER,width=90)
tree.heading("#6", text="Total Cost")

tree.column("#7", anchor=tk.CENTER)
tree.heading("#7", text="Total Selling Price")

tree.column("#8", anchor=tk.CENTER,width=90)
tree.heading("#8", text="Profit")

tree.column("#9", anchor=tk.CENTER)
tree.heading("#9", text="Vendor Name")

tree.column("#10", anchor=tk.CENTER)
tree.heading("#10", text="Vendor Contact details")

tree.column("#11", anchor=tk.CENTER)
tree.heading("#11", text="Product ID")

tree.pack()

button1 = tk.Button(text="Display Data", command=View,width=18,height=2,bg='green',fg='black')

button1.pack(pady=10)
button1.place(x=600,y=236)

def homePage1():
    root.destroy()
    import project
tk.Button(root, text="Home Page",command=homePage1,width=18,height=2,bg='grey',fg='black').place(x=860,y=236)

root.title('Inventory Management System')
root['bg']='#5d8a82'
root.geometry("1566x768+0+0")
root.mainloop()