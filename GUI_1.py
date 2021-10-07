from tkinter import *

root = Tk()

def nameEnter():
    label_2 = Label(root, text = "Hello, " +entry_1.get())
    label_2.pack()

label_1 = Label(root, text = "What's your name ?")
label_1.pack()

entry_1 = Entry(root, width = 50)
entry_1.insert(0, "Enter Your Name Here")
entry_1.pack()

button_1 = Button(root, text = "Enter", command = nameEnter)
button_1.pack()

root.mainloop()