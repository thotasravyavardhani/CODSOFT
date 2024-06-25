import tkinter as tk
from tkinter import messagebox

class ToDoList:

    def __init__(self, root):
        self.root = root
        root.title("To Do List")
        root.configure(bg="#fff043")

        # Create tasks list
        self.tasks = []

        # Create entry box for new tasks
        self.entry = tk.Entry(root, width=38, font=('Arial', 14), bd=2)
        self.entry.grid(row=0, column=0, padx=8, pady=8)

        # Create Add Task button
        self.addtask = tk.Button(root, text='Add Task', command=self.add_task, bg="green", fg="white", font=('Arial', 12, 'bold'), bd=2)
        self.addtask.grid(row=0, column=1, padx=8, pady=8)

        # Create listbox to display tasks
        self.listbox = tk.Listbox(root, width=55, height=10, font=('Arial', 14), bd=2, selectbackground="lightgray")
        self.listbox.grid(row=1, column=0, columnspan=3, padx=8, pady=8)

        # Create Delete Task button
        self.deletetask = tk.Button(root, text="Delete Task", command=self.delete_task, bg="red", fg="white", font=('Arial', 12, 'bold'), bd=2)
        self.deletetask.grid(row=2, column=0, padx=8, pady=8)

        # Create Clear All Tasks button
        self.cleartasks = tk.Button(root, text="Clear All", command=self.clear_tasks, bg="black", fg="white", font=('Arial', 12, 'bold'), bd=2)
        self.cleartasks.grid(row=2, column=1, padx=8, pady=8)

        # Create Update Task button
        self.updatetask = tk.Button(root, text="Update Task", command=self.update_task_entry, bg="blue", fg="white", font=('Arial', 12, 'bold'), bd=2)
        self.updatetask.grid(row=2, column=2, padx=8, pady=8)

    def add_task(self):
        task = self.entry.get()
        if task:
            self.tasks.append(task)
            self.update_task()
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning(title='Warning', message='Please enter a task')

    def update_task(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            self.listbox.insert(tk.END, task)

    def delete_task(self):
        item_position = self.listbox.curselection()
        if item_position:
            item_name = self.listbox.get(item_position)
            confirmation = messagebox.askyesno(title='Confirmation', message=f'Are you sure you want to delete "{item_name}"?')
            if confirmation:
                self.tasks.remove(item_name)
                self.update_task()
        else:
            messagebox.showwarning(title="Warning", message="Please select an item")

    def clear_tasks(self):
        confirmation = messagebox.askyesno(title='Confirmation', message='Are you sure you want to clear all tasks?')
        if confirmation:
            self.tasks.clear()
            self.update_task()

    def update_task_entry(self):
        item_position = self.listbox.curselection()
        if item_position:
            item_name = self.listbox.get(item_position)
            self.entry.delete(0, tk.END)
            self.entry.insert(0, item_name)
            self.tasks.remove(item_name)
            self.update_task()
        else:
            messagebox.showwarning(title="Warning", message="Please select an item to update")

window = tk.Tk()
root = ToDoList(window)
window.mainloop()
