import tkinter as tk
import json
import os
from tkinter import messagebox
from data_load_upload import save_file,load_data,destroy_win
from scrollbar import scroll_it
import datetime

student_batch={
    "1st":"212-134-",
    "2nd":"221-134-",
    "3rd":"222-134-",
    "4th":"231-134-", 
    "5th":"232-134-",
    "6th":"241-134-",
    "7th":"242-134-"
}

marking_feilds={
        "class test 1":"CT1",
        "class test 2":"CT2",
        "Assignment":"assignment",
        
    }


def create_student_file():
    master = tk.Tk()
    master.geometry(f"{master.winfo_screenwidth()}x{master.winfo_screenheight()}")
    master.title("Create Student File")
    
    
    form_frame = tk.Frame(master)
    form_frame.place(relx=0.5, rely=0.5, anchor="center")
    
    tk.Label(form_frame, text="Select Batch", font=("Arial", 15, "bold"), bg="#2DF7BE", fg="black").pack(padx=10, pady=10)
   
    file_batch = tk.StringVar(master)
    file_batch.set("click")
    op_menu = tk.OptionMenu(form_frame, file_batch, *student_batch.keys())
    op_menu.config(font=("Arial", 15), bg="#2DF7BE")
    op_menu.pack(padx=10, pady=10)

    tk.Label(form_frame, text="Number of students", font=("Arial", 15, "bold")).pack(padx=10, pady=10)

    students_number = tk.Entry(form_frame, font=("Arial", 15))
    students_number.pack(padx=5, pady=5)

    
    def file_creation():
        try:
            num=int(students_number.get().strip())
            if num<=0:
                raise ValueError
        except(ValueError):
            messagebox.showerror("student number","put integer as a input ")

        batch_id=student_batch[f'{file_batch.get()}']
        batch_num=file_batch.get()
        Filename=f'{batch_num} {batch_id} sheet.json'
        students=[]
        for i in range(0,num+1):
            if i==0:
                students.append({"null":f"{batch_id}{i:03}",
                                 "attendance":0,
                                 "CT1":None,
                                 "ct1_marking_count":0,
                                 "CT2":None,
                                 "ct2_marking_count":0,
                                 "assignment":None,
                                 "assignment_marking_count":0,
                                 "total":None,
                                 "total_student":num})
            else:    
                students.append({"id":f"{batch_id}{i:03}",
                                "attendance":0,
                                "CT1":None,
                                "CT2":None,
                                "assignment":None,
                                "total":None})
        
        save_file(Filename,students)
        messagebox.showinfo("success","Your file has been created")
        master.destroy()
        
    ...

    tk.Button(form_frame, text="Done", font=("Arial", 15, "bold"), bg="#44FF5A", fg="black", command=file_creation).pack(padx=10, pady=10)
    tk.Label(form_frame,text='''
             
Default Feilds Are:
1. Attendance
2.CT1
3.CT2
4.Assignment
             
             ''',font=("Arial",15,"bold")).pack(padx=10,pady=10)
    master.mainloop()
    ...
def mark_attendance():
    master=tk.Tk()
    master.geometry(f"{master.winfo_screenwidth()}x{master.winfo_screenheight()}")
    master.title("Mark Attendance")

    form_frame = tk.Frame(master)
    form_frame.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(master,text="Select Batch",font=("Arial",15,"bold"),bg="#2DF7BE",fg="black").pack(padx=10,pady=10)
    file_batch=tk.StringVar(master)
    file_batch.set("click")
    op_menu=tk.OptionMenu(master,file_batch,*[key for i,key in enumerate(student_batch)])
    op_menu.config(font=("Arial", 15), bg="#2DF7BE")
    op_menu.pack(padx=10,pady=10)
    

    def marking():
        batch_id=student_batch[f'{file_batch.get()}']
        batch_num=file_batch.get()
        Filename=f'{batch_num} {batch_id} sheet.json'
        students=[]
        students=load_data(Filename,students)

        if not students:
            messagebox.showerror("Error","file have no student info please create an new file ")
            return
        
       
        scroll_it(Filename,students)
    ...

    tk.Button(master,text="Done",font=("Arial","15","bold"),bg="#44FF5A",fg="black",command=marking).pack(padx=10,pady=10)
    tk.Button(master,text="EXIT",font=("Arial",15,"bold"),bg="red",fg="black",command=lambda:destroy_win(master)).pack(padx=10,pady=10)
    master.mainloop()
    
    ...

