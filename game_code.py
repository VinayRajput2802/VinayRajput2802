import random
from score import cards
from score import computer1,art
def one_card():
    
    one = random.choice(cards)
    cards.remove(one)
    return one

def computer():
    
    return computer1
def user():
    user = []
    user.append(one_card())
    user.append(one_card())
    return user

def chance(user1):
    sums = sum(user1)
    
    while sums < 23:
        print(f"THE SUM OF ALL NUMBER IS {sum(user1)}")
        if input("Enter you want to take another card (y/n):") == "y":
            x = one_card()
            if x == 11:
                if int(input("If you want to 11 to 1")) == 1:
                    x = 1
            user1.append(x)
            sums = sum(user1)
        else:
            if sum(computer()) < sums:
                return f"WIN\nScore : {sums}\ncomputer Score {sum(computer())}"
            elif sum(computer()) > sums:
                return f"LOSE\nScore : {sums}\ncomputer Score {sum(computer())}"
            else:
                return f"DRAW\nScore : {sums}\ncomputer Score {sum(computer())}"
    else:
        return f"LOSE\nScore : {sums}\ncomputer Score {sum(computer())}"



def game():
    user1 = user()
    comp = computer()
    if 11 in user1:
        return (f"WIN\nScore : {sum(user1)}\ncomputer Score {sum(comp)}\nbecause of ACE")
    elif 11 in comp:
        return (f"LOSE\nScore : {sum(user1)}\ncomputer Score {sum(comp)}\nbecauser of ACE")
    else:
        return(chance(user1))

print(art)
print()
print(game())
    

    



    
