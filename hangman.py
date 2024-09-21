import random

def game():
    import hangman_logo 
    print(hangman_logo.logo)
    book = open('secret.txt','r')
    for i in book:
        library = list(i.split())
    
    word = random.choice(library)
    res = word
    count = 0
    x = ""
    secret_word = []
    dic = {}

    for i in range(len(word)):
        if count %2 == 0:
            x+=word[i]
        else:
            if word[i] in dic:
                x+= word[i]
                count += 1
            else:
                dic[word[i]] = i
                x+="_"
                secret_word.append(word[i])
        count += 1

    x = x.upper()
    print("\nWord is " +x+"\n")
    over = 5
    correct = 0
    
    print("YOU HAVE ONLY 5 WRONG ATTEMPTS\n")
    print("\nCHARACTER IN LOWER CASE")
    from hang_man import hang
    while (over != 0):
        s = input("\nEnter Character : ")
        if s.isupper() == True:
            s = s.lower()
        if s in secret_word:
            print("\nCorrect Choice")
            ind =dic.get(s)
            secret_word.remove(s)
            x = x[:ind]+s+x[ind+1:]
            x = x.upper()
            correct += 1
            print(x)
            if secret_word == []:
                print("\nWINNER WINNER CHICKEN DINNER")
                break

        else:
            over -= 1
            print(f"\nWrong Answer")
            print(f"\nYour chances of wrong answer is {over}")
            print()
            print(hang[over])


    else:
        print(f"\nCorrect Word is {res.upper()}")
        print("\nGame Over\nHANGMAN DIED")

    check = input("IF YOU WANT TO PLAY (Y/N): ")
    if check.islower():
        check = check.upper()

    if check == "Y":
        game()
    else:
        print("\nTHANKS FOR PLAYING")
           

game()