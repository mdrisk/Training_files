from Tkinter import *

root = Tk()
root.title("Ice-Cream Delight")



def change():
    canvas.itemconfig(ice, fill = "SpringGreen2")
    canvas.itemconfig(words, text = "Mint Chocolate")

def change2():
    canvas.itemconfig(ice, fill = "pink")
    canvas.itemconfig(words, text = "Strawberry")

def change3():
    canvas.itemconfig(ice, fill = "red")
    canvas.itemconfig(words, text = "Cherry Sorbet")

canvas = Canvas(root, width = 500, height = 500, bg = "white")
canvas.grid(row = 0, column = 0, columnspan = 3, rowspan = 10)

ice = canvas.create_oval(175,150,325,300, fill = "pink")
canvas.create_polygon(190,270,310,270,250,450, fill = "tan", outline = "black")

b1 = Button(root, width = 10, bg = "SpringGreen2", command = change)
b1.grid(row = 0, column = 0)

b2 = Button(root, width = 10, bg = "pink", command = change2)
b2.grid(row = 0, column = 1)

b3 = Button(root, width = 10, bg = "red", command = change3)
b3.grid(row = 0, column = 2)

words = canvas.create_text(250, 475, text = "Strawberry")
root.mainloop()