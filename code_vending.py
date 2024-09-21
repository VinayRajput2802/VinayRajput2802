import time
from logo import art
from many import m,name2,x
material_required = open("material.txt",'r')
for mat in material_required:
    coffee_powder,milk,water,sugar,profit = map(float,mat.split(':'))


def off():
    print("Thank You")
    print("Machine is off")
def profit_margin():
    print(f"Your All over Profit is {profit}")
    vending()

def vending():
    print()

    def payment(n):
        print(f"PAY : {n}")
        pay = int(input("Payment Enter: "))
        if pay == 0:
            off()
        if pay > n:
            print(f"{pay-n} take change")
        elif pay < n:
            print(f"Payment not complete and required payment is {pay-n}")
            payment(n-pay)
        return True
    def sugar1(name,n):
        global sugar
        m = n*(x.get(name)[3])
        if (m<=sugar):
            return True
        else:
            return False
    def milk1(name,n):
        global milk
        m = n*(x.get(name)[1])
        if (m<=milk):
            return True
        else:
            return False
    def water1(name,n):
        global water
        m = n*(x.get(name)[2])
        if (m<=water):
            return True
        else:
            return False
    def coffee_powder1(name,n):
        global coffee_powder
        m = n*(x.get(name)[0])
        if (m<=coffee_powder):
            return True
        else:
            return False
    def countdown(t):
        
        while t:
            mins,sec = divmod(t,60)
            timer = '{:02d}:{:02d}'.format(mins,sec)
            print(timer,end='\r')
            time.sleep(1)
            t-=1
        return
    def making_coffee(name,n):
        global material_required,sugar,coffee_powder,milk,water,profit
        coffee_powder -= n*(x.get(name)[0])
        milk -= n*(x.get(name)[1])
        sugar -= n*(x.get(name)[3])
        water -= n*(x.get(name)[2])
         
        
        
        print("Preparing Coffee!!")
        t = 30+n*10
        countdown(t)
        global art
        print(art)
        print()
        print("Coffee is ready!!")
        material_required = open('material.txt','w')
        material_required.write(str(coffee_powder)+":"+str(milk)+":"+str(water)+":"+str(sugar)+":"+str(profit))
        
        
    def coffee(name,n,price):
        
        if payment(price) == True:
            global profit
            profit += price
            
            True
        else:
            print("Payment Not Complete")
            vending()
        if (sugar1(name,n) == True):
            True
        else:
            print("Insufficient Sugar")
            vending()
        if (milk1(name,n) == True):
            True
        else:
            print("Insufficient Milk")
            vending()
        if (water1(name,n) == True):
            True
        else:
            print("Insufficient Water")
            vending()
        if coffee_powder1(name,n) == True:
            True
        else:
            print("Insufficient Coffee Powder")
        making_coffee(name,n)
    def add_material(): 
        global material_required,coffee_powder,milk,water,sugar
        
        print(f"Coffee powder  : {coffee_powder}")
        print(f"Sugar          : {sugar}")
        print(f"Milk Quantity  : {milk} L")
        print(f"Water Quantity : {water} L")

        check = input("IF you want to add some material (y/n): ")
        if (check == "y"):
            cof = float(input("Enter Coffee_Powder Quantity: "))
            sug = float(input("Sugar Quantity: "))
            mil = float(input("Enter Milk Quantity: "))
            wat = float(input("Enter Water Quantity: "))

            mater = open('material.txt','w')
            mater.write(str(cof+coffee_powder)+":"+str(milk+mil)+":"+str(water+wat)+":"+str(sugar+sug)+str(profit))
            mater.close()
            vending()
        else:
            vending()
    def menu():

        print("--WELCOME TO APNA COFFEE--")
        print()
        
        print(m)
        order = int(input("Enter Coffee Serial No : "))
        name1 = name2[order][0]
        
        n = int(input("How many Cup Coffee: "))
        price = name2[order][1]
        coffee(name1,n,price)

        
    check = input("0.Machine OFF\n1. Add material\n2.Coffee Order\n3.Profit\nEnter: ")
    if check == "1":
        add_material()
    elif check == '2':
        
        menu()
    elif check == '3':
        profit_margin()
    else:
        off()
    
vending()