from getpass import getpass

def users():
    data = open('data.txt','r')
    user = []
    pass1 = []
    for i in data:
        m,n = i.split(":")
        n =n.strip()
        user.append(m)
        pass1.append(n)

    my_data = dict(zip(user,pass1))
    


    def register():
        ### some information ###
        name = input("Enter Your Full Name: ")
        date = input("Enter your date of DOB: ")
        month = input("Enter your month of DOB: ")
        year = input("Enter your year of DOB: ")

        ## username and password ##
        username = input("Username: ")
        password = getpass("Password: ")
        password1 = getpass("Confirm Password: ")

        if password != password1:
            print("password and confirm password does not match!!")
            print("Register again")
            register()
        

        else:
            if len(password)<6:
                print("Password too short (min length = 6)")
                register()
            elif username in user:
                print("Username already exists: ")
                register()
            else:
                data = open('data.txt','a')
                data.write(username+":"+password+"\n")

                per = open('personal.txt','a')
                per.write(name+":"+date+"-"+month+"-"+year+":"+username+"\n")

                print("success")
                access()

    def login():
        username = input("Username: ")
        password = getpass("Password: ")
        pass2 = my_data.get(username)

        if username in user and pass2 == password:
            print("Successfully Login")
            
            access()
        else:
            print("Invalid username and password")
            login()


    def access():
        username = input('Enter username same as login: ')
        sc = open('score.txt','r')
        name = []
        sc2 = []
        for _ in sc:
            name1,sc1 = _.split(',')
            sc1= sc1.strip()

            name.append(name1)
            sc2.append(sc1)
        
        my_score = dict(zip(name,sc2))
        my_pass = my_score.get(username)
        print(my_pass)
        def entrance():
            
            j =1
            score = 0
            que = open("entrance.txt",'r')
            for i in que:
                q,a,b,c,d,res = i.split(",")
                
                print(f"Que{j}. {q}\n")

                print(f"a. {a}     b. {b}")
                print(f"c. {c}     d. {d}\n")
                ans = input("Enter Your Answer: ")
                res= res.strip()
                if res != ans:
                    print("Wrong Answer\n")
                    score -= 0.25
                else:
                    print("Correct Answer\n")
                    score += 1
                j += 1
            
            
            if username in name:
                if float(my_pass) >= float(score):
                    print("Try again")
                elif float(my_pass)<float(score):
                    with open('score.txt','r') as file:
                        file_data = file.read()
                    file_data = file_data.replace(my_pass,str(score))

                    with open('score.txt','w') as file:
                        file.write(file_data)
                
            else:
                sc = open('score.txt','a')
                sc.write(username+","+str(score)+"\n")
            
        

        def quiz():
            print(my_pass)
            if username in name:
                if float(my_pass)>=3:
                    j = 1
                    score = 0
                    que = open('Questions.txt','r')

                    for i in que:
                        q,a,b,c,d,res = i.split(",")
                        res = res.strip()

                        print(f"Que{j}. {q}\n")

                        print(f"a. {a}     b. {b}")
                        print(f"c. {c}     d. {d}\n")
                        ans = input("Enter Your Answer: ")
                        res= res.strip()
                        if res != ans:
                            print("Wrong Answer\n")
                            
                        else:
                            print("Correct Answer\n")
                            score += 1
                        j += 1
                    level = score//5

                    sc_1 = open('Level.txt','r')
                    name2 = []
                    sc_2 = []
                    lev = []
                    for _ in sc_1:
                        name_1,sc3,l = _.split(',')
                        l = l.strip()
                        name2.append(name_1)
                        sc_2.append(sc3)
                        lev.append(l)
                    
                    my_list = dict(zip(name2,sc_2))
                    my_list1 = dict(zip(name2,lev))
                    my_pass2 = my_list1.get(username)
                    my_pass1 = my_list.get(username)
                    
                    if username in name2:

                        if level <= float(my_pass1):
                            print(f"Your level is {my_pass1}")
                        else:
                            with open('Level.txt','r') as file:
                                file_data = file.read()
                            file_data = file_data.replace(my_pass1,str(level))
                            file_data = file_data.replace(my_pass2,str(score))


                            with open('Level.txt','w') as file:
                                file.write(file_data)

                    else:
                        sc_1 = open('Level.txt','a')
                        sc_1.write(username+","+str(level)+','+str(score)+'\n')
                        print(f"Your level is {level}\nYour score is{score}")
                else:
                    print("Your Entrane score is low \nYou take first entrance exam")
                    entrance()

            else:
                print("Your Entrane score is low \nYou take first entrance exam")
                entrance()

        def new_func(my_pass1):
            print(float(my_pass1))



        status = input("CHOOSE\n1.Entrance Exam\n2.Quiz\n3.Summary\n:")
        if status == "1":
            print("WELCOME TO ENTRANCE EXAM OF BIGGEST QUIZ")
            entrance()
        elif status == "2":
            print("WELCOME TO THE BIGGEST QUIZ ")
            quiz()
        elif status == "3":
            data1 = open('level.txt','r')
            name2 = []
            lev1 = []
            sc3 = []
            for i in data1:
                
                name,sc,lev = i.split(",")
                lev = lev.strip()

                name2.append(name)
                lev1.append(lev)
                sc3.append(sc)
            
            my_data1 = dict(zip(name2,sc3))
            my_data2 = dict(zip(name2,lev1))

            my_sc = my_data1.get(username)
            my_lev = my_data2.get(username)


            print(f"username = {name}\nLevel = {my_sc}\nScore = {my_lev}")
            print('\n')
            access()
        else:
            print("Invalid Input")
            
            
        
    check = input("Choose\n1.New User\n2.Exsisting user\n")
    if check == "1":
        register()
    elif check == "2":
        login()
    else:
        print("Invalid Input")

