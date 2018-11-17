from Tkinter import *
import pygame
from random import *
score=0
timeleft=30
root=Tk()
def startGame(event):

    
    if timeleft == 30:
        
        countdown()
          
def event1(event):
    print("{},{}".format(event.x,event.y))

def jump(event):
    mygame.abc.place(relx=random(),rely=random())

def countdown():
    

    
    global timeleft
    if timeleft > 0:
        
        timeleft -= 1
        label2.config(text="Time left: " + str(timeleft))
        label2.after(1000, countdown)
         

class mygame:
    def __init__(self,master):
        frame = Frame(master)
        master.geometry("555x444")
        master.title("Fun Game")
        master.bind("<Button-1>",event1)
        master.bind("<Button-1>",event1)
        frame.pack()

        self.abc = Button(master,text="PRESS ME",command=sys.exit,bg="Green")
        self.abc.bind("<Enter>",jump)
        self.abc.pack()



label1 = Label(root, text="Score:0", font=('Bold', 20))
label1.pack()
label2 = Label(root, text="Time left: " + str(timeleft), font=('Bold', 20))
label2.pack()
label3 = Label(root, font=('Bold', 80))
label3.pack()
mygame = mygame(root)
root.bind('<Return>', startGame)
root.mainloop()
