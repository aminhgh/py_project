# input login form by python 

#import tkinter 
#import functools
from tkinter import *
from functools import partial

def Validate_login(username,password):
    print("Enter your Username",username.get())
    print("Enter your Password",password.get())
    return

tk_window = Tk()
tk_window.geometry("400x150")
tk_window.title("Login Form")

#username_labels
username_label = Label(tk_window,text="username").grid(row=0,column=0)
#username Type
username = StringVar()
#username Entry
username_Entry = Entry(tk_window,textvariable=username).grid(row=0,column=1)
#password_labels
password_label = Label(tk_window,text="password").grid(row=1,column=0)
#password Type
password = StringVar()
#password Entry
password_Entry  = Entry(tk_window,textvariable=password).grid(row=1,column=1)

# validation

Validate_login = partial(Validate_login,username,password)

Login_button = Button(tk_window,text="Login" ,command=Validate_login ).grid(row=4,column=0)

tk_window.mainloop()