def admin():
    data = open("admin_log.txt",'r')
    user = []
    pass1 = []
    for i in data:
        m,n = i.split(",")
        n = n.strip()
        user.append(m)
        pass1.append(n)
    my_data = dict(zip(user,pass1))

    def register():
        name = input("Enter Your full Name: ")
        date = input("date of birth (d-m-y): ")
        username = input("Enter username: ")
        password = getpass("Enter Password: ")
        password1 = getpass("Confirm Password: ")

        if password != password1:
            print("Wrong Password!")
            register()
        
        elif len(password)<6:
            print("Password too short (min length 6)")
            register()
        
        else:
            
            if username in user:
                print("Username is already exists")
                register()
            else:
                print("Your account successfully created!!")
                data = open("admin_log.txt",'a')
                data.write(username+','+password)

                det = open("admin_data.txt",'a')
                det.write(name+'='+date+','+username)
                access()


    def login():
        username = input("Enter Username: ")
        password = getpass("Enter Password: ")

        my_pass = my_data.get(username)

        if username in user and password == my_pass:
            print("Login succesfully")
            access()

        else:
            print("username and password does not match!")
            login()
            
    
    def access():
        sys = input("1.ADD QUESTION\n2.REMOVE QUESTION\n3.REPLACE QUESTION\n4.CHECk SCORE AND LEVEL OF ALL USERS\n5.Logout\n: ")
        if sys =="1":
            check1 = input("1.Entrance\n2.Quiz\n=")
            if check1 == "1":
                question =  input("Enter Question: ")
                a = input("Option a: ")
                b = input("Option b: ")
                c = input("Option c: ")
                d = input("Option d: ")
                ans = input("answer option(a,b,c,d): ")
                op = open('entrance.txt','a')
                op.write(question+","+a+','+b+','+c+','+d+','+ans+'\n')
                print("Question Successfully added")
            elif check1 == "2":
                question =  input("Enter Question: ")
                a = input("Option a: ")
                b = input("Option b: ")
                c = input("Option c: ")
                d = input("Option d: ")
                ans = input("answer option(a,b,c,d): ")
                op = open('Questions.txt','a')
                op.write(question+","+a+','+b+','+c+','+d+','+ans+'\n')
                print("Question Successfully added")
            else:
                print("Invalid Input")
            print("\n")
            access()
        
        elif sys == "2":
            check2 = input("1.ENRANCE\n2.QUIZ\n=")

            if check2 == "1":
                ent = open('entrance.txt','r')
                j = 1
                
                for i in ent:
                    print(f"Que{j} = {i}")
                    
                    j = j+1
                
                rem = int(input("Enter questions number: "))
                

                input_file = 'entrance.txt'
                with open(input_file,'r') as file:
                    file_line = file.readlines()

                    line = 1

                    with open(input_file,'w') as file:
                        for textline in file_line:
                            if line != rem:
                                file.write(textline)
                                
                            line += 1
                    print("Question remove successfully")
            elif check2 =='2':
                qui = open('Questions.txt','r')
                
                j = 1
                
                for i in qui:
                    print(f"Que{j} = {i}")
                   
                    j = j+1
                
                remove = int(input("Enter questions number: "))
                

                inputFile = 'Questions.txt'

                with open(inputFile,'r') as file_data:
                    fileLine = file_data.readlines()

                    num_line = 1

                    with open(inputFile,'w') as file_data:
                        for textline1 in fileLine:
                            if num_line != remove:
                                file_data.write(textline1)

                            num_line += 1
                    print("Question remove Succesfully")
            else:
                print("Invalid Input")
            print('\n')
            access()
        
        elif sys == "3":
            check3 = input("1.Entrance\n2.Quiz\n= ")
            que = input("Enter Questions: ")
            a1 = input("Enter option a: ")
            b1 = input("Enter option b: ")
            c1 = input("Enter option c: ")
            d1 = input("Enter option d: ")
            ans1 = input("Enter correct option(a,b,c,d): ")


            if check3 == "1":
                j =1
                ent1 = open('entrance.txt','r')
                for i in ent1:
                    print(f"Que{j}={i}")
                    j = j+1
                rep = int(input("Enter question no. do you want to replace: "))


                input_file1 = 'entrance.txt'
                with open(input_file1,'r') as file1:
                    file_rep = file1.readlines()

                    line1 = 1

                    with open(input_file1,'w') as file1:
                        for text in file_rep:
                            if rep != line1:
                                file1.write(text)
                            else:
                                file1.write(que+","+a1+","+b1+","+c1+","+d1+","+ans1+"\n")
                            line1 += 1
                    print("Question replaced succesfully!!")
            
            elif check3 == "2":
                j =1
                qui1 = open('Questions.txt','r')
                for i in qui1:
                    print(f"Que {j}= {i}")
                    j = j+1
                rep1 = int(input("Enter question no. do you want to replace"))

                input_file2 = 'Questions.txt'
                with open(input_file2,'r') as file3:
                    file_rep1 = file3.readlines()

                    line2 = 1

                    with open(input_file2,'w') as file3:
                        for text1 in file_rep1:
                            if rep1!= line2:
                                file3.write(text1)
                            else:
                                file3.write(que+','+a1+','+b1+','+c1+','+d1+','+ans1+'\n')
                            line2 = line2+1
                    print("Question replaced succesfully")
            else:
                print("Invalid Input!!")
            print('\n')
            access()

        elif sys == "4":
            data1 = open('level.txt','r')
            for i in data1:
                name,sc,lev = i.split(",")
                lev = lev.strip()
                print(f"username = {name}\nscore = {sc}\nlev = {lev}")
            print('\n')
            access()

        sys == "5"
        print("Log out Successfully!!")



    check = input("1. New admin\n2.Excisting admin\n=")
    if check == "1":
        register()
    
    elif check == "2":
        login()

    else:
        print("Invalid Input")



choose = input("1. Admin\n2. User\n")
if choose == "1":
    num = input("Enter key for admin login!!")
    if num == "14725"or num == "admin":
        print("Welcome to admin login")
        admin()
elif choose == "2":
    print("Welcome to users login")
    users()
else:
    print("Invalid Input")
