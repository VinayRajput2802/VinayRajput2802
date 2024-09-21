from getpass import getpass
import time

def access():
    print('Welcome to vinay ATM')
    acc = open('data.txt','r')
    atm_no = []
    pin_no = []

    for i in acc:
        atm1,pin1 = i.split(',')
        pin1 = pin1.strip()

        atm_no.append(atm1)
        pin_no.append(pin1)
    my_atm = dict(zip(atm_no,pin_no))
    
    def countdown(t):
        while t:
            mins,secs = divmod(t,60)
            timer = '{:02d}:{:02d}'.format(mins,secs)
            print(timer,end='\r')
            time.sleep(1)
            t-=1
        return
    def details():

        atm = input("Enter ATM number: ")
        pin = getpass("Create PIN: ")
        con_pin = getpass("Confirm PIN: ")

        if int(pin) != int(con_pin):
            details()
        elif atm in atm_no:
            print("ATM no already exists")
            access()
        else:
            if len(pin)!=4:
                print("Enter 4 digits pin only")
                details()
            elif len(atm)!= 12:
                print("Enter 12 digits atm number only")
                details()
            
            else:
                countdown(5)
                data = open('data.txt','a')
                data.write(atm+','+pin+'\n')
                
                print("PIN successfully created") 

    def deposite():
        
        print(my_atm)

        atm = input('Enter ATM number: ')
        pin = getpass('Enter PIN Number: ')
        pin_1 = my_atm.get(atm)
        print(pin_1)
        if atm in atm_no and pin == pin_1 :
            cash = input("Enter deposite money: ")
            cash3 = open('money.txt','r')
            for j in cash3:
                atm2,cash2 = j.split(',')
                cash2 = cash2.strip()
                if atm2 == atm:
            
                    cash1 = str(int(cash)+int(cash2))
                    with open('money.txt','r') as file:
                        file_data = file.read()
                    file_data = file_data.replace(cash2,cash1)

                    with open('money.txt','w') as file:
                        file.write(file_data)
                        countdown(5)
                        print("Payment Successful")
                        break
            else:
                countdown(5)
                money = open('money.txt','a')
                money.write(atm+','+cash+'\n')
                print("Payment successful")
        else:
            print("ATM and PIN does not exists")

    def check_balance():
        cash = open('money.txt','r')
        atm_1 = input("Enter ATM number: ")
        pin = getpass("Enter PIN number: ")
        for money in cash:
            atm,cash1 = money.split(',')
            cash1 = cash1.strip()
            pass1 = my_atm.get(atm_1)
            if atm_1 == atm and pin == pass1:
                countdown(5)
                print(f"Total money = {cash1}")
                break
            
        else:
            print("Wrong Pin and ATM number")
            print("No money in your bank account")
            check = input('if you deposite money first (y/n): ')
            if check == 'y':
                deposite()
            else:
                print("Thankyou for visit")
    
    def change_pin():
        data = open('data.txt','r')
        atm2 = input("ENTER ATM NUMBER: ")
        pin2 = getpass("ENTER PIN: ")
        pass1 = my_atm.get(atm2)
        for i in data:
            atm,pin = i.split(',')
            pin = pin.strip()
            if atm2 == atm and pin2 ==pass1:
                pin3 = getpass("ENTER NEW PIN: ")
                pin_con = getpass("CONFIRM PIN: ")
                if pin3 != pin_con:
                    print("Confirm pin and pin does not match")
                    change_pin()
                else:
                    if len(pin3) != 4:
                        print("PIN only in 4 Numbers")
                        change_pin()
                    else:
                        change = atm+','+pin2
                        new = atm+','+pin3
                        with open('data.txt','r') as file:
                            file_data = file.read()
                        file_data = file_data.replace(change,new)

                        with open('data.txt','w') as file:
                            file.write(file_data)

    def withdraw():
        atm = input('Enter ATM number: ')
        pin = getpass('Enter PIN Number: ')
        pin_1 = my_atm.get(atm)
        print(pin_1)
        if atm in atm_no and pin == pin_1 :
            cash = input("Enter withdraw money: ")
            cash3 = open('money.txt','r')
            if int(cash) <= 40000:
                for j in cash3:
                    atm2,cash2 = j.split(',')
                    cash2 = cash2.strip()
                    if atm2 == atm:
                
                        cash1 = str(int(cash2)-int(cash))
                        old = atm+','+cash2
                        new = atm+','+cash1
                        with open('money.txt','r') as file:
                            file_data = file.read()
                        file_data = file_data.replace(old,new)

                        with open('money.txt','w') as file:
                            file.write(file_data)
                            countdown(10)
                            print("Withdraw successfully")
                            break
                else:
                    print("Low balance")
            else:
                print("ATM limit upto 40,000")
        else:
            print("ATM and PIN does not exists")



    check = input("1.ATM PIN GENERATE\n2.DEPOSITE MONEY\n3.CHECK BALANCE\n4.CHANGE PIN\n5.WITHDRAW MONEY\n: ")
    if check == '1':
        print("WELCOME TO PIN GENERATE")
        details()
    elif check == '2':
        print("DEPOSITE MONEY")
        deposite()
    elif check == '3':
        print("CHECK BALANCE")
        check_balance()
    elif check == '4':
        change_pin()
    elif check == '5':
        withdraw()
    else:
        print("INVALID INPUT")

    
access()



