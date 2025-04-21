import tkinter as tk
from tkinter import messagebox

root=tk.Tk()
root.title("To-do list")


def add_task():
    task=entry_task.get()
    if task:
        list_Task.insert(tk.END,task)
        entry_task.delete(0,tk.END)
    else:
        messagebox.showerror("Error","Please enter a task")

def del_task():
    try:
        selected_task_index=list_Task.curselection()[0]
        list_Task.delete(selected_task_index)
    except:
        messagebox.showerror("Error","Please select a task to delete")

def on_closing():
    if messagebox.askokcancel("Quit","Do you want to quit?"):
        tasks=list_Task.get(0,tk.END)
        with open("tasks.txt","w") as file:
            for task in tasks:
                file.write(task + "\n")
    root.destroy    

label=tk.Label(root,text="Enter the task",font=('Arial',24))
label.pack()

entry_task=tk.Entry(root,width=50)
entry_task.pack(pady=10)


btn_add=tk.Button(root,text="add task",width=48,command=add_task)
btn_add.pack(pady=10)

btn_del=tk.Button(root,text="Delete button",width=48,command=del_task)
btn_del.pack(pady=10)

list_Task=tk.Listbox(root,selectmode=tk.SINGLE,height=10,width=50)
list_Task.pack(pady=20)

try:
    with open("tasks.txt", "r") as file:
        tasks=file.read().splitlines()
    for task in tasks:
        list_Task.insert(tk.END,task)
except FileExistsError:
    print("File not found")

root.protocol("WM_DELETE_WINDOW",on_closing)

root.mainloop()