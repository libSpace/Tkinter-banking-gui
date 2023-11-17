from tkinter import *
import os
from PIL import ImageTk,Image
import re
import random
import secrets
import string
import math

#Main screen
root = Tk()
root.title("Banking app")

#Functions



def generate_random_password():
    global rand_password
    # Generate 3 random special characters
    special_chars = ''.join(secrets.choice(string.punctuation.replace(' ', '')) for _ in range(4))

    # Generate 4 random alphabets (excluding spaces)
    alphabets = ''.join(secrets.choice(string.ascii_letters.replace(' ', '')) for _ in range(4))

    # Generate 3 random numbers
    numbers = ''.join(secrets.choice(string.digits) for _ in range(4))

    # Combine the three components to create the final password
    password = special_chars + alphabets + numbers

    # Shuffle the password to make it more secure
    password_list = list(password)
    secrets.SystemRandom().shuffle(password_list)
    rand_password = ''.join(password_list)
    notif.config(fg="black", text=rand_password)
    


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
            update_trans_log.writelines(f"Deposit: +R{deposit_amount}\n")
            
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
                update_trans_log.writelines(f"Withdraw: -R{withdraw_amount}\n")
                
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
                withdraw_notif.config(fg ="red", text="You can not withdraw coins ")
                return
        else:
            withdraw_notif.config(fg="red", text="Insufficient funds")
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
    Label(deposits_tk, text="R", font=("calibri",12)).grid(row=1,column=0,sticky=N,pady=10)
    
    Entry(deposits_tk,textvariable=d_amount).grid(row=1,column=1,padx=5,pady=15)
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

def comp_years():
    
    principal1 = invest_p.get()
    rate1 = invest_r.get()
    time1 = invest_t.get()
    
    principal = principal1.replace(" ","").strip()
    rate = rate1.replace(" ","").strip()
    time = time1.replace(" ","").strip()
   
    if principal =="" and rate =='' and time =='':
        inve_notif.config(fg='red',text='All fields are required')
    else:
        print(principal)
        print(rate)
        print(time)
        if principal.replace('.','',1).isdigit() and rate.replace('.','',1).isdigit and time.replace('.','',1).isdigit():
                    
            time = float(time.replace(".",'',1).strip())
            rate=float(rate.replace(".",'',1).strip())
            principal=float(principal.replace(".",'',1).strip())
            if principal > 0 and rate > 0 and time >0:
                print('we still good')
                rate = rate/100
                value = principal*(1+rate)**(time)
                inve_notif.config(fg="red", text=f"Future vale = R{value:.2f}")
            else:
                inve_notif.config(fg="red", text="Positive values")
        else:
            inve_notif.config(fg="red", text="Invalid input!")

def comp_months():
    
    principal1 = invest_p.get()
    rate1 = invest_r.get()
    time1 = invest_t.get()
    
    principal = principal1.replace(" ","").strip()
    rate = rate1.replace(" ","").strip()
    time = time1.replace(" ","").strip()
    
    if principal =="" and rate =='' and time =='':
        inve_notif.config(fg='red',text='All fields are required')
    else:
        print(principal)
        print(rate)
        print(time)
        if principal.replace('.','',1).isdigit() and rate.replace('.','',1).isdigit and time.replace('.','',1).isdigit():
                    
            time = float(time.replace(".",'',1).strip())
            rate=float(rate.replace(".",'',1).strip())
            principal=float(principal.replace(".",'',1).strip())
            if principal > 0 and rate > 0 and time >0:
                print('we still good')
                rate = rate/100
                time = time/12
                value = principal*(1+rate)**(time)
                inve_notif.config(fg="red", text=f"Future vale = R{value:.2f}")
                inve_notif.config(fg="green", text="good")
            else:
                inve_notif.config(fg="red", text="Positive values")
        else:
            inve_notif.config(fg="red", text="Invalid input!")
    
    
    
