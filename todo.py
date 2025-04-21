import tkinter as tk
from tkinter import messagebox

root=tk.Tk()
root.title("To-do list")


label=tk.Label(root,text="Enter the task",font=('Arial',24))
label.pack()

entry_task=tk.Entry(root,width=50)
entry_task.pack(pady=10)


btn_add=tk.Button(root,text="add task",width=48,command=add_task)
btn_add.pack()







root.mainloop()