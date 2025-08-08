import json
import os
import tkinter as tk
from tkinter import messagebox
from main_app import menu
from data_load_upload import load_data,save_file

log=[]
File="teacher_login.json"
log=load_data(File,log)
    
def create_account(prev_win):
    if prev_win:
        prev_win.destroy()

    create = tk.Tk()
    create.geometry(f"{create.winfo_screenwidth()}x{create.winfo_screenheight()}")
    create.title("create account")

    form_frame = tk.Frame(create)
    form_frame.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(form_frame, text="Name", font=("Arial", "14")).grid(row=0, column=0)
    name_entry = tk.Entry(form_frame, font=("Arial", "14"))
    name_entry.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(form_frame, text="email", font=("Arial", "14")).grid(row=1, column=0)
    email_entry = tk.Entry(form_frame, font=("Arial", "14"))
    email_entry.grid(row=1, column=1)

    tk.Label(form_frame, text="Password", font=("Arial", "14")).grid(row=2, column=0)
    password_entry = tk.Entry(form_frame, font=("Arial", "14"), show="*")
    password_entry.grid(row=2, column=1, padx=10, pady=10)

    def attempt_login():
        name=name_entry.get().strip()
        email=email_entry.get().strip()
        password=password_entry.get().strip()
        found=False
        if name and email and password:
            for i,info in enumerate(log):
                if info['email']==email:
                    messagebox.showerror("Exist","Your Account Already Exist")
                    found=True
                    create.destroy()
                    login(prev_win=None)
                    
                    break
        else:
            messagebox.showerror("No input",f"you did't gave any information")
            create_account(win=None)
        
        if not found:
            
            dict={
            "name":name,
            "email":email,
            "pasword":password
            }
            log.append(dict)
            save_file(File,log)
            messagebox.showinfo("welcome",f"welcome {dict['name']}")
            create.destroy()
            menu()######################## 
        
        

    tk.Button(form_frame, text="create", font=("Arial", "14", "bold"),bg="#27F56F", fg="white", command=attempt_login).grid(row=3, column=1, padx=10, pady=10)


def login(prev_win=None):
    if prev_win:
        prev_win.destroy()

    login = tk.Tk()
    login.geometry(f"{login.winfo_screenwidth()}x{login.winfo_screenheight()}")
    login.title("Login Page")

    # Frame to center the form
    form_frame = tk.Frame(login)
    form_frame.place(relx=0.5, rely=0.5, anchor="center")

    # Email Label & Entry
    tk.Label(form_frame, text="Email", font=("Arial", "14", "bold")).grid(row=0, column=0, padx=10, pady=10)
    email_entry = tk.Entry(form_frame, font=("Arial", "15"))
    email_entry.grid(row=0, column=1, padx=10, pady=10)

    # Password Label & Entry
    tk.Label(form_frame, text="Password", font=("Arial", "14", "bold")).grid(row=1, column=0, padx=10, pady=10)
    password_entry = tk.Entry(form_frame, font=("Arial", "15", "bold"), show="*")
    password_entry.grid(row=1, column=1, padx=10, pady=10)

    def data_check():
        email = email_entry.get().strip()
        password = password_entry.get().strip()
        found=False

        for i,info in enumerate(log):
            if info['email']== email and info["pasword"] == password:
                messagebox.showinfo(f"welcome {info['name']}",f"welcome {info['name']}")
                found=True
                login.destroy()
                menu()####################
                
                break
        if not found:   
            messagebox.showerror("Invalid","Invalid log in information")
        login.destroy()



        ...


    tk.Button(form_frame, text="Login", bg="#2DF73F", fg="black", command=data_check).grid(row=2, column=1, padx=10, pady=10)


    

    
    

    ... 