def simp_months(): 
   
    principal1 = invest_p.get()
    rate1 = invest_r.get()
    time1 = invest_t.get()
    
    principal = principal1.replace(" ","").strip()
    rate = rate1.replace(" ","").strip()
    time = time1.replace(" ","").strip()
    
    if principal =="" and rate =='' and time =='':
        inve_notif.config(fg='red',text='All fields are required')
    else:
        print(principal)
        print(rate)
        print(time)
        if principal.replace('.','',1).isdigit() and rate.replace('.','',1).isdigit and time.replace('.','',1).isdigit():
                    
            time = float(time.replace(".",'',1).strip())
            rate=float(rate.replace(".",'',1).strip())
            principal=float(principal.replace(".",'',1).strip())
            if principal > 0 and rate > 0 and time >0:
                print('we still good')
                rate = rate/100
                time = time/12
                value = principal*(1+rate*time)
                inve_notif.config(fg="red", text=f"Future vale = R{value:.2f}")
                inve_notif.config(fg="green", text="good")
            else:
                inve_notif.config(fg="red", text="Positive values")
        else:
            inve_notif.config(fg="red", text="Invalid input!")
            
def logout():
    account_dashboard.destroy()
    
def simp_years():
    
    principal1 = invest_p.get()
    rate1 = invest_r.get()
    time1 = invest_t.get()
    
    principal = principal1.replace(" ","").strip()
    rate = rate1.replace(" ","").strip()
    time = time1.replace(" ","").strip()

    
    if principal =="" and rate =='' and time =='':
        inve_notif.config(fg='red',text='All fields are required')
        return
    else:
        print(principal)
        print(rate)
        print(time)
        if principal.replace('.','',1).isdigit() and rate.replace('.','',1).isdigit and time.isdigit():
            principal = float(principal)
            rate = float(rate)
            time = float(time)
            if principal > 0 and rate > 0 and time >0:
                print('we still good')
                rate = rate/100
                value = principal*(1+rate*time)
                inve_notif.config(fg="red", text=f"Future vale = R{value:.2f}")
                inve_notif.config(fg='green',text='simp year good')
            else:
                inve_notif.config(fg="red", text="Positive values")
                return
        else:
            inve_notif.config(fg="red", text="Invalid input!")
            return

    print("simp in years")
    
    
    

    
    
    
    
def investments():
    #Global vars
    global invest_p
    global invest_r
    global invest_t
    global inve_notif
    #variabkes
    invest_p = StringVar()
    invest_r = StringVar()
    invest_t = StringVar()
    
    
    invest_widget = Toplevel(root)
    invest_widget.title("Investment Calculator")
    
    Label(invest_widget, text="Invesment Dashboard").pack()
    
    Label(invest_widget, text="Principal Amount").pack()
    Entry(invest_widget,text = invest_p).pack()
    
    Label(invest_widget, text="rate (i)").pack()
    Entry(invest_widget,text = invest_r).pack()
    
    Label(invest_widget, text="time").pack()
    Entry(invest_widget,text = invest_t).pack()
    Label(invest_widget, text="").pack()
    inve_notif = Label(invest_widget)
    inve_notif.pack()
    
    #Buttons
    Button(invest_widget, text="Compound Interest(time in years)" , command=comp_years, font=("calibri",12),width=30).pack()
    Button(invest_widget, text="Compound Interest(time in months)", command=comp_months, font=("calibri",12),width=30).pack()
    Button(invest_widget, text="simple Interest(time in months)" , command=simp_months, font=("calibri",12),width=30).pack()
    Button(invest_widget, text="simple interest(time in years)", command=simp_years, font=("calibri",12),width=30).pack()
    print("Investments")



