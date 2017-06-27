from Tkinter import *
 
root = Tk()
 
def wink():
    if var.get() == 0: 
        canvas.itemconfig(eye2, state = "hidden")
        canvas.itemconfig(ineye2, state = "hidden")
        canvas.itemconfig(winky, state = "normal")
    else:
        canvas.itemconfig(eye2, state = "normal")
        canvas.itemconfig(ineye2, state = "normal")
        canvas.itemconfig(winky, state = "hidden") 
    
    
canvas = Canvas(root, width = 500, height = 500, bg = 'red')
canvas.grid(row = 0,column = 0)

eye = canvas.create_oval(100, 100, 150, 150, fill = 'black')
ineye = canvas.create_oval(130, 130, 145, 145, fill = 'white')
eye2 = canvas.create_oval(350, 100, 400, 150, fill = 'black')
ineye2 = canvas.create_oval(380, 130, 395, 145, fill = 'white')
nose = canvas.create_polygon(250, 200, 200, 250, 300, 250, 250, 200, fill = 'black') 
mouth = canvas.create_arc( 0, 50, 500, 450, start=210, extent=120, width=25, style="arc")
hair = canvas.create_arc( 0, 50, 500, 250, start=0, extent=180, width=45, outline = 'white', style = "arc")
winky = canvas.create_arc(350, 100, 400, 150, start = 210, extent = 120, width = 10, outline = 'black', style = 'arc', state = "hidden")
var = IntVar()
check = Checkbutton(root, text="Wink", variable=var,onvalue=1, offvalue=0, command = wink)
check.grid(row = 0, column = 2)
 
 
 
root.mainloop()
