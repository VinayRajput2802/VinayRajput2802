from datetime import date
def register():
    def one():
        
        Name = input("Enter Student Name: ")
        st = open("1st.txt",'r')
        for i in st:
            name,f= i.split(',')
            if Name == name:
                print("Student Already Registered")
        else:
            fee = open('fees.txt','r')
            for i in fee:
                cl,fees = i.split(",")
                fees = fees.strip()
                if cl == "1":
                    
                    chk = open('1st.txt','a')
                    chk.write(Name+','+fees+'\n')
                    print("Student Registered Suucessfully\n")

                    break
            else:
                print("Class Not registered")
        c = input("1==Exit and hit any button : ")
        if c != "1":
            one()
        else:
            print("Thankyou")
        

    def second(): 
        Name = input("Enter Student Name: ")
        st = open("2nd.txt",'r')
        for i in st:
            name,f= i.split(',')
            if Name == name:
                print("Student Already Registered")
        else:
            fee = open('fees.txt','r')
            for i in fee:
                cl,fees = i.split(",")
                fees = fees.strip()
                if cl == "2":
                    
                    chk = open('2nd.txt','a')
                    chk.write(Name+','+fees+'\n')
                    print("Student Registered Suucessfully\n")
                    break
            else:
                print("Class Not registered")
        c = input("1==Exit and hit any button : ")
        if c != "1":
            second()
        else:
            print("Thankyou")
    def third():

        Name = input("Enter Student Name: ")
        st = open("3rd.txt",'r')
        for i in st:
            name,f= i.split(',')
            if Name == name:
                print("Student Already Registered")
        else:
            fee = open('fees.txt','r')
            for i in fee:
                cl,fees = i.split(",")
                fees = fees.strip()
                if cl == "3":
                    
                    chk = open('3rd.txt','a')
                    chk.write(Name+','+fees+'\n')
                    print("Student Registered Suucessfully\n")
                    break
            else:
                print("Class Not registered")
        c = input("1==Exit and hit any button : ")
        if c != "1":
            third()
        else:
            print("Thankyou")
    def fourth():
        Name = input("Enter Student Name: ")
        st = open("4th.txt",'r')
        for i in st:
            name,f= i.split(',')
            if Name == name:
                print("Student Already Registered")
        else:
            fee = open('fees.txt','r')
            for i in fee:
                cl,fees = i.split(",")
                fees = fees.strip()
                if cl == "4":
                    
                    chk = open('4th.txt','a')
                    chk.write(Name+','+fees+'\n')
                    print("Student Registered Suucessfully\n")
                    break
            else:
                print("Class Not registered")
        c = input("1==Exit and hit any button : ")
        if c != "1":
            fourth()
        else:
            print("Thankyou")
    def fifth():
        Name = input("Enter Student Name: ")
        st = open("5th.txt",'r')
        for i in st:
            name,f= i.split(',')
            if Name == name:
                print("Student Already Registered")
        else:
            fee = open('fees.txt','r')
            for i in fee:
                cl,fees = i.split(",")
                fees = fees.strip()
                if cl == "5":
                    
                    chk = open('5th.txt','a')
                    chk.write(Name+','+fees+'\n')
                    print("Student Registered Suucessfully\n")
                    break
            else:
                print("Class Not registered")
        c = input("1==Exit and hit any button : ")
        if c != "1":
            fifth()
        else:
            print("Thankyou")


    chk = input("Enter Class: ")
    if chk == "1":
        print('\n')
        

        one()
    elif chk == "2":
        print('\n')

        second()
    elif chk == "3":
        print('\n')

        third()
    elif chk == "4":
        print('\n')

        fourth()
    elif chk == "5":
        print('\n')

        fifth()
    else:
        print('\n')

        print("Class not exists")


