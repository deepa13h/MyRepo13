import tkinter as tk
from subprocess import call
from tkinter.font import BOLD

ws = tk.Tk()
ws.title('Inventory Management System')
ws['bg']='#5d8a82'

f = ("Times bold", 14)
l= ("Times bold", 18)

w = tk.Label(ws, text="Inventory Management System", height=2,font=l,fg='black',border=2)
w.place(x=20)
w.pack()

def addPage():
     ws.destroy()
     call(["python", "add_to_db.py"])

def viewPage():
    ws.destroy()
    call(["python", "test.py"])

def updatePage():
    ws.destroy()
    call(["python", "update.py"])

def billPage():
    ws.destroy()
    call(["python", "main.py"])

def deletePage():
    ws.destroy()
    call(["python", "delete.py"])

tk.Button(ws, text="Add Products to Database", font=f,command=addPage,width=30,height=1).place(x=100,y=100)
tk.Button(ws, text="View Products in Database", font=f,command=viewPage,width=30,height=1).place(x=100,y=210)
tk.Button(ws, text="Search and Update Products", font=f,command=updatePage,width=30,height=1).place(x=100,y=320)
tk.Button(ws, text="Generate Bill", font=f,command=billPage,width=30,height=1).place(x=100,y=430)
tk.Button(ws, text="Delete Product", font=f,command=deletePage,width=30,height=1).place(x=100,y=540)

ws.geometry("1566x768+0+0")
ws.mainloop()