import mysql.connector
import tkinter as tk
from tkinter import messagebox

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("300x200")
        self.root.title("IPL Login Page")
        
        self.label1 = tk.Label(root, text="Username -", font=('bold', 10))
        self.label1.place(x=40, y=30)
        
        self.username = tk.Entry(root, width=35)
        self.username.place(x=130, y=33, width=120)
        
        self.label2 = tk.Label(root, text="Password -", font=('bold', 10))
        self.label2.place(x=40, y=60)
        
        self.password = tk.Entry(root, width=25, show="*")  # Show asterisks by default
        self.password.place(x=130, y=63, width=100)
        
        # Button to toggle password visibility
        self.eye_button = tk.Button(root, text="👁", command=self.toggle_password_visibility)
        self.eye_button.place(x=235, y=60)
        
        self.submitbtn = tk.Button(root, text="Login", bg='white', command=self.submit)
        self.submitbtn.place(x=150, y=135, width=55)
        
        self.password_visible = False  # Flag to track password visibility
    
    def toggle_password_visibility(self):
        if self.password_visible:
            self.password.config(show="*")  # Hide password
            self.password_visible = False
        else:
            self.password.config(show="")  # Show password
            self.password_visible = True
            
    def error_destroy(self):
        self.err.destroy()
        
    def error(self):
        self.err = tk.Toplevel(root)
        self.err.title("Error")
        self.err.geometry("200x150")
        errlabel = tk.Label(self.err, text="Enter valid details...", fg="red", font="bold")
        errlabel.place(x=15, y=20)
        tk.Label(self.err, text="").pack()
        errok = tk.Button(self.err, text="Ok", bg="grey", width=8, height=1, command=self.error_destroy)
        errok.place(x=50, y=70)
        
    def submit(self):
        user = self.username.get()
        passget = self.password.get()
        self.logindb(user, passget)
        
    def logindb(self, user, passget):
        if user == 'root' and passget == 'anoopanoop':
            #mydb = mysql.connector.connect(
            #host="localhost",
            #user="root",
            #password="anoopanoop",
            #database="ipl")
            self.nextPage()
        else:
            self.error()
            
    def nextPage(self):
        self.root.destroy()
        import details 

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()
