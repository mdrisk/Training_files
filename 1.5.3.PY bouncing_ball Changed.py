#####
# bouncing_ball.py
# 
# Creates a Scale and a Canvas. Animates a circle based on the Scale
# (c) 2013 PLTW
# version 11/1/2013
####

import Tkinter #often people import Tkinter as *

#####
# Create root window 
####
root = Tkinter.Tk()

#####
# Create Model
######
# Initialize y coordinate
# radius and x-coordinate of circle
hearts = 3
score = 0
r = 100
x = 150
y = 150
ball_speed = 1
direction = 0.5 # radians of angle in standard position, ccw from positive x axis
 
######
# Create Controller
#######
# Instantiate and place slider
'''speed_slider = Tkinter.Scale(root, from_=5, to=1, variable=speed_intvar,    
                              label='speed')
speed_slider.grid(row=1, column=0, sticky=Tkinter.W)
# Create and place directions for the user
text = Tkinter.Label(root, text='Drag slider \nto adjust\nspeed.')
text.grid(row=0, column =0)
'''
######
# Create View
#######
# Create and place a canvas
canvas = Tkinter.Canvas(root, width=600, height=600, background='#FFFFFF')
canvas.grid(row=0, rowspan=2, column=0)

# Create a circle on the canvas to match the initial model
circle_item = canvas.create_oval(x-r, y-r, x+r, y+r, 
                                 outline='#000000', fill='#00FFFF')
import math
def animate():
    global direction
    # Get the slider data and create x- and y-components of velocity
    velocity_x = ball_speed * math.cos(direction) # adj = hyp*cos()
    velocity_y = ball_speed * math.sin(direction) # opp = hyp*sin()
    # Change the canvas item's coordinates
    canvas.move(circle_item, velocity_x, velocity_y)
    
    # Get the new coordinates and act accordingly if ball is at an edge
    x1, y1, x2, y2 = canvas.coords(circle_item)
    
    # If crossing left or right of canvas
    if x2>canvas.winfo_width() or x1<0: 
        direction = math.pi - direction # Reverse the x-component of velocity
    # If crossing top or bottom of canvas
    if y2>canvas.winfo_height() or y1<0: 
        direction = -1 * direction # Reverse the y-component of velocity
    
    # Create an event in 1 msec that will be handled by animate(),
    # causing recursion        
    canvas.after(2, animate)
# Call function directly to start the recursion
animate()



def increase_speed():
    global ball_speed
    ball_speed +=1
    
def decrease_ball_size():
    global r
    r-=10
    a,b,c,d = canvas.coords(circle_item)
    x = (a+c)/2
    y = (b+d)/2
    canvas.coords(circle_item, x-r, y-r, x+r, y+r) 
 

def miss():
    '''
    This is called when the mouse click is not within the circle area.
    '''
    global hearts
    if hearts > 1:
        hearts -= 1
    else:
        end()
        
def end():
    '''
    This is the function called when the game ends.
    '''
    canvas.itemconfig(circle_item, state = "hidden")
    words = canvas.create_text(300, 275, font="Times 20 italic bold", text = "Game Over")
    temptext = "Score was : " + str(score)
    scoretext = canvas.create_text(300, 375,font="Times 20 italic bold", text = temptext)
    b1['state'] = 'normal'


def down(event):
    '''
    This is the event handler for the mouse click where the event X,Y is compared
    to the bouding box Xs and Ys of the circle.
    '''
    global score
    a,b,c,d = canvas.coords(circle_item)
    if event.x > a and event.x < c:
        if event.y > b and event.y < d:
            increase_speed()
            decrease_ball_size()
            score +=1
        else:
            miss()
    else:
        miss()
        
def reset():
    global circle_item, ball_speed, score, hearts, r
    r = 100
    hearts = 3
    ball_speed = 1
    score = 0
    canvas.delete("all")
    circle_item = canvas.create_oval(x-r, y-r, x+r, y+r, 
                                 outline='#000000', fill='#00FFFF')
    
    
    b1['state'] = 'disabled'
    animate()



b1 = Tkinter.Button(root, text = "Play again?", width = 10, state = "disabled", command = reset)
b1.grid(row=3, column = 0)


#binding the mouse button one

canvas.bind('<Button-1>', down)


#######
# Event Loop
#######
root.mainloop()