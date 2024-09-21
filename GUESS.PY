import random
from logo import logo
num = random.randint(1,101)
# print(num)
j = 0
def guess(i):
    print(logo)
    global num,j
    x = int(input("Enter Your guess: "))
    # print(num)
    if x == num:
        print("HURRAH!\nYou guess the number")
        return 0
    
    elif x>num:
        if x-10<num:
            print("TOO CLOSE")
            
            
        else:
            print("TOO HIGH")
        i-=1
        if i>=0:
            print(f"Chances {i}")
            guess(i)
        else:
            return "You Lose the game"
    else:
        if x+10>num:
            print("TOO CLOSE")
        else:
            print("TOO LOW")
        i-=1
        if i>=0:
            print(f"Chances {i}")
            guess(i)
        else:
            print("Number is ",num)
            return "You Lose the game"

       

check = input("Enter Level \n1.EASY\n2.HARD\nEnter: ")
if check == "1":
    i = 10
    print(guess(i))
elif check == "2":
    i = 5
    print(guess(i))
else:
    print("Wrong Input!")
