import tkinter as tk
from tkinter import messagebox
root=tk.Tk()

def varify_user():
 user_name=entry_user.get()
 user_password=password_user.get()
 if user_name== "swetha" and user_password== "1236":
    messagebox.showinfo("succsessful","welcome to page")
 else:
    messagebox.showerror("invalid")
login_Label=tk.Label(text="username",fg="blue",bg="purple",height=6,width=12)
login_Label.pack()
    
entry_user=tk.Entry()
entry_user.pack()
    
password_Label=tk.Label(text="username",fg="blue",bg="purple",height=6,width=60)
password_Label.pack()
    
password_user=tk.Entry()
password_user.pack()
    
sub_button=tk.Button(text="submit",command=varify_user)
sub_button.pack()
