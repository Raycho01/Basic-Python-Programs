from tkinter import *
from PIL import ImageTk, Image

root=Tk()

image = Image.open("C:/Users/raich/Documents/Stuff/best memories/04.12 (2).jpg")
# The (450, 350) is (height, width)
image = image.resize((450, 350), Image.ANTIALIAS)
my_img = ImageTk.PhotoImage(image)
my_img = Label(image = my_img)
my_img.grid(row = 0, column = 0)

root.mainloop()