def view_attendance():
    master=tk.Tk()
    master.geometry(f"{master.winfo_screenwidth()}x{master.winfo_screenheight()}")
    master.title("Mark Attendance")

    form_frame = tk.Frame(master)
    form_frame.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(master,text="Select Batch",font=("Arial",15,"bold"),bg="#2DF7BE",fg="black").pack(padx=10,pady=10)
    file_batch=tk.StringVar(master)
    file_batch.set("click")
    op_menu=tk.OptionMenu(master,file_batch,*[key for i,key in enumerate(student_batch)])
    op_menu.config(font=("Arial", 15), bg="#2DF7BE")
    op_menu.pack(padx=10,pady=10)
    

    def show_it():
        batch_id=student_batch[f'{file_batch.get()}']
        batch_num=file_batch.get()
        Filename=f'{batch_num} {batch_id} sheet.json'
        students=[]
        students=load_data(Filename,students)
        def on_mouse_wheel(event):
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        students=[]
        students=load_data(Filename)

        view=tk.Tk()
        view.title("sheet")
        view.geometry(f"{view.winfo_screenwidth()}x{view.winfo_screenheight()}")
     
        view_frame=tk.Frame(view)
        view_frame.place(relx=0.5,rely=0.5,anchor="center")

        canvas=tk.Canvas(view_frame,width=500,height=400)
        scrollbar=tk.Scrollbar(view_frame,orient="vertical",command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)

        scrollable_frame=tk.Frame(canvas)
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        canvas.create_window((0,0),window=scrollable_frame,anchor="nw")

        canvas.pack(side="left",fill="both",expand=True)
        scrollbar.pack(side="right",fill="y")
        canvas.bind_all("<MouseWheel>",on_mouse_wheel)
        tk.Label(view,text=f'''
            Marksheet of {batch_num}
            Total class Days:{students[0]['attendance']}
            CT1 out of {students[0]['CT1']if students[0]['CT1'] else"<Not Taken>" }and CT2 out of{students[0]['CT2'] if students[0]['CT2'] else"<Not Taken>"}
''',font=("Arial",14,"bold")).pack(padx=10,pady=100)
    
        
        for ind,info in enumerate(students):
            if ind==0:
                tk.Label(scrollable_frame,text=f'''
ID           Attendance           CT1              CT2             Assignment              Total
''').pack(padx=10,pady=10)

                ...
            else:
                attendance=(info['attendance']/students[0]['attendance'])*100
                ct1=info['CT1']
                ct2=info['CT2']
                Assignment=info['assignment']
                total=(int(attendance if attendance else 0)/10)+int(ct1 if ct1 else 0)+int(ct2 if ct2 else 0)+int(Assignment if Assignment else 0)
                info['total']=total
                tk.Label(scrollable_frame,text=f'''
{info['id']}                    {attendance}%                    {info['CT1']}               {info['CT2']}               {info['assignment']}                    {info['total']}                   
''').pack(padx=10,pady=10)
    
    
    tk.Button(master,text="Submit",bg="green",fg="black",font=("Arial",15,"bold"),command=show_it).pack(padx=10,pady=10)

   

    

    master.mainloop()
    ...

