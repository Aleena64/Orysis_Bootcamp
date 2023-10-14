import tkinter as tk

def m_to_km():
    n=float(a_entry.get())
    km=n*1.60934
    c_label.config(text="{n} miles = {km} kilometers")
window=tk.Tk()
window.title("Miles to Kilometer Conversion")
window.minsize(1000, 500)

a_label=tk.Label(text = 'Enter Miles', font=('Times New Roman',20))
a_entry=tk.Entry(window)
a_label.grid(row=0, column=0)
a_entry.grid(row=0, column=1)

b_button=tk.Button(text ="Convert", command=m_to_km)
b_button.grid(row=1, column=0)
b_button.pack()

c_label=tk.Label(text="Result")
c_label.grid(row=2, column=0)

window.mainloop()