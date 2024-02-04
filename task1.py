import tkinter as tk

root = tk.Tk()
root.title("To-Do List")


task_entry = tk.Entry(root, width=150)
task_entry.grid(row=0, column=0, padx=20, pady=20)

task_list = tk.Listbox(root, width=150, height=10)
task_list.grid(row=2, column=0, padx=20, pady=20)


def add_task():
    task = task_entry.get()
    task_list.insert(tk.END, task)
    task_entry.delete(0, tk.END)  

def delete_task():
    task_index = task_list.curselection()[0]
    task_list.delete(task_index)

def show_author_info():
    top = tk.Toplevel(root)
    top.title("Creater Info")
    tk.Label(top, text="To-Do List Application").pack()
    tk.Label(top, text="Created by:- kiran kumar manikandan").pack()
    tk.Label(top, text="Email: kk5613789@gmail.com").pack()
   

# buttons
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.grid(row=1, column=0, sticky="w", padx=20, pady=20)

delete_button = tk.Button(root, text="Delete Selected Task", command=delete_task)
delete_button.grid(row=1, column=0, sticky="e", padx=20, pady=20)

# button to open the author information window
author_button = tk.Button(root, text="Creater Info", command=show_author_info)
author_button.grid(row=3, column=0, sticky="s",padx=20,pady=20)  

root.mainloop()