def fees():
    today = str(date.today())
    name = input("Enter name: ")
    chk = input("Enter Class: ")
    if chk == "1":
        st = open("1st.txt",'r')
        line = 0
        for i in st:
            line += 1
            name1,fee = i.split(',')
            fee = fee.strip()
            if name1 == name:
                print(f'Fees Pending: {fee}')
                dep = input("Enter Amount to pay: ")
                pend = str(int(fee)-int(dep))
                old = name+','+fee
                new = name+','+pend
                input_file = '1st.txt'
                his = open("history.txt",'a')
                his.write(name1+','+chk+','+dep+','+today+'\n')
                his.close()
                with open(input_file,'r') as file:
                    file_data = file.read()
                file_data = file_data.replace(old,new)

                with open(input_file,'w') as file:
                    file.write(file_data)
                print("Fees deposite Successfully")
                break
        else:
            print("Student Not Registerd in class 1")

    elif chk == "2":
        st = open("2nd.txt",'r')
        line = 0
        for i in st:
            line += 1
            name1,fee = i.split(',')
            fee = fee.strip()
            if name1 == name:
                print(f'Fees Pending: {fee}')
                dep = input("Enter Amount to pay: ")
                pend = str(int(fee)-int(dep))
                old = name+','+fee
                new = name+','+pend
                input_file = '2nd.txt'
                his = open('history.txt','a')
                his.write(name1+','+chk+','+dep+','+today+'\n')
                his.close()
                with open(input_file,'r') as file:
                    file_data = file.read()
                file_data = file_data.replace(old,new)

                with open(input_file,'w') as file:
                    file.write(file_data)
                print("fees deposite Successfully")
                break
        else:
            print("Student Not Registerd in class 2")

    elif chk == "3":
        st = open("3rd.txt",'r')
        line = 0
        for i in st:
            line += 1
            name1,fee = i.split(',')
            fee = fee.strip()
            if name1 == name:
                print(f'Fees Pending: {fee}')
                dep = input("Enter Amount to pay: ")
                pend = str(int(fee)-int(dep))
                old = name+','+fee
                new = name+','+pend
                input_file = '3rd.txt'
                his = open('history.txt','a')
                his.write(name1+','+chk+','+dep+','+today+'\n')
                his.close()
                with open(input_file,'r') as file:
                    file_data = file.read()
                file_data = file_data.replace(old,new)

                with open(input_file,'w') as file:
                    file.write(file_data)
                print("fees deposite Successfully")
                break
        else:
            print("Student Not Registerd in class 3")

    elif chk == "4":
        st = open("4th.txt",'r')
        line = 0
        for i in st:
            line += 1
            name1,fee = i.split(',')
            fee = fee.strip()
            if name1 == name:
                print(f'Fees Pending: {fee}')
                dep = input("Enter Amount to pay: ")
                pend = str(int(fee)-int(dep))
                old = name+','+fee
                new = name+','+pend
                input_file = '4th.txt'
                his = open('history.txt','a')
                his.write(name1+','+chk+','+dep+','+today+'\n')
                his.close()
                with open(input_file,'r') as file:
                    file_data = file.read()
                file_data = file_data.replace(old,new)

                with open(input_file,'w') as file:
                    file.write(file_data)
                print("fees deposite Successfully")
                break
        else:
            print("Student Not Registerd in class 4")

    elif chk == "5":
        st = open("5th.txt",'r')
        line = 0
        for i in st:
            line += 1
            name1,fee = i.split(',')
            fee = fee.strip()
            if name1 == name:
                print(f'Fees Pending: {fee}')
                dep = input("Enter Amount to pay: ")
                pend = str(int(fee)-int(dep))
                old = name+','+fee
                new = name+','+pend
                input_file = '5th.txt'
                his = open('history.txt','a')
                his.write(name1+','+chk+','+dep+','+today+'\n')
                his.close()
                with open(input_file,'r') as file:
                    file_data = file.read()
                file_data = file_data.replace(old,new)

                with open(input_file,'w') as file:
                    file.write(file_data)
                print("fees deposite Successfully")
                break
        else:
            print("Student Not Registerd in class 5")
    
    else:
        print("Class Does Not Registered")
    fees()


def class_register():
    cl1 = input("Enter Class: ")
    l = 0
    st = open('fees.txt','r')
    for i in st:
        l+=1
        cl,fee = i.split(',')
        
        fee = fee.strip()
        if cl == cl1:
            print("Class Already Registered")
            chk = input("1.For Change fees\nclick any button to exit\nEnter: ")
            if chk == "1":
                new_fees = input("Enter New fees: ")
                old = cl1+','+fee
                new = cl1+','+new_fees+'\n'
                input_file = 'fees.txt'
                with open(input_file,'r') as file:
                    file_data = file.readlines()
                    line = 1

                    with open(input_file,'w') as file:
                        for t in file_data:
                            if line == l:
                                file.write(new)
                            else:
                                file.write(t)
                            line += 1
                break
            else:
                print("Thankyou")
            
    else:
        fee1 = input("Enter Total Fees: ")
        st = open('fees.txt','a')
        st.write(cl1+','+fee1+'\n')
        print("Class Registeres Successfully")
    # c = input("1.Exit and click any button: ")
    # if c == "1":
    #     print("Thankyou")
    # else:
    #     class_register()
def history():
    name = input("Enter Name: ")
    class1 = input("Enter Class: ")
    hist =  open("history.txt",'r')
    for i in hist:
        nam,cl,pay,dat = i.split(",")
        dat.strip()
        if name == nam and class1 == cl:
            print("\n"+name+":"+cl+":"+pay+":"+dat)
    else:
        print("Only this payment datails history!")

    

sys = input("1.Register\n2.fees\n3.Class Registration\n4.History\nEnter: ")
if sys == "1":
    register()
elif sys == "2":
    fees()
elif sys == "3":
    class_register()
elif sys == "4":
    history()
else:
    print("Fuction Not Available yet")

                    





