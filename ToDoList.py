import tkinter as tk
from tkinter import messagebox

class TodoListApp:
    def __init__(self, master):
        self.master = master
        master.title("Austodo")
        master.geometry("800x400")

        self.frame = tk.Frame(master, bg="light blue", width=800, height=100)
        self.frame.grid(row=0, column=0, padx=10, pady=20, sticky="ew")

        self.task_entry = tk.Entry(self.frame, width=50, bg="white", font=("Helvetica", 12))
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        self.add_button = tk.Button(self.frame, text="Add Task", command=self.add_task, bg="white", font=("Helvetica", 12), width=10)
        self.add_button.grid(row=0, column=1, padx=(0, 5), pady=10)

        self.clear_button = tk.Button(self.frame, text="Clear All Tasks", command=self.clear_tasks, bg="white", font=("Helvetica", 12), width=15)
        self.clear_button.grid(row=0, column=2, padx=(0, 10), pady=10)

        self.task_list = tk.Listbox(master, width=70, font=("Helvetica", 12, "bold"), height=15)
        self.task_list.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        self.delete_button = tk.Button(master, text="Delete Task", command=self.delete_task, bg="white", font=("Helvetica", 12), width=10)
        self.delete_button.grid(row=2, column=0, padx=(10, 5), pady=10, sticky="e")

        self.update_button = tk.Button(master, text="Update Task", command=self.update_task, bg="white", font=("Helvetica", 12), width=10)
        self.update_button.grid(row=2, column=0, padx=(0, 10), pady=10, sticky="w")

        self.tasks = []

    def add_task(self):
        task = self.task_entry.get()
        if not task:
            messagebox.showwarning("Error", "Please enter a task!")
            return

        self.tasks.append(task)
        self.task_list.insert(tk.END, task)
        self.task_entry.delete(0, tk.END)

    def delete_task(self):
        try:
            selected_index = self.task_list.curselection()[0]
        except IndexError:
            messagebox.showwarning("Error", "Please select a task to delete!")
            return

        self.task_list.delete(selected_index)
        del self.tasks[selected_index]

    def update_task(self):
        try:
            selected_index = self.task_list.curselection()[0]
        except IndexError:
            messagebox.showwarning("Error", "Please select a task to update!")
            return

        updated_task = self.task_entry.get()
        if not updated_task:
            messagebox.showwarning("Error", "Please enter a task!")
            return

        self.tasks[selected_index] = updated_task
        self.task_list.delete(selected_index)
        self.task_list.insert(selected_index, updated_task)
        self.task_entry.delete(0, tk.END)

    def clear_tasks(self):
        self.tasks.clear()
        self.task_list.delete(0, tk.END)

def main():
    root = tk.Tk()
    TodoListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
