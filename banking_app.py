from tkinter import *
import os
from PIL import ImageTk,Image
import re

#Main screen
root = Tk()
root.title("Banking app")

#Functions
def add_deposit():
    global updated
    deposit_amount = d_amount.get()
    print(deposit_amount)
    print("add deposits")
    deposit_file = open(login_name+"_balance_update.txt", "r")
    dp = deposit_file.readlines()
    result_list = [word.split('R', 1)[-1] for word in dp if 'R' in word]

    bal = result_list[0]
    bal_fl =float(bal)
    deposit_amount = deposit_amount.replace(" ","").strip()
    print(deposit_amount)
    if deposit_amount.replace('.','',1).isdigit():
        deposit_amount = float(deposit_amount.strip())
        if deposit_amount >0 and deposit_amount%10 == 0:
            bal_fl += deposit_amount
            
            #Update the transactional log
            update_trans_log = open(login_name+"log",'a')
            update_trans_log.writelines(f"+R{deposit_amount}\n")
            
            updated = f"Balance = R{bal_fl}"
            print(updated)
            #Lets open the file to update the balance
            balance_file = open(login_name+"_balance_update.txt", "r")
            bf = balance_file.readlines()
            print("before")
            print(bf)
            #Deleting infor
            balance_file_update = open(login_name+"_balance_update.txt", "w")
            balance_file_update.write(updated)
            
            print(updated)
            balance_update_update.config(text=updated)

            deposit_notif.config(fg ="green", text="Success ")
            deposits_tk.destroy()
            
        else:
            deposit_notif.config(fg ="red", text="You can not deposit less than 0 or coins ")
            return
    else:
        deposit_notif.config(fg ="red", text="Invalid input")
        return
    # print(dp)
    # print(balance+deposit_amount)
         

def withdraw_func():
    print("Withdraw function success button")
    global updated
    withdraw_amount = w_amount.get()
    print(withdraw_amount)
    print("add deposits")
    deposit_file = open(login_name+"_balance_update.txt", "r")
    dp = deposit_file.readlines()
    result_list = [word.split('R', 1)[-1] for word in dp if 'R' in word]

    bal = result_list[0]
    bal_fl =float(bal)
    withdraw_amount = withdraw_amount.replace(" ","").strip()
    print(withdraw_amount)
    if withdraw_amount.replace('.','',1).isdigit():
        withdraw_amount = float(withdraw_amount.strip())
        if  0 < withdraw_amount < bal_fl: 
            if withdraw_amount%10 == 0:
                bal_fl -= withdraw_amount
                #Update the transactional log
                update_trans_log = open(login_name+"log",'a')
                update_trans_log.writelines(f"\n-R{withdraw_amount}\n")
                
                
                
                updated = f"Balance = R{bal_fl}"
                print(updated)
                #Lets open the file to update the balance
                balance_file = open(login_name+"_balance_update.txt", "r")
                bf = balance_file.readlines()
                print("before")
                print(bf)
                #Deleting infor
                balance_file_update = open(login_name+"_balance_update.txt", "w")
                balance_file_update.write(updated)
                
                print(updated)
                balance_update_update.config(text=updated)
                
                withdraw_notif.config(fg ="green", text="Success ")
                withdraw.destroy()
                
            else:
                withdraw_notif.config(fg ="red", text="You can not deposit coins ")
                return
        else:
            withdraw_notif.config(fg="red", text="Invalid Input")
            return
    else:
        withdraw_notif.config(fg ="red", text="Invalid input")
        return
    # print(dp)
    # print(balance+deposit_amount)
    
    
    
    
