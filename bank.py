def register():
    name = input("Enter name: ")
    adhar = input("Enter Adhaar number: ")
    user = open('user.txt','r')
    for i in user:
        name1,adhar1,acc_num,total = i.split(',')
        total = total.strip()
        if name == name1 and adhar == adhar1:
            print("your account already exists")
            break

    else:
        balance = input("Enter Amount do you want to deposite: ")
        if len(adhar) != 12:
            print("adhaar card number invalid")
            register()
        else:
            acc = open('account.txt','r')
            for i in acc:
                old_acc = i
                new_acc = str(int(i)+1)
            print(f"Your Account Number: {new_acc}")
            user = open('user.txt','a')
            user.write(name+','+adhar+','+new_acc+','+balance+'\n')
            print("\nThankyou for visiting")
            acc1 = 'account.txt'
            with open(acc1,'r') as file:
                file_data = file.read()
            file_data = file_data.replace(old_acc,new_acc)

            with open(acc1,'w') as file:
                file.write(file_data)
# register()


def deposite():
    name = input("Enter Name: ")
    acc = input("Enter Account Number: ")
    acc1 = open('user.txt','r')
    for i in acc1:
        name1,adhar,acc2,bal = i.split(',')
        bal = bal.strip()
        if name == name1 and acc == acc2:
            cash = input("Enter Money: ")
            old = name1+','+adhar+','+acc2+','+bal+'\n'
            new = name1+','+adhar+','+acc2+','+str(int(bal)+int(cash))+'\n'
            state = open('state.txt','a')
            state.write(acc2+','+'+'+cash+','+str(int(bal)+int(cash))+'\n')
            user = 'user.txt'
            with open(user,'r') as file:
                file_data = file.read()
            file_data = file_data.replace(old,new)
            with open(user,'w') as file:
                file.write(file_data)
            break


def withdraw():
    name = input("Enter Name: ")
    acc = input("Enter Account Number: ")
    acc1 = open('user.txt','r')
    for i in acc1:
        name1,adhar,acc2,bal = i.split(',')
        bal = bal.strip()
        if name == name1 and acc == acc2:
            cash = input("Enter Money: ")
            if int(cash) > int(bal):
                print("Account does not have enough money")
                break
            else:
                old = name1+','+adhar+','+acc2+','+bal+'\n'
                new = name1+','+adhar+','+acc2+','+str(int(bal)-int(cash))+'\n'
         

                state = open('state.txt','a')
                state.write(acc2+','+'-'+cash+','+str(int(bal)-int(cash))+'\n')
                
                user = 'user.txt'
                with open(user,'r') as file:
                    file_data = file.read()
                file_data = file_data.replace(old,new)
                with open(user,'w') as file:
                    file.write(file_data)
                break
def statement():

    account = input("Enter Account Number: ")
    state = open('state.txt','r')
    for i in state:
        acc,cash,bal = i.split(",")
        bal = bal.strip()
        if account == acc:
            print(acc+" : "+cash+" : "+bal)
    else:
        print("Done")


opt = input("1.Create an Account\n2.Deposite Money\n3.Withdraw money\n4.Statement\nEnter: ")
if opt == '1':
    print("Thankyou for creating an account\n")
    register()
elif opt == '2':
    print("Thankyou for using bank\n")
    deposite()
elif opt == '3':
    print("Thankyou for using my bank\n")
    withdraw()
elif opt == '4':
    statement()
else:
    print("Invalid Input")