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
login_Label=tk.Label(text="username",fg="blue",height=40,width=60)
login_Label.grid(row=0,column=3,pady=50)
    
entry_user=tk.Entry()
entry_user.grid(row=0,column=3,pady=50)
    
password_Label=tk.Label(text="username",height=40,width=60)
password_Label.grid(row=0,column=3,padx=50)
    
password_user=tk.Entry()
password_user.grid(row=0,column=3,pady=50)
    
sub_button=tk.Button(text="submit",command=varify_user)
sub_button.grid(row=0,column=3,pady=50)
