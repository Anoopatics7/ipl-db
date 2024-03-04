from tkinter import ttk
import mysql.connector
import tkinter as tk
from tkinter import *

mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="anoopanoop",
        database="ipl")
    
c = mydb.cursor()


paddings = {'padx': 5, 'pady': 5}
        
root = tk.Tk()
root.geometry("1000x600")
root.title("IPL")
root.configure(bg='black')

def RCB():
        global rcb
        rcb=Toplevel(root)
        rcb.title("RCB")
        rcb.geometry("700x350")
        c.execute("SELECT b.Player_ID, b.Name , b.Age, b.contact FROM team a JOIN  player b ON a.Team_ID= b.Team_id WHERE a.Team_name LIKE '%Royal%Challengers%Banglore%' ORDER BY a.Team_ID;")
        result = c.fetchall() 
        
        table = ttk.Treeview(rcb)
        table["columns"] = ("ID", "Name","Age", "Contact")
        table.column("ID", width=50)
        table.column("Name", width=150)
        table.column("Age", width=50)
        table.column("Contact", width=100)
        table.heading("ID", text="ID")
        table.heading("Name", text="Name")
        table.heading("Age", text="Age")
        table.heading("Contact", text="Contact")  
        for row in result:
                table.insert("", END, values=row)
        table.pack()
        rcb.mainloop() 
     
def CSK():
        global csk
        csk=Toplevel(root)
        csk.title("CSK")
        csk.geometry("700x350") 
        c.execute("SELECT b.Player_ID, b.Name , b.Age, b.contact FROM team a JOIN  player b ON a.Team_ID= b.Team_id WHERE a.Team_name LIKE '%Chennai%Super%Kings%' ORDER BY a.Team_ID;")
        result = c.fetchall() 
        
        table = ttk.Treeview(csk)
        table["columns"] = ("ID", "Name","Age", "Contact")
        table.column("ID", width=50)
        table.column("Name", width=150)
        table.column("Age", width=50)
        table.column("Contact", width=100)
        table.heading("ID", text="ID")
        table.heading("Name", text="Name")
        table.heading("Age", text="Age")
        table.heading("Contact", text="Contact")  
        for row in result:
                table.insert("", END, values=row)
        table.pack()
        csk.mainloop()        

def KKR():
        global kkr
        kkr=Toplevel(root)
        kkr.title("KKR")
        kkr.geometry("700x350") 
        c.execute("SELECT b.Player_ID, b.Name , b.Age, b.contact FROM team a JOIN  player b ON a.Team_ID= b.Team_id WHERE a.Team_name LIKE '%Kolkota%knight%riders%' ORDER BY a.Team_ID;")
        result = c.fetchall() 
        
        table = ttk.Treeview(kkr)
        table["columns"] = ("ID", "Name","Age", "Contact")
        table.column("ID", width=50)
        table.column("Name", width=150)
        table.column("Age", width=50)
        table.column("Contact", width=100)
        table.heading("ID", text="ID")
        table.heading("Name", text="Name")
        table.heading("Age", text="Age")
        table.heading("Contact", text="Contact")  
        for row in result:
                table.insert("", END, values=row)
        table.pack()
        kkr.mainloop()
        
def DC():
        global dc
        dc=Toplevel(root)
        dc.title("DC")
        dc.geometry("700x350") 
        c.execute("SELECT b.Player_ID, b.Name , b.Age, b.contact FROM team a JOIN  player b ON a.Team_ID= b.Team_id WHERE a.Team_name LIKE '%Delhi%Capitals%' ORDER BY a.Team_ID;")
        result = c.fetchall() 
        
        table = ttk.Treeview(dc)
        table["columns"] = ("ID", "Name","Age", "Contact")
        table.column("ID", width=50)
        table.column("Name", width=150)
        table.column("Age", width=50)
        table.column("Contact", width=100)
        table.heading("ID", text="ID")
        table.heading("Name", text="Name")
        table.heading("Age", text="Age")
        table.heading("Contact", text="Contact")  
        for row in result:
                table.insert("", END, values=row)
        table.pack()
        dc.mainloop()
        
def MI():
        global mi
        mi=Toplevel(root)
        mi.title("MI")
        mi.geometry("700x350") 
        c.execute("SELECT b.Player_ID, b.Name , b.Age, b.contact FROM team a JOIN  player b ON a.Team_ID= b.Team_id WHERE a.Team_name LIKE '%Mumbai%Indians%' ORDER BY a.Team_ID;")
        result = c.fetchall() 
        
        table = ttk.Treeview(mi)
        table["columns"] = ("ID", "Name","Age", "Contact")
        table.column("ID", width=50)
        table.column("Name", width=150)
        table.column("Age", width=50)
        table.column("Contact", width=100)
        table.heading("ID", text="ID")
        table.heading("Name", text="Name")
        table.heading("Age", text="Age")
        table.heading("Contact", text="Contact")  
        for row in result:
                table.insert("", END, values=row)
        table.pack()
        mi.mainloop()


def insert_data():
    Injury_Type = entry1.get()
    Player_id = entry2.get()
    severity =entry3.get()

    
    sql = "INSERT INTO injury_record (Injury_Type,I_PlayerID ,Seviarity) VALUES (%s , %s , %s)"
    val = (Injury_Type, Player_id ,severity)
    
    c.execute(sql, val)
    mydb.commit()
    label4.config(text="Data inserted successfully.")

