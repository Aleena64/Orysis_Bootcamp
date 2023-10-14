import tkinter as tk

def print_hi():
    n=int(square_value.get())
    sq=n*n
    label2=tk.Label(text=sq, font=('Times New Roman',20))
    label2.pack(side="bottom")
window=tk.Tk()
window.minsize(1000, 500)
square_value=tk.StringVar()
label1 = tk.Label(text = 'Enter a number', font=('Times New Roman',20))
label1.pack()
input_element=tk.Entry(textvariable=square_value)
input_element.pack()
button=tk.Button(text="submit", command=print_hi)
button.pack()


window.mainloop()