# PROGRAM DETAILS
# This is program of Hospital Management System.
# IN this program :
# 1 = Check in system, In this system first input All details of Pateint and family and Address.
# 2 = Checking system, In this system used for check patient name, Disease, Doctor Name and Secret code.
# 3 = Fees system, In this system enter deposite money and also check statement of payment details and date.
# 4 = Check out system, In this system if you want to check out therefore you do not check in this details, 
#     if you want to checkin again then you take new check in system.


from getpass import getpass
import time
import calendar
def access():
    def register():
        sec = open('secret.txt','r')
        i = sec.read()

        secret = str(int(i)+1)
        sec = open('secret.txt',"w")
        sec.write(secret)
        sec.close()

        print("\n!!!!  Welcome to Hospital  !!!!\n")
        name = input("Enter Patient name: ")
        date_of_birth = input("Enter Date of Birth (D-M-Y): ")
        father = input("Enter Father's Name: ")
        adress = input("Enter Address [(Vill/Town/City)-Dist-State]: ")
        disease = input("Disease Name: ")
        doctor = input("Enter Doctor Name: ")
        fees = input("Enter fess: ")
        pay = input("Deposite money: ")
        
        d,m,y = map(int,input("Enter (Date-Month-Year): ").strip().split('-'))
        
        day = calendar.day_name[calendar.weekday(y,m,d)]
        check_in = f"date: {str(d)}-{str(m)}-{str(y)}--{day}"

        time1 = time.strftime('%H:%M:%S')

        data = open('data.txt','a')
        data.write(name+','+date_of_birth+','+father+','+adress+','+disease+','+check_in+','+time1+'\n')

        check = open('check.txt','a')
        check.write(name+','+secret+','+disease+','+doctor+'\n')
        

        money = open('money.txt','a')
        money.write(name+','+secret+','+fees+','+pay+'\n')
        print("Registerd Successfully")
        access()
    def check():
        check_out = open('checkout.txt','r')
        data = open('check.txt','r')
        id = getpass("Enter secret code")

        for j in check_out:
            id1,name1,date,time1 = j.split(',')
            if id1 == id:
                print("Patient already Checkout")
                break
        else:
            for i in data:
                name,secret,disease,doctor = i.split(',')
                doctor = doctor.strip()
                if id == secret:

                    print(f"\nPatient Name: {name}\nDisease: {disease}\nDoctor Name: {doctor}")
                    break
            access()
        
    def statement():
        id = getpass("Enter ID number: ")
        money = open('money.txt','r')
        for i in money:
            name,secret,fees,pay = i.split(',')
            pay = pay.strip()
            
            if id == secret:
                print('Statement')
                print(f"Name = {name}\nTotal fees = {fees}\nDeposite Amount = {pay}\nPayable Amount = {str(int(fees)-int(pay))}")
        access()    

    def pay():
        id = getpass("Enter Secret Code: ")
        money = open('money.txt','r')
        for i in money:
            name,secret,fees,pay = i.split(',')
            pay = pay.strip()

            if id == secret:
                print('Statement')
                print(f"Name = {name}\nTotal fees = {fees}\nDeposite Amount = {pay}\nPayable Amount = {str(int(fees)-int(pay))}")

                option = input("1.pay\n2.Exit\n: ")
                if option == "1":
                    pay1 = input('Depsite Pay: ')

                    new_pay = str(int(pay)+int(pay1))
                    state = open('statement.txt','a')
                    state.write(id+','+pay1+'\n')
                    with open('money.txt','r') as file:
                        file_data = file.read()
                        file_data = file_data.replace(pay,new_pay)
                    with open('money.txt','w') as file:
                        file.write(file_data)
                    print("Payment Successfull")



                    break
        access()
                    



    def checkout():
        data = open('check.txt','r')
        
        id = getpass("Enter secret code: ")
        
        money = open('money.txt','r')
        def run():
            check_out = open("checkout.txt",'r')
            for j in check_out:
                id1,name1,checkDate,time2 = j.split(',')
            

                if id == id1:
                    print("Patient already Checkout!!")
                    print(id1,name1,checkDate,time2)
                    break
            else:
                for i in data:
                    name,secret,disease,doctor = i.split(',')
                    print(secret)
                    doctor = doctor.strip()
                    if id == secret:
                        d,m,y = map(int,input("Enter (Date-Month-Year): ").strip().split('-'))

                        day = calendar.day_name[calendar.weekday(y,m,d)]
                        check_out_date = f"date: {str(d)}-{str(m)}-{str(y)}--{day}"

                        time1 = time.strftime('%H:%M:%S')
                        check_out = open('checkout.txt','a')
                        check_out.write(secret+','+name+','+check_out_date+','+time1+'\n')
                        break
                    
                else:
                    print("Wrong Id")

        for cash in money:
            name2,code,payment,deposite = cash.split(',')
            if id == code:
                if int(payment) == int(deposite):
                    run()
                    break
        else:
            print("!!Payment Pending!!")
            access()
    

    def paymentStatement():
        state = open('statement.txt','r')
        id2 = getpass("Enter ID")
        print(f"Statement of this Id {id2}")
        num = 1
        for j in state:
            id1,payment = j.split(',')
            payment = payment.strip()
            if id1 == id2:
                print(num,'=',payment)
                num += 1
        else:
            print("No payment Data")


    option = input("1. Check in\n2. Check patient detail\n3. Checkout\n4. Check Statement\n5.For paying amount\n6.Payment Statement\n: ")
    if option == '1':
        register()
    elif option == '2':
        check()
    elif option == '3':
        checkout()
    elif option == '4':
        statement()
    elif option == '5':
        pay()
    elif option == '6':
        paymentStatement()
    else:
        print("Enter Valid Number")

access()

