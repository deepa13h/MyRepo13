#import all the modules
from tkinter import *

import sqlite3
import tkinter.messagebox

conn=sqlite3.connect("storedb.db")
c=conn.cursor()
result=c.execute("SELECT Max(id) from inventory")
for r in result:
    id=r[0]
items=c.execute("SELECT COUNT(*) from inventory")
for total in items:
    count=total[0]

class Database:
    def __init__(self,master,*args,**kwargs):
         self.master=master
         self.heading=Label(master,text="Add New Product to the Databse",font=('arial 35 bold'),fg='black',bg='green')
         self.heading.place(x=400,y=0)

         #inputs for the database
         self.name_l=Label(master,text="Enter Product Name",font=('arial 18 bold italic'))
         self.name_l.place(x=0,y=70)

         self.stock_l=Label(master,text="Enter Number of Items in Stock",font=('arial 18 bold italic'))
         self.stock_l.place(x=0,y=120)

         self.cp_l = Label(master, text="Enter Cost Price ", font=('arial 18 bold italic'))
         self.cp_l.place(x=0, y=170)

         self.sp_l = Label(master, text="Enter Retail Price", font=('arial 18 bold italic'))
         self.sp_l.place(x=0, y=220)

         self.vendor_l = Label(master, text="Enter Vendor Name", font=('arial 18 bold italic'))
         self.vendor_l.place(x=0, y=270)

         self.vendor_phone_l = Label(master, text="Enter Vendor's Contact Detail", font=('arial 18 bold italic'))
         self.vendor_phone_l.place(x=0, y=320)

         self.id_l = Label(master, text="Enter Product ID", font=('arial 18 bold italic'))
         self.id_l.place(x=0, y=370)

        #further entries

         self.name_e=Entry(master,width=25,font=('arial 18 bold'))
         self.name_e.place(x=380,y=70)

         self.stock_e = Entry(master, width=25, font=('arial 18 bold'))
         self.stock_e.place(x=380, y=120)

         self.cp_e = Entry(master, width=25, font=('arial 18 bold'))
         self.cp_e.place(x=380, y=170)

         self.sp_e = Entry(master, width=25, font=('arial 18 bold'))
         self.sp_e.place(x=380, y=220)

         self.vendor_e = Entry(master, width=25, font=('arial 18 bold'))
         self.vendor_e.place(x=380, y=270)

         self.vendor_phone_e = Entry(master, width=25, font=('arial 18 bold'))
         self.vendor_phone_e.place(x=380, y=320)

         self.id_e=Entry(master,width=25,font=('arial 18 bold'))
         self.id_e.place(x=380,y=370)

         
         self.btn_add=Button(master,text='Add Product to Database',width=25,height=2,bg='Green',fg='white',command=self.get_items)
         self.btn_add.place(x=520,y=420)

         self.btn_clear=Button(master,text="Clear Your Entries",width=18,height=2,bg='yellow',fg='red',command=self.clear_all)
         self.btn_clear.place(x=350,y=420)

          
         self.tbBox=Text(master,width=60,height=7,background='blue')
         self.tbBox.place(x=800,y=100)
         self.tbBox.insert(END,"Total number of products in the database is:"+str(count))

         self.master.bind('<Return>', self.get_items)
         self.master.bind('<Up>', self.clear_all)

    def get_items(self, *args, **kwargs):
    
       self.name = self.name_e.get()
       self.stock = self.stock_e.get()
       self.cp = self.cp_e.get()
       self.sp = self.sp_e.get()
       self.vendor = self.vendor_e.get()
       self.vendor_phone = self.vendor_phone_e.get()
       self.pid = self.id_e.get()

    
       self.totalcp = float(self.cp) * float(self.stock)
       self.totalsp = float(self.sp) * float(self.stock)
       self.assumed_profit = float(self.totalsp - self.totalcp)

       if self.name == '' or self.stock == '' or self.cp == '' or self.sp == '' or self.pid == '':
        tkinter.messagebox.showinfo("Error", "Please Fill all the entries.")
       else:
        sql = "INSERT INTO inventory (name, stock, cp, sp, totalcp, totalsp, assumed_profit, vendor, vendor_phoneno, pid ) VALUES(?,?,?,?,?,?,?,?,?,?)"
        c.execute(sql, (
        self.name, self.stock, self.cp, self.sp, self.totalcp, self.totalsp, self.assumed_profit, self.vendor,
        self.vendor_phone, self.pid))
        conn.commit()
        
        self.tbBox.insert(END, "\n\nProduct " + str(self.name) + " is added into the database with product id " + str(self.id_e.get()) +
        "\nCalculated Profit for the product is " + str(self.assumed_profit))
        tkinter.messagebox.showinfo("Done!", "Product is successfully added to the database")


    def clear_all(self, *args, **kwargs):
       num = id + 1
       self.name_e.delete(0, END)
       self.stock_e.delete(0, END)
       self.cp_e.delete(0, END)
       self.sp_e.delete(0, END)
       self.vendor_e.delete(0, END)
       self.vendor_phone_e.delete(0, END)

root=Tk()

b=Database(root)
root.configure(background='lightyellow',highlightbackground='green',highlightcolor='green',highlightthickness=5)
root.geometry("1366x768+0+0")
root.title("Inventory Management System - Group 4")

root.mainloop()
