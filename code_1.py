import random
import os
from data import detail
from logo import art,vs1
def vs(x,i):
    print(art)
    try:
        y = random.choice(detail)
        detail.remove(y)
    except UnboundLocalError and IndexError:
        print("YOU WON THE GAME")
        print("YOUR SCORE IS ",i)
    else:
        name = x.get("Name")
        follower = x.get("Follower")
        prof = x.get("Profession")
        country = x.get("Country")
        print(f"A\nName : {name}\nprofession : {prof}\nCountry : {country}")
        print()
        print(vs1)
        print()
        name1 = y.get("Name")
        follower1 = y.get("Follower")
        prof1 = y.get("Profession")
        country1 = y.get("Country")
        print(f"B\nName : {name1}\nProfession : {prof1}\nCountry : {country1}")
        print()
        check = (input("Enter A and B: "))
        if check == "A" or check == "a":
            if follower > follower1:
                i+=1
                print("Correct")
                os.system('cls')
                vs(x,i)
            else:
                print("Incorrect!!")
                print("YOUR SCORE IS :",i)
            

        elif check == "B" or check == "b":
            if follower < follower1:
                print("Correct")
                i+=1
                os.system('cls')
            
                vs(y,i)
            else:
                print("Incorrect!!")
                print("YOUR SCORE IS :",i)
            
        else:
            print("WRONG INPUT")
            game()


def game():
    
    
    x= random.choice(detail)
    detail.remove(x)

    vs(x,0)



game()