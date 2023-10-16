import tkinter as tk

def add_a_task():
    task=entry.get()
    if task:
        listbox.insert("end",task)
        listbox.delete(0,"end")
    else:
        print("WARNING: Please enter a task")
def remove_a_task():
     task1=listbox.curselection()
     listbox.delete(task1)

window = tk.Tk()
window.title("To-do-list")
window.minsize(400,300)

entry=tk.Entry(width=30)
entry.grid=(row=0, column=0, padx=20, pady=10 )

button1=tk.Button(text="Add a task", command=add_a_task)
button1.grid=(row=0, column=1, padx=20, pady=10 )

button2=tk.Button(text="Remove a Task", command=remove_a_task)
button2.grid=(row=1, column=1, padx=20, pady=10 )

listbox=tk.Listbox(selectmode=tk.single, width=40)
listbox.grid=(row=2, column=1, columnspan=1, padx=20, pady=10)

window.mainloop()