def bond():
    #Global vars
    global bond_p
    global bond_r
    global bond_t
    global bond_notif
    global bond_widget
    #variabkes
    bond_p = StringVar()
    bond_r = StringVar()
    bond_t = StringVar()
    
    
    bond_widget = Toplevel(root)
    bond_widget.title("Investment Calculator")
    
    Label(bond_widget, text="Invesment Dashboard").pack()
    
    Label(bond_widget, text="Principal Amount").pack()
    Entry(bond_widget,text = bond_p).pack()
    
    Label(bond_widget, text="rate (i)").pack()
    Entry(bond_widget,text = bond_r).pack()
    
    Label(bond_widget, text="time").pack()
    Entry(bond_widget,text = bond_t).pack()
    Label(bond_widget, text="").pack()
    bond_notif = Label(bond_widget)
    bond_notif.pack()
    
    #Buttons
    Button(bond_widget, text="Calculate(time in years)" , command=calc, font=("calibri",12),width=30).pack()
    Button(bond_widget, text="Calculate(time in months)", command=calc_months, font=("calibri",12),width=30).pack()
    Button(bond_widget, text="exit" , command=exit_bond, font=("calibri",12),width=30).pack()
   
    print("Bond")   
    
def exit_bond():
    bond_widget.destroy()
     
def calc():
    principal1 = bond_p.get()
    rate1 = bond_r.get()
    time1 = bond_t.get()
    
    principal = principal1.replace(" ","").strip()
    rate = rate1.replace(" ","").strip()
    time = time1.replace(" ","").strip()
   
    if principal =="" and rate =='' and time =='':
        bond_notif.config(fg='red',text='All fields are required')
    else:
        print(principal)
        print(rate)
        print(time)
        if principal.replace('.','',1).isdigit() and rate.replace('.','',1).isdigit and time.replace('.','',1).isdigit():
                    
            time = float(time)
            rate=float(rate)
            principal=float(principal)
            if principal > 0 and rate > 0 and time >0:
                if time <= 100:
                    print('we still good')
                    rate = rate/1200
                    time = time*12
                    monthly_payment = (rate * principal) / (1 - math.pow((1 + rate),-time))
                    bond_notif.config(fg="green", text=f"Monthly payment would = R{monthly_payment:.2f}")
                else:
                    bond_notif.config(fg="red", text="Interest rate cant be more than 100%")
            else:
                bond_notif.config(fg="red", text="Positive values")
        else:
            bond_notif.config(fg="red", text="Invalid input!")
    print("Home loan")
def calc_months():
    principal1 = bond_p.get()
    rate1 = bond_r.get()
    time1 = bond_t.get()
    
    principal = principal1.replace(" ","").strip()
    rate = rate1.replace(" ","").strip()
    time = time1.replace(" ","").strip()
   
    if principal =="" and rate =='' and time =='':
        bond_notif.config(fg='red',text='All fields are required')
    else:
       
        if principal.replace('.','',1).isdigit() and rate.replace('.','',1).isdigit and time.replace('.','',1).isdigit():
                    
            time = float(time)
            rate=float(rate)
            principal=float(principal)
            if principal > 0 and rate > 0 and time >0:
                if time <= 100:
                    print('we still good')
                    rate = rate/1200
                    monthly_payment = (rate * principal) / (1 - math.pow((1 + rate),-time))
                    bond_notif.config(fg="green", text=f"Monthly payment would = R{monthly_payment:.2f}")
                else:
                    bond_notif.config(fg="red", text="Interest rate cant be more than 100%")
            else:
                bond_notif.config(fg="red", text="Positive values")
        else:
            bond_notif.config(fg="red", text="Invalid input!")
    print("Home loan")



