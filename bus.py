def register():
    bus = input("Enter Bus Size(L,M,S): ")
    num = input("Enter Bus Number: ")
    b = open("bus.txt",'r')
    for i in b:
        name,bus1,num1,avail = i.split(',')
        avail = avail.strip()
        if num == num1 and bus == bus1:
            print("Bus Already Registered")
            register()
            break
    else:
        driver = input("Enter Driver Name: ")
        b = open('bus.txt','a')
        b.write(driver+','+bus+','+num+','+'Y'+'\n')
        print("Registered Successfully")
    
def check():
    num = input("Which type of bus you want (L,M,S): ")
    b = open("bus.txt",'r')
    for i in b:
        name,bus1,num1,avail = i.split(',')
        avail = avail.strip()
        if avail == "Y" and num == bus1:
            print(name+" : "+bus1+" : "+num1)

    else:
        ck = input("If you want to book bus \nEnter (y/n): ")
        if ck == 'y':
            book()
        elif ck == "n":
            
            print("\nThankyou for visiting")
        else:
            print("Invalid Input")


def book():
    num = input("Enter Bus Number: ")
    b = open("bus.txt",'r')
    nam = input("Enter Your name: ")
    tour = input("Enter your destination: ")
    km = input("Enter distance (in km): ")
    # cash = ""
    for i in b:
        name,bus1,num1,avail = i.split(',')
        avail = avail.strip()
        if num == num1 and avail == "Y":
            print(f"Driver name : {name}\nsize : {bus1}\nBus Number : {num1}")
            old = name+','+bus1+','+num1+','+avail+'\n'
            input_file = 'bus.txt'
            new = name+','+bus1+','+num1+','+'N'+'\n'
            with open(input_file,'r') as file:
                file_data = file.read()
            file_data = file_data.replace(old,new)
            with open(input_file,'w') as file:
                file.write(file_data)
            
            charge = open('charge.txt','a')
            if bus1 == "L":
                cash = str(5000+int(km)*50)
            elif bus1 == "S":
                cash = str(4500+int(km)*30)
            elif bus1 == "M":
                cash = str(5000+int(km)*40)
            charge.write(nam+':'+num1+':'+tour+":"+km+":"+cash+"\n")

            print("Your Order Confirmed")
            break
    else:
        print("Sorry does not find any bus")

def cancel():
    num = input("Enter Bus Number: ")
    b = open("bus.txt",'r')
    
    for i in b:
        name,bus1,num1,avail = i.split(',')
        avail = avail.strip()
        if num == num1 and avail == "N":
            print(f"Driver name : {name}\nsize : {bus1}\nBus Number : {num1}")
            old = name+','+bus1+','+num1+','+avail+'\n'
            input_file = 'bus.txt'
            new = name+','+bus1+','+num1+','+'Y'+'\n'
            with open(input_file,'r') as file:
                file_data = file.read()
            file_data = file_data.replace(old,new)
            with open(input_file,'w') as file:
                file.write(file_data)
            print("Your Order Cancelled")
            break
    else:
        print("Sorry does not find any bus")



def status():
    num = input("Enter bus Number: ")
    b = open("bus.txt",'r')
    for i in b:
        name,bus1,num1,avail = i.split(',')
        avail = avail.strip()
        if num == num1:
            print(name+" : "+bus1+" : "+avail)
            break
    else:
        print("Thankyou")
        

def charge():
    print("L type bus additional charge : 5000 Rs\nKm charge : 50Rs per Km")
    print("\nM type bus additional charge : 5000 Rs\nKm charge per Km : 40 Rs per km")
    print("\nS type bus additional charge : 4500 Rs\nKm charge per Km : 30Rs per Km")


sys = input("1.Registration of Bus\n2.Check Availabble Bus\n3Cancel Book\n4.Check Status\n5.About Charge of bus\nEnter: ")
if sys == "1":
    register()
elif sys == "2":
    check()
elif sys =="3":
    cancel()
elif sys == "4":
    status()
elif sys == "5":
    charge()
else:
    print("Invalid Input")
