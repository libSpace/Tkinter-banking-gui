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
            new_file = open(f"{name}.txt","w")
            new_file_acc = open(f"{name}","w")
            new_file.write(f"Name       : {name}\n")
            new_file.write(f"Password   : {password} \n")
            new_file_acc.write(password)
            new_file.write(f"Age        : {age}\n")
            new_file.write(f"Gender     : {gender}\n")
            new_file.write(f"Balance    : R0")
            new_file.close()
            # new_file_acc.close()
            
            notif.config(fg ="green", text="Account has been created succesfully")
            register_screen.destroy()
        
    
def register():
    #register vars
    global temp_name
    global temp_age
    global temp_gender
    global temp_password
    global notif
    global register_screen
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
    
def login_function():
    all_accounts = os.listdir()
    print(all_accounts)
    
    login_name = temp_login_name.get()
    login_password = temp_login_password.get()
    if login_name =="" or login_password =="":
        login_notif.config(fg ="red", text="All fields are required*")
        return
          
    for username in all_accounts:
        if login_name+".txt" == username:
            print("success for login name")
            file = open(f"{login_name}.txt", "r")
            file_security = open(login_name,"r")
            file_data=file.read()
            file_data.split("\n")
            file_security_data =file_security.read().split()
            user_password = file_security_data[0]
            
            
        
            #account dash
            if login_password == user_password:
                login_notif.config(fg ="green", text="Successfully logged in")
                login_screen.destroy()
                account_dashboard = Toplevel(root)
                account_dashboard.title("Dashboard")
                
                #Labels
                Label(account_dashboard, text="Account dashboard", font=("calibri",15)).grid(row=0,sticky=N,padx=10)
                Label(account_dashboard, text="Welcome\n"+login_name, font=("calibri",12)).grid(row=1,sticky=N,padx=10)
                
                #Buttons
                Button(account_dashboard,text="Personal details", font=("calibri",12),width=30).grid(row=2,sticky=N,padx=10)
                Button(account_dashboard,text="Deposit", font=("calibri",12),width=30).grid(row=3,sticky=N,padx=10)
                Button(account_dashboard,text="Withdraw", font=("calibri",12),width=30).grid(row=4,sticky=N,padx=10)
                
                #
                Label(account_dashboard).grid(row=5,sticky=N,pady=10)
                return
            else:
                login_notif.config(fg ="red", text="Wrong password!*")
            
            return
        else:
            login_notif.config(fg ="red", text="Username/Acount does not exist*")
    
    
def login():
    #Vars
    global temp_login_name
    global temp_login_password
    global login_notif
    global login_screen
    temp_login_name = StringVar()
    temp_login_password = StringVar()
    #Login screen
    login_screen = Toplevel(root)
    login_screen.title("Login")
    #Labels
    Label(login_screen, text="Login to your account", font=("calibri",12)).grid(row=0,sticky=N,pady=10)
    Label(login_screen, text="Username     ", font=("calibri",12)).grid(row=1,sticky=W)
    Label(login_screen, text="password ", font=("calibri",12)).grid(row=2,sticky=W)
    login_notif = Label(login_screen, font=("calibri",12))
    login_notif.grid(row=4,sticky=N,pady=10)
    
    
    #Entries
    Entry(login_screen,textvariable=temp_login_name).grid(row=1,column=1,padx=5)#Relative padding
    Entry(login_screen,textvariable=temp_login_password, show="*").grid(row=2,column=1)
    
    #register button
    Button(login_screen, text="Login", command=login_function, font=("calibri",12), width=16).grid(row= 3, sticky=W, pady = 5)
    
    

#Image import
img = Image.open('Logo.png')
img = img.resize((150,150))
img = ImageTk.PhotoImage(img)

#Labels
Label(root, text ="Creative Innovators Bank", font=("arial",14)).grid(row=0,sticky=N,pady=10)
Label(root, text ="The Mint", font=("arial",10)).grid(row=1,sticky=N)

#Label image
Label(root,image=img).grid(row=2,sticky=N,pady=15)

#buttons
Button(root, text="Register", font=("calibri",12),width=20, command=register).grid(row=3,sticky=N)
Button(root, text="Login", font=("calibri",12),width=20, command=login).grid(row=4,sticky=N,pady = 5)


root.mainloop()