def finish_reg():
    
    global pop_up
    
    # Generate a random 7-digit number
    random_middle_part = str(random.randint(1000000, 9999999))

    # Concatenate the parts to form a 9-digit number
    random_9_digit_number = "9" + random_middle_part + "2"

    print(random_9_digit_number)
    
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
        err_notif.config(fg ="red", text="All fields are required*")
        return
    if not name.isalpha():
        err_notif.config(fg ="red", text="Invalid name*")
        return
    pattern = re.compile(r'^(0[1-9]|[1-2][0-9]|3[0-1])(0[1-9]|1[0-2])(1920|19[2-9][0-9]|20[0-1][0-9]|202[0-3])$')
    if pattern.match(id_number):
        print("Valid ID format.")
    
    else:
        print("Invalid ID format.")
        err_notif.config(fg="red", text="Invalid ID(ddmmyyyy)")
        return
    
    gender = gender.replace(" ","").strip()
    if gender.lower() != 'male' and gender.lower() != 'female' and gender.lower() != 'm' and gender.lower() != 'f':
        print("Gender must be either (male, female, m, f)")
        err_notif.config(fg='red',text='Gender must be either (male, female, m, f)')
        return
    if len(password) != 12:
        err_notif.config(fg='red',text='Password must be 12 characters')
        return 
    # Initialize variables
    found = False
    index = 0

    # Use a while loop to iterate through the list
    while index < len(all_accounts):
        if all_accounts[index] == name:
            found = True
            break
        index += 1

    # Check the result
    if found:
        
        err_notif.config(fg ="red", text="Account already exists")
        return
    else:
        new_file = open(f"{name}.txt","w")
        new_file_acc = open(f"{name}","w")
        statement = open(f"{name}_balance_update.txt","w")
        open(f"{name}log","w")
        new_file.write(f"Account no : {random_9_digit_number}\n")
        new_file.write(f"Name       : {name}\n")
        new_file.write(f"Password   : {password}\n")
        new_file_acc.write(password)
        statement.write(f"Balance = R{amount}")
        new_file.write(f"ID number  : {id_number}\n")
        new_file.write(f"Gender     : {gender}\n")
        
        # new_file.write(f"Balance    : R0")
        new_file.close()
        pop_up=Toplevel(root)
        pop_up.title("Account")
        Label(pop_up,text=f"Hi {name}, The Mint's account \nhas been succesfully created", font=("Arial",12)).grid(row=0,sticky=N)
        Label(pop_up,text=f"Name     : {name}").grid(row=1,sticky=W)
        Label(pop_up,text=f"Ac no    : {password}").grid(row=2,sticky=W)
        Label(pop_up,text=f"Password : {password}").grid(row=3,sticky=W)
        Label(pop_up,text=" ").grid(row=4,sticky=W)
        
        Button(pop_up,text="OK",command=kill_popup).grid(row=5,sticky=W)
        
        Label(pop_up,text=" ").grid(row=6,sticky=W)
        
        register_screen.destroy()

def kill_popup():
    pop_up.destroy
    
def kill_popup2():
    sub.destroy()
    
def register():
    #register vars
    
    global temp_name
    global temp_id
    global temp_gender
    global temp_password
    global notif
    global err_notif
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
    Label(register_screen, text="Enter your details to register", font=("calibri",12)).grid(row=0,sticky=N)
    Label(register_screen, text="Name            : ", font=("calibri",12)).grid(row=1,sticky=W)
    Label(register_screen, text="ID no.(DDMMYYYY): ", font=("calibri",12)).grid(row=2,sticky=W)
    Label(register_screen, text="Gender          : ", font=("calibri",12)).grid(row=3,sticky=W)
    Label(register_screen, text="password        : ", font=("calibri",12)).grid(row=4,sticky=W)
   
    
    
    #Entries
    Entry(register_screen,textvariable=temp_name).grid(row=1,column=1,sticky=E,padx=10)#Relative padding
    Entry(register_screen,textvariable=temp_id).grid(row=2,column=1,sticky=E,padx=10)
    Entry(register_screen,textvariable=temp_gender).grid(row=3,column=1,sticky=E,padx=10)
    Entry(register_screen,textvariable=temp_password, show="*").grid(row=4,column=1,sticky=E,padx=10)
    notif = Label(register_screen, font=("calibri",12))
    notif.grid(row=5,sticky=N,pady=10)
    err_notif = Label(register_screen, font=("calibri",12))
    err_notif.grid(row=6,sticky=N,pady=10)
    
    #register button
    Button(register_screen, text="Register"         , command=finish_reg, font=("calibri",12),width=25).grid(row= 7,column=0 , sticky=N, pady = 10)
    Button(register_screen, text="generate password", command=generate_random_password, font=("calibri",12),width=25).grid(row= 7,column=1, sticky=N, pady = 10)
    