def add_ct_marks():

    add=tk.Tk()
    add.title("Add CT Marks")
    add.geometry(f"{add.winfo_screenwidth()}x{add.winfo_screenheight()}")
    tk.Label(add,text="Select Batch",font=("Arial",15,"bold"),bg="#2DF7BE",fg="black").pack(padx=10,pady=10)
    file_batch=tk.StringVar(add)
    file_batch.set("click")
    op_menu=tk.OptionMenu(add,file_batch,*[key for i,key in enumerate(student_batch)])
    op_menu.config(font=("Arial", 15), bg="#2DF7BE")
    op_menu.pack(padx=10,pady=10)

    tk.Label(add,text="select add feild",font=("Arial",14,"bold")).pack(padx=10,pady=10)
    field_name=tk.StringVar(add)
    field_name.set("Click")

    file_op_menu=tk.OptionMenu(add,field_name,*[key for i,key in enumerate(marking_feilds)])
    file_op_menu.config(font=("Arial",14))
    file_op_menu.pack(padx=10,pady=10)

    

    def marking():
       

        filed_name_dict=marking_feilds[f'{field_name.get()}']
        batch_id=student_batch[f'{file_batch.get()}']
        batch_num=file_batch.get()
        Filename=f'{batch_num} {batch_id} sheet.json'
        students=[]
        students=load_data(Filename,students)
        total_stu=students[0]["total_student"]

        popup=tk.Toplevel()
        popup.geometry("500x400")
        def show_it(i):
            if i==0:
                tk.Label(popup,text="CT marks").pack()
                entry=tk.Entry(popup,font=("Arial",10))
                entry.pack(padx=10,pady=10)
                entry_val=int(entry.get())
                students[0][f"{filed_name_dict}_marking_count"]=entry_val

                ...
            else:
                
                tk.Label(popup,text=f"{students[i]['id']}").pack()
                entry=tk.Entry(popup,font=("Arial",14))
                entry.pack(padx=10,pady=10)
                def apply(i,students,feilds):
                    marks=int(entry.get())
                    students[i][feilds]=marks
                    students[0][f"{feilds}_marking_count"]=i
                    destroy_win(popup)

                tk.Button(popup,text="apply",command=lambda :apply(i,students,filed_name_dict)).pack()


            popup.mainloop()



        ...

    tk.Button(add,text="Submit",bg="green",fg="black",font=("Arial",14,"bold"),command=marking).pack(padx=10,pady=10)
    tk.Button(add,text="Back",font=("Arial",14,"bold"),command=add.quit).pack(padx=10,pady=10)
    add.mainloop()
    ...

def menu():
    menu = tk.Tk()
    menu.title("Features")
    menu.geometry(f"{menu.winfo_screenwidth()}x{menu.winfo_screenheight()}")

    
    menu_frame = tk.Frame(menu)
    menu_frame.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(menu_frame, text="Welcome!", font=("Arial", 20, "bold")).grid(row=0, column=0, padx=10, pady=10)
    tk.Button(menu_frame, text="Create student file", font=("Arial", 15, "bold"),bg="#C82DF7", fg="black", command=create_student_file).grid(row=1, column=0, padx=10, pady=10)
    tk.Button(menu_frame, text="Mark Attendance", font=("Arial", 15, "bold"),bg="#C82DF7", fg="black", command=mark_attendance).grid(row=2, column=0, padx=10, pady=10)
    tk.Button(menu_frame, text="View Attendance", font=("Arial", 15, "bold"),bg="#C82DF7", fg="black",command=view_attendance).grid(row=3, column=0, padx=10, pady=10)
    tk.Button(menu_frame, text="ADD CT and Assignment", font=("Arial", 15, "bold"),bg="#C82DF7", fg="black",command=add_ct_marks).grid(row=4, column=0, padx=10, pady=10)
    tk.Button(menu_frame, text="EXIT", font=("Arial", 15, "bold"),bg="red", fg="black", command=lambda: destroy_win(menu)).grid(row=5, column=0, padx=10, pady=10)

    menu.mainloop()
    ...
#menu() #done ✅
#create_student_file() #done✅
#mark_attendance() #done✅
#view_attendance()
add_ct_marks()