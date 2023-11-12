from tkinter import *
import os
from PIL import ImageTk,Image

#Main screen
root = Tk()
root.title("Banking app")

#Functions
def finish_reg():
    name = temp_name.get()#We use get() method to get an store
    age = temp_age.get()
    gender = temp_gender.get()
    password = temp_password.get()
    all_accounts = os.listdir()
    print(all_accounts)
    
    if name== "" or age == "" or gender == "" or password =="":
        notif.config(fg ="red", text="All fields are required*")
        return

    for name_check in all_accounts:
        if name == name_check:
            notif.config(fg ="red", text="Account already exists")
            return
        else:
            new_file = open(name,"w")
            new_file.write(f"Name       : {name}\n")
            new_file.write(f"Password   : {password} \n")
            new_file.write(f"Age        : {age}\n")
            new_file.write(f"Gender     : {gender}\n")
            new_file.close()
            notif.config(fg ="green", text="Account has been created succesfully")
        
    
def register():
    #register vars
    global temp_name
    global temp_age
    global temp_gender
    global temp_password
    global notif
    temp_name = StringVar()
    temp_age = StringVar()
    temp_gender = StringVar()
    temp_password = StringVar()
    '''
    Creates a popup 
    window when you 
    press register button
    '''
    register_screen = Toplevel(root)
    
    register_screen.title("Register")
    #Labels
    Label(register_screen, text="Enter your details to register", font=("calibri",12)).grid(row=0,sticky=N,pady=10)
    Label(register_screen, text="Name     ", font=("calibri",12)).grid(row=1,sticky=W)
    Label(register_screen, text="Age      ", font=("calibri",12)).grid(row=2,sticky=W)
    Label(register_screen, text="Gender   ", font=("calibri",12)).grid(row=3,sticky=W)
    Label(register_screen, text="password ", font=("calibri",12)).grid(row=4,sticky=W)
    notif = Label(register_screen, font=("calibri",12))
    notif.grid(row=6,sticky=N,pady=10)
    
    
    #Entries
    Entry(register_screen,textvariable=temp_name).grid(row=1,column=0,padx=70)#Relative padding
    Entry(register_screen,textvariable=temp_age).grid(row=2,column=0)
    Entry(register_screen,textvariable=temp_gender).grid(row=3,column=0)
    Entry(register_screen,textvariable=temp_password, show="*").grid(row=4,column=0)
    
    #register button
    Button(register_screen, text="Register", command=finish_reg, font=("calibri",12)).grid(row= 5, sticky=N, pady = 10)
    
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