def login_function():
    global login_name
    global balance_update_update
    global account_dashboard
    
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
                Label(account_dashboard, text = f"Welcome {login_name}", font=("calibri",12)).grid(row=2,sticky=N,padx=10)
                
                #Buttons
                Button(account_dashboard,text="Personal details", font=("calibri",12),width=30, command= personal_details).grid(row=3,sticky=N,padx=10)
                Button(account_dashboard,text="Deposit", font=("calibri",12),width=30,command=deposits).grid(row=4,sticky=N,padx=10)
                Button(account_dashboard,text="Withdraw" ,font=("calibri",12),width=30,command=withdrawals).grid(row=5,sticky=N,padx=10)
                Button(account_dashboard,text="Transaction log" ,font=("calibri",12),width=30,command=transaction).grid(row=6,sticky=N,padx=10)
                Button(account_dashboard,text="Investments" ,font=("calibri",12),width=30,command=investments).grid(row=7,sticky=N,padx=10)
                Button(account_dashboard,text="Home Loan" ,font=("calibri",12),width=30,command=bond).grid(row=8,sticky=N,padx=10)
                Button(account_dashboard,text="Change password" ,font=("calibri",12),width=30,command=change_password).grid(row=9,sticky=N,padx=10)
                Label(account_dashboard).grid(row=10,sticky=N)
                Button(account_dashboard,text="Logout" ,font=("calibri",12),width=15,command=logout, bg="red").grid(row=11,sticky=E,padx=1)
                
                #
                Label(account_dashboard).grid(row=12,sticky=N,pady=10)
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

def forgot_password():
    global f_username
    global f_id_num
    global for_notif
    global f_new_password
    global f1_new_password
    f_username = StringVar()
    f_id_num = StringVar()  
    f_new_password = StringVar()
    f1_new_password = StringVar()
    
    forgot = Toplevel(root)
    forgot.title("Password reset")
    
    #Labeels
    Label(forgot, text="Login to your account", font=("calibri",12)).pack()
    
    Label(forgot, text="Username:", font=("calibri",12)).pack()
    Entry(forgot,textvariable=f_username).pack()
    
    Label(forgot, text="id_number(DDMMYYYY):", font=("calibri",12)).pack()
    Entry(forgot,textvariable=f_id_num).pack()
    
    Label(forgot, text="New PIN :", font=("calibri",12)).pack()
    Entry(forgot,textvariable=f_new_password).pack()
    
    Label(forgot, text="Confirm PIN:", font=("calibri",12)).pack()
    Entry(forgot,textvariable=f1_new_password).pack()
    
    for_notif = Label(forgot, font=("calibri",12))
    for_notif.pack() 
     
    Button(forgot, text="submit", command=submit, font=("calibri",12), width=15).pack()
    
    print("forgot_password")
    

def change_password():
    global change_notif
    global f_new_passwords
    global f1_new_passwords 
    global change_pass
    f_new_passwords = StringVar()
    f1_new_passwords = StringVar()
    
    change_pass = Toplevel(root)
    change_pass.title("Password reset")
    
    #Labeels
    Label(change_pass, text="Change password", font=("calibri",12)).pack()
    
    Label(change_pass, text="New PIN :", font=("calibri",12)).pack()
    Entry(change_pass,textvariable=f_new_passwords).pack()
    
    Label(change_pass, text="Confirm PIN:", font=("calibri",12)).pack()
    Entry(change_pass,textvariable=f1_new_passwords).pack()
    
    change_notif = Label(change_pass, font=("calibri",12))
    change_notif.pack() 
     
    Button(change_pass, text="submit", command=submit_change, font=("calibri",12), width=15).pack()
    
    print("chnage_password")
    
    