def deposits():
    global d_amount
    global deposit_notif
    global deposits_tk

    d_amount = StringVar()
    deposits_tk = Toplevel(root)
    deposits_tk.title(f"Deposits")
    
    
    Label(deposits_tk, text=f"Hi, {login_name}, lets deposit", font=("calibri",12)).grid(row=0,sticky=N,pady=10)
    Label(deposits_tk, text="R", font=("calibri",12)).grid(row=0,column=0,sticky=N,pady=10)
    
    Entry(deposits_tk,textvariable=d_amount).grid(row=2,column=1,padx=5,pady=15)
    Button(deposits_tk, text="Deposit", command=add_deposit, font=("calibri",12), width=16).grid(row= 3, sticky=W, pady = 5)
    
    deposit_notif = Label(deposits_tk, font=("calibri",12))
    deposit_notif.grid(row=4,sticky=N,pady=10)
    

def withdrawals():
    print("Withdraw")
    global w_amount
    global withdraw_notif
    global withdraw

    w_amount = StringVar()
    withdraw = Toplevel(root)
    withdraw.title(f"Deposits")
    
    
    Label(withdraw, text=f"Hi, {login_name}, lets withdraw", font=("calibri",12)).grid(row=0,sticky=N,pady=10)
    Label(withdraw, text="R", font=("calibri",12)).grid(row=2,column=0,sticky=N,pady=10)
    
    Entry(withdraw,textvariable=w_amount).grid(row=2,column=1,padx=5,pady=15)
    Button(withdraw, text="Withdraw", command=withdraw_func, font=("calibri",12), width=16).grid(row= 3, sticky=W, pady = 5)
    
    withdraw_notif = Label(withdraw, font=("calibri",12))
    withdraw_notif.grid(row=4,sticky=N,pady=10)

def transaction():
    global balance_update_transact
    print("Transaction log")
    trans_log_file = open(f"{login_name}log", "r")
    t_l_f = trans_log_file.read()
    print(t_l_f) 
    transact = Toplevel(root)
    transact.title(f"The Mint")
    
    user_file = open(login_name+"_balance_update.txt", "r+")
    current_balance = user_file.readlines()
    the_curent_bal = current_balance[0]
    print(the_curent_bal)
    
    
    
    Label(transact, text=f"Hi, {login_name}\nTransactional log", font=("calibri",12)).grid(row=0,sticky=N,pady=10)
    balance_update_update = Label(transact, text=the_curent_bal, font=("calibri",10))
    balance_update_update.grid(row=1,sticky=N,pady=10)
    Label(transact, text=t_l_f, font=("calibri",10)).grid(row=2,sticky=W,pady=10)


def investments():
    print("Investments")
    
def bond():
    print("Home loan")




def finish_reg():
    global amount
    amount      = int(0)
    name        = temp_name.get()#We use get() method to get an store
    id_number   = temp_id.get()
    gender      = temp_gender.get()
    password    = temp_password.get()
    all_accounts = os.listdir()
    print(all_accounts)
    name = name.replace(" ","").strip()
    id_number = id_number.replace(" ","").strip()
    password = password.replace(" ","").strip()
    
    if name== "" or id_number == "" or gender == "" or password =="":
        notif.config(fg ="red", text="All fields are required*")
        return

    pattern = re.compile(r'^(0[1-9]|[1-2][0-9]|3[0-1])(0[1-9]|1[0-2])(1920|19[2-9][0-9]|20[0-1][0-9]|202[0-3])$')
    if pattern.match(id_number):
        print("Valid date format.")
    
    else:
        print("Invalid date format.")
        return
    
    gender = gender.replace(" ","").strip()
    if gender.lower() != 'male' and gender.lower() != 'female' and gender.lower() != 'm' and gender.lower() != 'f':
        print("Gender must be either (male, female, m, f)")
        return
    else:
        print("gender success")
        
    for name_check in all_accounts:
        if name == name_check:
            notif.config(fg ="red", text="Account already exists")
            return
        else:
            new_file = open(f"{name}.txt","w")
            new_file_acc = open(f"{name}","w")
            statement = open(f"{name}_balance_update.txt","w")
            new_file.write(f"Name       : {name}\n")
            new_file.write(f"Password   : {password}\n")
            new_file_acc.write(password)
            statement.write(f"Balance = R{amount}")
            new_file.write(f"Age        : {id_number}\n")
            new_file.write(f"Gender     : {gender}\n")
            # new_file.write(f"Balance    : R0")
            new_file.close()
            # new_file_acc.close()
            
            log = open(name+"log","w")
            
       
            
            # notif.config(fg ="green", text="Account has been created succesfully")
            register_screen.destroy()
        
    
