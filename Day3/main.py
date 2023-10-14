import tkinter

def print_hello():
    print("Helooo")
    label1["text"]="Hey"
window=tkinter.Tk()
window.title("My first GUI application")

window.minsize(500, 420)


#500-width, 420-height
#0,0 default size
label=tkinter.Label(text="This is my first GUI application")
label.pack(side="bottom")

label1=tkinter.Label(text="This is my first GUI application", font=("Times New Roman", 24) )
label1.pack()
#label1["text"]="Hey"
#label1.place(x=10, y=50)
button=tkinter.Button(text="Click me", command=print_hello)
button.pack()
#pack: helps to create a layout.

window.mainloop()