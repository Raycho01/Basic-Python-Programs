from tkinter import *
from PIL import ImageTk, Image



root = Tk()
root.title("Album of my love.")

#root.iconbitmap("adress_of_icon")

image_1 = ImageTk.PhotoImage(Image.open("C:/Users/raich/Documents/Stuff/best memories/04.12 (2).jpg"))
image_2 = ImageTk.PhotoImage(Image.open("C:/Users/raich/Documents/Stuff/best memories/04.12 (1).jpg"))
image_3 = ImageTk.PhotoImage(Image.open("C:/Users/raich/Documents/Stuff/best memories/06.12 (1).jpg"))
image_4 = ImageTk.PhotoImage(Image.open("C:/Users/raich/Documents/Stuff/best memories/27.11.jpg"))
image_5 = ImageTk.PhotoImage(Image.open("C:/Users/raich/Documents/Stuff/best memories/10.12 (2).jpg"))

image_list = [image_1, image_2, image_3, image_4, image_5]

label_1 = Label(image = image_list[0])
label_1.grid(row = 2, column = 0, columnspan = 3)

status = Label(root, text = "Image 1 of " + str(len(image_list)), bd = 1, relief = SUNKEN)
status.grid(row = 0, column = 3, columnspan = 3, sticky = W+E, pady = 2)



def backPic(image):
    global label_1
    global button_forward
    global button_back

    label_1.grid_forget()
    label_1 = Label(image = image_list[image])
    label_1.grid(row = 2, column = 0,  columnspan = 3)

    status = Label(root, text="Image " + str(image + 1) + " of " + str(len(image_list)), bd = 1, relief = SUNKEN)
    status.grid(row = 0, column = 3, columnspan = 3, sticky = W, pady = 2)

    button_forward = Button(root, text=">>", padx = 30, pady = 5, command=lambda: nextPic(image + 1))
    button_forward.grid(row = 1, column = 2)

    if image < 1:
        button_back = Button(root, text = "<<", padx = 30, pady = 5, state = DISABLED)
        button_back.grid(row = 1, column = 0)
    else:
        button_back = Button(root, text = "<<", padx = 30, pady = 5, command = lambda: backPic(image - 1))
        button_back.grid(row = 1, column = 0)



def nextPic(image):
    global label_1
    global button_forward
    global button_back

    label_1.grid_forget()
    label_1 = Label(image = image_list[image])
    label_1.grid(row = 2, column = 0, columnspan = 3)

    image = image + 1

    status = Label(root, text = "Image " + str(image) + " of " + str(len(image_list)), bd = 1, relief = SUNKEN)
    status.grid(row = 0, column = 3, columnspan = 3, sticky = W+E, pady = 2)

    if image == 5:
        button_back = Button(root, text="<<", padx = 30, pady = 5, command = lambda: backPic(image - 2))
        button_back.grid(row=1, column=0)

    if image > 4:
        button_forward = Button(root, text = ">>", padx = 30, pady = 5, state = DISABLED)
        button_forward.grid(row = 1, column = 2)
    else:
        if image < 1:
            button_back = Button(root, text = "<<", padx = 30, pady = 5, state = DISABLED)
            button_back.grid(row = 1, column = 0)
        else:
            button_back = Button(root, text = "<<", padx = 30, pady = 5, command = lambda: backPic(image - 2))
            button_back.grid(row = 1, column = 0)

        button_forward = Button(root, text = ">>", padx = 30, pady = 5, command = lambda: nextPic(image))
        button_forward.grid(row = 1, column = 2)



button_quit = Button(root, text = "Exit", padx = 30, pady = 5, command = root.quit)
button_back = Button(root, text = "<<", padx = 30, pady = 5, state = DISABLED)
button_forward = Button(root, text = ">>", padx = 30, pady = 5, command = lambda: nextPic(1))

button_back.grid(row = 1, column = 0)
button_quit.grid(row = 1, column = 1)
button_forward.grid(row = 1, column = 2)

root.mainloop()