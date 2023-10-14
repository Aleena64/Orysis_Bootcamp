import tkinter as tk

window=tk.Tk()
window.title("GUI")
window.minsize(500, 100)

label1=tk.Label(text="Hello World", font=("Times New Roman", 20) )
label1.pack()

window.mainloop()