def submit_change():
    new_passw    = f_new_passwords.get()
    new_passw1   = f1_new_passwords.get() 
    global sub
    
    forgot_all_accounts = os.listdir()
    #Validated
    
  
    new_passw =new_passw.replace(" ", "").strip()
    new_passw1 =new_passw1.replace(" ", "").strip()
    
    if new_passw =="" or new_passw1 =="":
        change_notif.config(fg="red", text="All inout fields are important")
    elif new_passw1 != new_passw:
        change_notif.config(fg="red", text="Password does not match")
    else:
        f = open(login_name+".txt",'a')
        f.writelines(f"new password : {new_passw}\n")
        f.close()
        g = open(login_name,'w')
        g.write(new_passw)
        
        change_pass.destroy()
        sub = Toplevel(root)
        sub.title("Success")
        
        Label(sub, text=f"New pin created succesfully").pack()
        Label(sub, text=" ").pack()
        Label(sub, text=f"New pin: {new_passw}").pack()
        Label(sub, text=" ").pack()
        Button(sub, text="OK", width=7, command=kill_popup2).pack()
        Label(sub, text=" ").pack()
        
def submit():
    forgot_username = f_username.get()
    forgot_id_number = f_id_num.get()
    new_password    = f_new_password.get()
    new_password1   = f1_new_password.get() 
    
    
    forgot_all_accounts = os.listdir()
    #Validated
    
    forgot_username = forgot_username.replace(" ", "").strip()
    forgot_id_number = forgot_id_number.replace(" ", "").strip()
    new_password =new_password.replace(" ", "").strip()
    new_password1 =new_password1.replace(" ", "").strip()
    
    print(forgot_username)  
        #############Test the data base
    
    ##########################
    
    pattern = re.compile(r'^(0[1-9]|[1-2][0-9]|3[0-1])(0[1-9]|1[0-2])(1920|19[2-9][0-9]|20[0-1][0-9]|202[0-3])$')
    print(forgot_all_accounts)
    if forgot_username == "" or forgot_id_number == "" or f_new_password == "" or f1_new_password=="":
        print("All inout fields are required ")
        for_notif.config(fg ="red", text="All input fields are required!")
    
    else:   
        # Initialize variables
        found = False
        index = 0

        # Use a while loop to iterate through the list
        while index < len(forgot_all_accounts):
            if forgot_all_accounts[index] == forgot_username:
                found = True
                break
            index += 1

        # Check the result
        if found:
            print(f"{forgot_username} exists in the list")
            if pattern.match(forgot_id_number):
                forgot = open(f"{forgot_username}.txt", "r")
                forgot_files = forgot.readlines()
                id_after_colon = forgot_files[3].split(':')[1].strip()
                if forgot_id_number == id_after_colon:
                    if new_password == new_password1:
                        app = open(forgot_username,'w')
                        app.write(new_password)
                        app.close()
                        update_new_pass = open(f"{forgot_username}.txt","a")
                        update_new_pass.writelines(f"new password : {new_password}\n")
                        # forgot.destroy()
                        return
                    else:
                        for_notif.config(fg="red", text="Passwords does not match")
                        return
                else:
                    for_notif.config(fg="red", text="Wrong ID number")  
                    return    
            else:
                for_notif.config(fg="red", text="Invalid Id number")  
                return     
        else:
            print(f"{forgot_username} does not exist in the list")
            for_notif.config(fg="red", text="Account does not exist")
        
    
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
    login_notif.grid(row=3,sticky=N,pady=10)
    
    
    #Entries
    Entry(login_screen,textvariable=temp_login_name).grid(row=1,column=1,padx=5)#Relative padding
    Entry(login_screen,textvariable=temp_login_password, show="*").grid(row=2,column=1)
    
    Label(login_screen, text=" ", font=("calibri",12)).grid(row=4,sticky=W)
    #register button
    Button(login_screen, text="Login", command=login_function, font=("calibri",12), width=15).grid(row= 5,column=0 )
    Button(login_screen, text="forgot-password", command=forgot_password, font=("calibri",12), width=15).grid(row= 5,column=1)
    Label(login_screen, text=" ", font=("calibri",12)).grid(row=6,sticky=W)
    
    

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