def register():
    #register vars
    
    global temp_name
    global temp_id
    global temp_gender
    global temp_password
    global notif
    global register_screen
    temp_name = StringVar()
    temp_id = StringVar()
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
    Label(register_screen, text="ID no.      ", font=("calibri",12)).grid(row=2,sticky=W)
    Label(register_screen, text="Gender   ", font=("calibri",12)).grid(row=3,sticky=W)
    Label(register_screen, text="password ", font=("calibri",12)).grid(row=4,sticky=W)
    notif = Label(register_screen, font=("calibri",12))
    notif.grid(row=6,sticky=N,pady=10)
    
    
    #Entries
    Entry(register_screen,textvariable=temp_name).grid(row=1,column=0,padx=70)#Relative padding
    Entry(register_screen,textvariable=temp_id).grid(row=2,column=0)
    Entry(register_screen,textvariable=temp_gender).grid(row=3,column=0)
    Entry(register_screen,textvariable=temp_password, show="*").grid(row=4,column=0)
    
    #register button
    Button(register_screen, text="Register", command=finish_reg, font=("calibri",12)).grid(row= 5, sticky=N, pady = 10)
    
def login_function():
    global login_name
    global balance_update_update
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
                
                #read the user data balance to display on the gui
                user_file = open(login_name+"_balance_update.txt", "r+")
                current_balance = user_file.readlines()
                the_curent_bal = current_balance[0]
                print(the_curent_bal)
                
                
                
                #Labels
                print(login_name)
                Label(account_dashboard, text="Account dashboard", font=("calibri",15)).grid(row=0,sticky=N,padx=10)
                balance_update_update = Label(account_dashboard, text =the_curent_bal , font=("calibri",12))
                balance_update_update.grid(row=1,sticky=N,padx=10)
                Label(account_dashboard, text = "Welcome", font=("calibri",12)).grid(row=2,sticky=N,padx=10)
                
                #Buttons
                Button(account_dashboard,text="Personal details", font=("calibri",12),width=30, command= personal_details).grid(row=3,sticky=N,padx=10)
                Button(account_dashboard,text="Deposit", font=("calibri",12),width=30,command=deposits).grid(row=4,sticky=N,padx=10)
                Button(account_dashboard,text="Withdraw" ,font=("calibri",12),width=30,command=withdrawals).grid(row=5,sticky=N,padx=10)
                Button(account_dashboard,text="Transaction log" ,font=("calibri",12),width=30,command=transaction).grid(row=6,sticky=N,padx=10)
                Button(account_dashboard,text="Investments" ,font=("calibri",12),width=30,command=investments).grid(row=7,sticky=N,padx=10)
                Button(account_dashboard,text="Home Loan" ,font=("calibri",12),width=30,command=bond).grid(row=8,sticky=N,padx=10)
                
                #
                Label(account_dashboard).grid(row=9,sticky=N,pady=10)
                return
            else:
                login_notif.config(fg ="red", text="Wrong password!*")
            
            return
        else:
            login_notif.config(fg ="red", text="Username/Acount does not exist*")
        
def personal_details():
    #variables 
    personal_det = open(f"{login_name}.txt", "r")
    pd = personal_det.read()
    print(pd) 
    Personal = Toplevel(root)
    Personal.title(f"The Mint")
    
    Label(Personal, text=f"Hi, {login_name}, Below is your details", font=("calibri",12)).grid(row=0,sticky=N,pady=10)
    Label(Personal, text=pd, font=("calibri",10)).grid(row=1,sticky=N,pady=10)


    
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