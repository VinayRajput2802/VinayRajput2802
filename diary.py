from getpass import getpass



def register():
    
    user = open('login.txt','r')
    user1 = []
    pass1 = []
    for i in user:
        n,d,us,pas = i.split(',')
        pas = pas.strip()
        user1.append(us)
        pass1.append(pas)
    my_username = dict(zip(user1,pass1))

    name = input("Enter Your Name: ")
    dob = input("Enter date of birth(d-m-y): ")
    def user_name():
        username = input("Enter Username: ")
        password = input("Enter Password: ")
        password1 = input("Enter Confirm Password: ")

        if password != password1:
            print("Password and Confirm password does't match")
            user_name()
        else:
            if len(password) < 6:
                print("Length of password is less than 6")
                user_name()
            
            elif username in user1:
                print("Username already registered")
                user_name()
            
            else:
                user = open("login.txt",'a')
                user.write(name+','+dob+','+username+','+password+'\n')
                note = open('notes.txt','a')
                note.write(username+":-"+"notes = "+"\n")
                print("Account Successfully Created")
    user_name()

def login():
    user = open('login.txt','r')
    username = getpass("Enter Username: ")
    password = getpass("Enter Password: ")

    for i in user:
        n,d,us,pas = i.split(',')
        pas = pas.strip()
        if us == username and password == pas:
            print(f"Welcome {n} to diary management")
            def notes():
                main = open('notes.txt')
                l = 0
                for i in main:
                    l +=1
                    user1,note1 = i.split(":-")
                    note1 = note1.strip()
                    if user1 == username:
                        print(note1)
                        note2 = input("Enter Notes\n=")
                        note3 = note1+note2
                        
                        new = username+':-'+note3+"\n"

                        s = 'notes.txt'
                        with open(s,'r') as file:
                            file_data = file.readlines()
                            line = 1
                            with open(s,'w') as file:
                                for txt in file_data:
                                    if line == l:
                                        file.write(new)
                                    else:
                                        file.write(txt)
                                    line += 1
                                break
                                print("Your Notes will be saved successfully")
                            
                        
            notes()

            break

    else:
        print("Username and Password does not match")
        ck = input("1.Create Account\n2.Login\nEnter: ")
        if ck == '1':
            register()
        elif ck == '2':
            login()
    
sys = input("1.Register New Account\n2.Login Account\nEnter: ")
if sys == "1":
    register()
elif sys == "2":
    login()        

