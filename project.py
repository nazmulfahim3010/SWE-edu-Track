import tkinter as tk
from PIL import Image,ImageTk
from account_center import create_account,login
from data_load_upload import destroy_win

welcome=tk.Tk() 
welcome.configure(bg="white") 
welcome.geometry(f"{welcome.winfo_screenwidth()}x{welcome.winfo_screenheight()}")

bg_image=Image.open("bg.png")
bg_image=bg_image.resize((500,400)) 
bg_photo=ImageTk.PhotoImage(bg_image)
 
tk.Label(welcome,image =bg_photo).place(x=0, y=0, relwidth=1, relheight=1)

tk.Label(welcome,text="welcome to SWE Edu Track",font=("Arial","18","bold")).pack(padx=50,pady=30)
tk.Button(welcome,text="Login",font=("Arial","15","bold"),bg="green",fg="white",command=lambda :login(welcome)).pack(padx=10,pady=10)
tk.Button(welcome,text="Create Acoount",font=("Arial","15","bold"),bg="#A327F5",fg="white",command=lambda :create_account(welcome)).pack(padx=10,pady=10)
tk.Button(welcome,text="Exit",font=("Arial","15","bold"),command=welcome.quit,bg="#F54927",fg="white").pack(padx=10,pady=10)

 
tk.mainloop()
welcome.destroy()