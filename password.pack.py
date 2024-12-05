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
    
login_Label=tk.Label(text="username")
login_Label.grid(row=0,column=0,padx=25,pady=15)
    
entry_user=tk.Entry()
entry_user.grid(row=0,column=1)
    
password_Label=tk.Label(text="password")
password_Label.grid(row=1,column=0)
    
password_user=tk.Entry()
password_user.grid(row=1,column=1)
    
sub_button=tk.Button(text="submit",command=varify_user)
sub_button.grid(row=6,column=1,pady=400)