def addvalues():
        global add
        add=Toplevel(root)
        add.title("Insert values")
        add.geometry("200x200")
        
        label1 = Label(add, text="Injury Type ")
        label1.grid(row=0, column=0)
        
        global entry1 
        entry1 = Entry(add)
        entry1.grid(row=0, column=1)
        
        label2 = Label(add, text="Player id")
        label2.grid(row=1, column=0)
        
        global entry2
        entry2 = Entry(add)
        entry2.grid(row=1, column=1)
        
        label3 = Label(add, text="Severity")
        label3.grid(row=2, column=0)
        
        global entry3
        entry3 = Entry(add)
        entry3.grid(row=2, column=1)
        
        global label4
        label4 = Label(add, text="")
        label4.grid(row=3, column=1)
        
        button = Button(add, text="Insert Data", command=insert_data)
        button.grid(row=6, column=1)
                         
        add.mainloop()

def delete_row():
        Player_id = entryd1.get()
        severity=entryd2.get()
        
        sql= "DELETE FROM injury_record WHERE  I_PlayerID = (%s) AND Seviarity = (%s)"
        val=(Player_id , severity)
        c.execute(sql, val)
        mydb.commit()
        
        
def deleteValues():
        global delete
        delete=Toplevel(root)
        delete.title("delete Records")
        delete.geometry("200x200")
        labeld1 = Label(delete, text="Player Id ")
        labeld1.grid(row=0, column=0)
        
        global entryd1
        entryd1 = Entry(delete)
        entryd1.grid(row=0, column=1)
        
        labeld2 = Label(delete, text="Severity")
        labeld2.grid(row=1, column=0)
        
        global entryd2 
        entryd2 = Entry(delete)
        entryd2.grid(row=1, column=1)
        
        delete_button = tk.Button(delete, text="Delete", command=delete_row)
        delete_button.grid(row=2, column=1)
        
        delete.mainloop()
        
def disOwners():
        global ownerList
        ownerList=Toplevel(root)
        ownerList.title("Owners")
        ownerList.geometry("700x350")
        c.execute("SELECT * FROM owner;")
        result = c.fetchall() 
        
        table = ttk.Treeview(ownerList)
        table["columns"] = ("ID", "Name","contact", "Email-ID")
        table.column("ID", width=50)
        table.column("Name", width=150)
        table.column("contact", width=50)
        table.column("Email-ID", width=100)
        table.heading("ID", text="ID")
        table.heading("Name", text="Name")
        table.heading("contact", text="contact")
        table.heading("Email-ID", text="Email-ID")  
        for row in result:
                table.insert("", END, values=row)
        table.pack()
        ownerList.mainloop()

def display_venues():
    global venues
    venues = Toplevel(root)
    venues.title("Venues")
    venues.geometry("700x350")
    c.execute("SELECT * FROM Venue")
    result = c.fetchall()

    table = ttk.Treeview(venues)
    table["columns"] = ("ID", "Name", "Capacity", "Location")
    table.column("ID", width=70)
    table.column("Name", width=200)
    table.column("Capacity", width=70)
    table.column("Location", width=100)
    table.heading("ID", text="Venue ID")
    table.heading("Name", text="Venue Name")
    table.heading("Capacity", text="Capacity")
    table.heading("Location", text="Location")

    for row in result:
        table.insert("", tk.END, values=row)

    table.pack()
    venues.mainloop()

        
B = tk.Button(root, text ="Royal Challengers Banglore",fg="black",bg="White",activebackground="black",activeforeground="white",command=RCB)
B.place(x = 200, y = 140)
B = tk.Button(root, text ="Chennai Super Kings",fg="black",bg="White",activebackground="black",activeforeground="white",command=CSK)
B.place(x = 600, y = 140)
B = tk.Button(root, text ="kolkata Knight Riders",fg="black",bg="White",activebackground="black",activeforeground="white",command=KKR)
B.place(x = 200, y = 200)
B = tk.Button(root, text ="Mumbai Indians",fg="black",bg="White",activebackground="black",activeforeground="white",command=MI)
B.place(x = 600, y = 200)
B = tk.Button(root, text ="Delhi capitals",fg="black",bg="White",activebackground="black",activeforeground="white",command=DC)
B.place(x = 400, y = 260)
delete_button = tk.Button(root, text="Delete From Injury record", command=deleteValues)
delete_button.place(x=200 , y=450)

headerlabel = tk.Label(root, text="IPL DATABASE", font=("Arial Bold", 50),foreground="red",background="black")
headerlabel.place(relx=0.45, rely=0.1,anchor=CENTER )

B = tk.Button(root, text ="Insert Into Injury record",fg="black",bg="White",activebackground="black",activeforeground="white",command=addvalues)
B.place(x = 200, y = 500)

B = tk.Button(root, text ="Venue",fg="black",bg="White",activebackground="black",activeforeground="white",command=display_venues)
B.place(x = 600, y = 400)

B = tk.Button(root, text ="Display Owners",fg="black",bg="White",activebackground="black",activeforeground="white",command=disOwners)
B.place(x = 200, y = 400)

root.mainloop()