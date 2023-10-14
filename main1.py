import tkinter as tk

def print_hi():
    label2.config(text=name.get())
window=tk.Tk()
window.minsize(1000, 500)
name=tk.StringVar()
label1 = tk.Label(text = 'Enter your name', font=('Times New Roman',20))
label1.pack()
input_element=tk.Entry(textvariable=name)
input_element.pack()
button=tk.Button(text="submit", command=print_hi)
button.pack()
label2=tk.Label(text = 'name', font=('Times New Roman',20))
label2.pack(side="bottom")

window.mainloop()