import tkinter as tk
import json
from tkinter import messagebox
from data_load_upload import save_file, load_data, destroy_win
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

def marking():
    add = tk.Tk()
    add.title("Add CT Marks")
    add.geometry(f"{add.winfo_screenwidth()}x{add.winfo_screenheight()}")

    tk.Label(add, text="Select Batch", font=("Arial", 15, "bold"), bg="#2DF7BE", fg="black").pack(padx=10, pady=10)
    file_batch = tk.StringVar(add)
    file_batch.set("click")
    op_menu = tk.OptionMenu(add, file_batch, *student_batch.keys())
    op_menu.config(font=("Arial", 15), bg="#2DF7BE")
    op_menu.pack(padx=10, pady=10)

    tk.Label(add, text="Select Field", font=("Arial", 14, "bold")).pack(padx=10, pady=10)
    field_name = tk.StringVar(add)
    field_name.set("click")
    file_op_menu = tk.OptionMenu(add, field_name, *marking_feilds.keys())
    file_op_menu.config(font=("Arial", 14))
    file_op_menu.pack(padx=10, pady=10)

    def start_marking():
        if file_batch.get() == "click" or field_name.get() == "click":
            messagebox.showwarning("Warning", "Please select both batch and field.")
            return

        filed_name_dict = marking_feilds[field_name.get()]
        batch_id = student_batch[file_batch.get()]
        batch_num = file_batch.get()
        Filename = f'{batch_num} {batch_id} sheet.json'

        students = []
        students = load_data(Filename, students)
        total_stu = students[0]["total_student"]

        if students[0][f"{filed_name_dict}_marking_count"] == 0:
            current_index = 1  # Start from 1

            def show_popup(i):
                if i > total_stu:
                    save_file(Filename, students)
                    messagebox.showinfo("Done", "All students marked.")
                    return

                popup = tk.Toplevel(add)
                popup.geometry("500x400")
                tk.Label(popup, text=f"Student ID: {students[i]['id']}", font=("Arial", 16)).pack(pady=20)
                entry = tk.Entry(popup, font=("Arial", 14))
                entry.pack(padx=10, pady=10)

                def apply():
                    try:
                        marks = int(entry.get())
                        students[i][filed_name_dict] = marks
                        students[0][f"{filed_name_dict}_marking_count"] = i
                        popup.destroy()
                        show_popup(i + 1)
                    except ValueError:
                        tk.Label(popup, text="Please enter a valid number", fg="red").pack()

                def exit_marking():
                    save_file(Filename, students)
                    popup.destroy()

                tk.Button(popup, text="Apply", command=apply, bg="green", font=("Arial", 12, "bold")).pack(pady=10)
                tk.Button(popup, text="Exit", command=exit_marking, bg="red", font=("Arial", 12, "bold")).pack()

            show_popup(current_index)
        else:
            messagebox.showinfo("Info", "Marks already added for this field.")

    # Buttons
    tk.Button(add, text="Submit", bg="green", fg="black", font=("Arial", 14, "bold"), command=start_marking).pack(padx=10, pady=10)
    tk.Button(add, text="Back", font=("Arial", 14, "bold"), command=add.quit).pack(padx=10, pady=10)

    add.mainloop()

marking()