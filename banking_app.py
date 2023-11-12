from tkinter import *
import os
from PIL import ImageTk,Image

#Main screen
root = Tk()
root.title("Banking app")

#Functions
def register():
    '''
    Creates a popup 
    window when you 
    press register button
    '''
    register_screen = Toplevel(root)
    register_screen.title("Register")
    #Labels
    Label(register_screen, text="Enter your details to register", font=("calibri",12)).grid(row=0,sticky=N,pady=10)
    Label(register_screen, text="Name", font=("calibri",12)).grid(row=1,sticky=W,pady=10)
    Label(register_screen, text="Age", font=("calibri",12)).grid(row=2,sticky=W,pady=10)
    Label(register_screen, text="Gender", font=("calibri",12)).grid(row=3,sticky=W,pady=10)
    Label(register_screen, text="password", font=("calibri",12)).grid(row=4,sticky=W,pady=10)
    
def login():
    print("This is a login page")

#Image import
img = Image.open('Logo.png')
img = img.resize((150,150))
img = ImageTk.PhotoImage(img)

#Labels
Label(root, text ="Custom Banking betta", font=("arial",14)).grid(row=0,sticky=N,pady=10)
Label(root, text ="The most secure bank, CI solutions", font=("arial",14)).grid(row=1,sticky=N)

#Label image
Label(root,image=img).grid(row=2,sticky=N,pady=15)

#buttons
Button(root, text="Register", font=("calibri",12),width=20, command=register).grid(row=3,sticky=N)
Button(root, text="Login", font=("calibri",12),width=20, command=login).grid(row=4,sticky=N,pady = 5)


root.mainloop()

