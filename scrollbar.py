import tkinter as tk
from data_load_upload import save_file
from tkinter import messagebox
from datetime import datetime


def scroll_it(filename,students):
    file_name=filename
    stu=students

    def on_mouse_wheel(event):
        canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    def scroll_up():
        canvas.yview_scroll(-10, "units")

    def scroll_down():
        canvas.yview_scroll(10, "units")

    mark = tk.Tk()
    mark.title("Scroll")
    mark.geometry(f"{mark.winfo_screenwidth()}x{mark.winfo_screenheight()}") 

    
    frame_container = tk.Frame(mark, width=500, height=400)
    frame_container.pack(pady=10)

    
    canvas = tk.Canvas(frame_container, width=500, height=400)
    scrollbar = tk.Scrollbar(frame_container, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)

    scrollable_frame = tk.Frame(canvas)
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0,0), window=scrollable_frame, anchor="nw")

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    canvas.bind_all("<MouseWheel>", on_mouse_wheel)

    clicked=False

    for ind,info in enumerate(students):
        if ind==0:
            ...
        else:
            check=tk.IntVar()
            def increment(n, student_info):
                
                if n.get() == 1:

                    student_info['attendance'] += 0
                else:
                    nonlocal clicked
                    clicked=True
                    student_info['attendance']  +=1

            tk.Checkbutton(scrollable_frame, text=f"{ind}. {info['id']}",font=("Arial",15,"bold"),variable=check,command=lambda v=check, s =info: increment(v,s)).pack(anchor="w")
        
    
    btn_frame = tk.Frame(mark)
    btn_frame.pack(pady=5)

    tk.Button(btn_frame, text="▲ Scroll Up", command=scroll_up).pack(side="left", padx=5)
    tk.Button(btn_frame, text="▼ Scroll Down", command=scroll_down).pack(side="left", padx=5)
    
    
    
    def save_and_destroy():
        if not clicked:
            messagebox.showerror("No input",f"There is no input you have given")
            mark.destroy()
            return
        stu[0]['attendance']+=1
        save_file(file_name,stu)
        messagebox.showinfo("success",f"Attendance of {datetime.today()}  is done!")

        mark.destroy()


    tk.Button(mark, text="Submit",font=("Arial",15,"bold"),  bg="green", fg="white",command=save_and_destroy).pack(pady=10)
    

    mark.mainloop()


