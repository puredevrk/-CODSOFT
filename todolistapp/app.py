# import tkinter as tk
# import pickle
# from tkinter import messagebox

# # Function to add a new task
# def add_task():
#     task = entry.get()
#     if task:
#         tasks.append({"task": task, "status": "active"})
#         update_listbox()
#         entry.delete(0, tk.END)
#         save_tasks_to_file()

# # Function to edit an existing task
# def edit_task():
#     selected_task_index = listbox.curselection()
#     if selected_task_index:
#         selected_task_index = int(selected_task_index[0])
#         new_task = entry.get()
#         if new_task:
#             tasks[selected_task_index]["task"] = new_task
#             update_listbox()
#             entry.delete(0, tk.END)
#             save_tasks_to_file()
#         else:
#             messagebox.showwarning("Warning", "Task cannot be empty!")

# # Function to delete a task
# def delete_task():
#     selected_task_index = listbox.curselection()
#     if selected_task_index:
#         selected_task_index = int(selected_task_index[0])
#         del tasks[selected_task_index]
#         update_listbox()
#         save_tasks_to_file()

# # Function to mark a task as completed
# def mark_completed():
#     selected_task_index = listbox.curselection()
#     if selected_task_index:
#         selected_task_index = int(selected_task_index[0])
#         tasks[selected_task_index]["status"] = "completed"
#         update_listbox()
#         save_tasks_to_file()

# # Function to update the listbox with tasks
# def update_listbox():
#     listbox.delete(0, tk.END)
#     for task in tasks:
#         listbox.insert(tk.END, f"{task['task']} - {task['status']}")

# # Function to save tasks to a file using pickle
# def save_tasks_to_file():
#     with open("tasks.pkl", "wb") as file:
#         pickle.dump(tasks, file)

# # Function to load tasks from a file using pickle
# def load_tasks_from_file():
#     try:
#         with open("tasks.pkl", "rb") as file:
#             return pickle.load(file)
#     except FileNotFoundError:
#         return []

# # Main program
# tasks = load_tasks_from_file()

# root = tk.Tk()
# root.title("To-Do List App")

# # Entry for task input
# entry = tk.Entry(root, width=50)
# entry.pack()

# # Buttons for actions
# add_button = tk.Button(root, text="Add Task", command=add_task,fg='blue')

# add_button.pack()

# edit_button = tk.Button(root, text="Edit Task", command=edit_task,fg='blue')
# edit_button.pack()

# delete_button = tk.Button(root, text="Delete Task", command=delete_task,fg='blue')
# delete_button.pack()

# mark_completed_button = tk.Button(root, text="Mark Completed", command=mark_completed,fg='blue')
# mark_completed_button.pack()

# # Listbox to display tasks
# listbox = tk.Listbox(root, width=50)
# listbox.pack()

# # Load tasks into the listbox
# update_listbox()
# root.state("zoomed")
# root.mainloop()
import tkinter as tk
from tkinter import messagebox
import pickle

# Function to add a new task with a title and description
def add_task():
    task_title = entry_title.get()
    task_description = entry_description.get()
    if task_title:
        tasks.append({"title": task_title, "description": task_description, "status": "active"})
        update_listbox()
        entry_title.delete(0, tk.END)
        entry_description.delete(0, tk.END)
        save_tasks_to_file()

# Function to edit an existing task
def edit_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        selected_task_index = int(selected_task_index[0])
        new_title = entry_title.get()
        new_description = entry_description.get()
        if new_title:
            tasks[selected_task_index]["title"] = new_title
            tasks[selected_task_index]["description"] = new_description
            update_listbox()
            entry_title.delete(0, tk.END)
            entry_description.delete(0, tk.END)
            save_tasks_to_file()
        else:
            messagebox.showwarning("Warning", "Task title cannot be empty!")

# Function to mark a task as completed or active
def toggle_task_status():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        selected_task_index = int(selected_task_index[0])
        if tasks[selected_task_index]["status"] == "active":
            tasks[selected_task_index]["status"] = "completed"
        else:
            tasks[selected_task_index]["status"] = "active"
        update_listbox()
        save_tasks_to_file()

# Function to delete a task
def delete_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        selected_task_index = int(selected_task_index[0])
        del tasks[selected_task_index]
        update_listbox()
        save_tasks_to_file()

# Function to update the listbox with tasks
def update_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        title = task.get('title', 'Unknown Task')
        description = task.get('description', 'No Description')
        status = task.get('status', 'Unknown Status')
        listbox.insert(tk.END, f"{title} - {description} - {status}")

# Function to load tasks from a file or create an empty list if the file doesn't exist
def load_tasks_from_file():
    try:
        with open("tasks.pkl", "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        return []

# Function to save tasks to a file using pickle
def save_tasks_to_file():
    with open("tasks.pkl", "wb") as file:
        pickle.dump(tasks, file)

# Main program
root = tk.Tk()
root.title("To-Do List App")

# Entry for task title input
label_title = tk.Label(root, text="Task Title:")
label_title.pack()
entry_title = tk.Entry(root, width=50)
entry_title.pack()

# Entry for task description input
label_description = tk.Label(root, text="Task Description:")
label_description.pack()
entry_description = tk.Entry(root, width=50)
entry_description.pack()

# Buttons for actions
add_button = tk.Button(root, text="Add Task", command=add_task, fg='blue')
add_button.pack()

edit_button = tk.Button(root, text="Edit Task", command=edit_task, fg='blue')
edit_button.pack()

delete_button = tk.Button(root, text="Delete Task", command=delete_task, fg='red')
delete_button.pack()

toggle_status_button = tk.Button(root, text="Toggle Status", command=toggle_task_status, fg='green')
toggle_status_button.pack()

# Listbox to display tasks
listbox = tk.Listbox(root, width=70)
listbox.pack()

# Load tasks into the listbox when the app starts
tasks = load_tasks_from_file()
update_listbox()

root.mainloop()
