def class1():
    def score_update():
        Name = input('Enter Student name: ')
        st = open('class1.txt','r')
        line = 0
        for i in st:
            line += 1
            name,h,e,m,s,ss = i.split(",")
            ss = ss.strip()
            if Name == name:
                print("Please Enter Marks")
                hindi = input("Enter Hindi Marks: ")
                english = input("Enter English Marks: ")
                math = input("Enter Math marks: ")
                science = input("Enter science marks: ")
                sst = input("Enter s.st marks: ")

                input_file = 'class1.txt'
                old = name,h,e,m,s,ss
                new = name+','+str(int(h)+int(hindi))+','+str(int(english)+int(e))+','+str(int(math)+int(m))+','+str(int(science)+int(s))+','+str(int(sst)+int(ss))+'\n'
                with open(input_file,'r') as file:
                    file_data = file.readlines()
                    
                    l = 1
                    with open(input_file,'w') as file:
                        for text in file_data:
                            if line == l:
                                file.write(new)
                            else:
                                file.write(text)
                            
                print("Scorecard updated successfully!")
                break
            
        else:
            print("Student not registerd")
    

    def register():
        Name = input("Enter Student name: ")
        st = open('class1.txt','r')
        for i in st:
            name,h,e,m,s,ss = i.split(",")
            ss = ss.strip()
            if name == Name:
                print("Student Already Registered")
                print("If two or more student name are same then take (student1 ,stuendent2) like this so on")
            
                register()
        else:
            h,e,m,s,ss = input("Enter Hindi Marks"),input("Enter Engilsh marks: "),input("Enter Maths marks: "),input("Enter Science marks: "),input("Enter S.st marks: ")

            st = open('class1.txt','a')
            st.write(Name+','+h+','+e+','+m+','+s+','+ss+'\n')
    # register()

    def show():
        Name = input("Enter Name: ")
        st = open('class1.txt','r')
        for i in st:
            name,h,e,m,s,ss = i.split(',')
            ss = ss.strip()
            
            if Name == name:
                print(f"Name : {Name}\nClass : 1st\nHindi : {h}\nEnglish : {e}\nMaths : {m}\nScience : {s}\nS.st : {ss}")
                count = 0
                if int(h)<33:
                    
                    count += 1
                if int(e)<33:
                    count += 1
                if int(m)<33:
                    count += 1
                if int(s)<33:
                    count += 1
                if int(ss)<33:
                    count += 1
            
                if count > 0 and count < 3:
                    print("Compartment")
                elif count >=3:
                    print("Fail")
                else:
                    print("pass")
                
                break
        else:
            print("Student does not registered")
    
    def all_student():
        st = open('class1.txt','r')
        for i in st:
            name,h,e,m,s,ss = i.split(',')
            ss = ss.strip()
            print("Vinay Public School")
            print(f"Name : {name}\nClass : 1st\nHindi : {h}\nEnglish : {e}\nMaths : {m}\nScience : {s}\nS.st : {ss}\n")
    

    def topper():
        name1 = ''
        name2 = ''
        name3 = ''
        name4 = ''
        name5 = ''
        first = 0
        sec = 0
        third = 0
        forth = 0
        fifth = 0
        st = open('class1.txt','r')
        for i in st:
            name,h,e,m,s,ss = i.split(',')
            ss = ss.strip()
            sum = int(h)+int(e)+int(m)+int(s)+int(ss)
            if sum >= first:
                fifth = forth
                forth = third
                third = sec
                sec = first
                first = sum
                name5 = name4
                name4 = name3
                name3 = name2
                name2 = name1
                name1 = name

                
                
        print(f"Rank : Name = Marks\nFirst : {name1} = {first}\nSecond : {name2} = {sec}\nThird : {name3} = {third}\nForth : {name4} = {forth}\nFifth : {name5} = {fifth}")

    def delete():
        name1 = input("Enter Name: ")
        st = open('class1.txt','r')
        l = 0
        for i in st:
            l += 1
            name,h,e,m,s,ss = i.split(',')
            ss = ss.strip()
            if name1 == name:
                input_file = 'class1.txt'
                with open(input_file,'r') as file:
                    file_data = file.readlines()
                    line = 1
                    with open(input_file,'w') as file:
                        for text in file_data:
                            if line != l:
                                file.write(text)
                            line += 1
                    print("Successfully Deleted")
                
                    break


    ck = input("1.Register Student\n2.Update Result\n3.Check Particular student Result\n4.Check All student Result\n5.Check Topper\n6. Delete\nEnter: ")
    if ck == "1":
        print("Wel Come to Registration Module")
        register()
    elif ck == "2":
        print("Wel come to update score card")
        score_update()
    elif ck == "3":
        print("Wel come for checking result")
        show()
    elif ck == "4":
        print("All student Result")
        all_student()
    elif ck == "5":
        print("Checking topper")
        topper()
    elif ck == '6':
        print("Delete")
        delete()
    else:
        print("Invalid Input")





            

def class2():
    def score_update2():
        Name = input('Enter Student name: ')
        st = open('class2.txt','r')
        line = 0
        for i in st:
            line += 1
            name,h,e,m,s,ss = i.split(",")
            ss = ss.strip()
            if Name == name:
                print("Please Enter Marks")
                hindi = input("Enter Hindi Marks: ")
                english = input("Enter English Marks: ")
                math = input("Enter Math marks: ")
                science = input("Enter science marks: ")
                sst = input("Enter s.st marks: ")

                input_file = 'class2.txt'
                old = name,h,e,m,s,ss
                new = name+','+str(int(h)+int(hindi))+','+str(int(english)+int(e))+','+str(int(math)+int(m))+','+str(int(science)+int(s))+','+str(int(sst)+int(ss))+'\n'
                with open(input_file,'r') as file:
                    file_data = file.readlines()
                    
                    l = 1
                    with open(input_file,'w') as file:
                        for text in file_data:
                            if line == l:
                                file.write(new)
                            else:
                                file.write(text)
                            
                print("Scorecard updated successfully!")
                break
            
        else:
            print("Student not registerd")
    

    def register2():
        Name = input("Enter Student name: ")
        st = open('class2.txt','r')
        for i in st:
            name,h,e,m,s,ss = i.split(",")
            ss = ss.strip()
            if name == Name:
                print("Student Already Registered")
                print("If two or more student name are same then take (student1 ,stuendent2) like this so on")
            
                register2()
        else:
            h,e,m,s,ss = input("Enter Hindi Marks"),input("Enter Engilsh marks: "),input("Enter Maths marks: "),input("Enter Science marks: "),input("Enter S.st marks: ")

            st = open('class2.txt','a')
            st.write(Name+','+h+','+e+','+m+','+s+','+ss+'\n')
    # register2()

    def show2():
        Name = input("Enter Name: ")
        st = open('class2.txt','r')
        for i in st:
            name,h,e,m,s,ss = i.split(',')
            ss = ss.strip()
            
            if Name == name:
                print(f"Name : {Name}\nClass : 1st\nHindi : {h}\nEnglish : {e}\nMaths : {m}\nScience : {s}\nS.st : {ss}")
                count = 0
                if int(h)<33:
                    
                    count += 1
                if int(e)<33:
                    count += 1
                if int(m)<33:
                    count += 1
                if int(s)<33:
                    count += 1
                if int(ss)<33:
                    count += 1
            
                if count > 0 and count < 3:
                    print("Compartment")
                elif count >=3:
                    print("Fail")
                else:
                    print("pass")
                
                break
        else:
            print("Student does not registered")
    
    def all_student():
        st = open('class2.txt','r')
        for i in st:
            name,h,e,m,s,ss = i.split(',')
            ss = ss.strip()
            print("Vinay Public School")
            print(f"Name : {name}\nClass : 1st\nHindi : {h}\nEnglish : {e}\nMaths : {m}\nScience : {s}\nS.st : {ss}\n")
    

    def topper2():
        name1 = ''
        name2 = ''
        name3 = ''
        name4 = ''
        name5 = ''
        first = 0
        sec = 0
        third = 0
        forth = 0
        fifth = 0
        st = open('class2.txt','r')
        for i in st:
            name,h,e,m,s,ss = i.split(',')
            ss = ss.strip()
            sum = int(h)+int(e)+int(m)+int(s)+int(ss)
            if sum >= first:
                fifth = forth
                forth = third
                third = second
                second = first
                first = sum
                name5 = name4
                name4 = name3
                name3 = name2
                name2 = name1
                name1 = name

        print(f"Rank : Name = Marks\nFirst : {name1} = {first}\nSecond : {name2} = {sec}\nThird : {name3} = {third}\nForth : {name4} = {forth}\nFifth : {name5} = {fifth}")
 
 
    def delete2():
        name1 = input("Enter Name: ")
        st = open('class2.txt','r')
        l = 0
        for i in st:
            l += 1
            name,h,e,m,s,ss = i.split(',')
            ss = ss.strip()
            if name1 == name:
                input_file = 'class2.txt'
                with open(input_file,'r') as file:
                    file_data = file.readlines()
                    line = 1
                    with open(input_file,'w') as file:
                        for text in file_data:
                            if line != l:
                                file.write(text)
                            line += 1
                    print("Successfully Deleted")
                
                    break
                
                
        
    
    ck = input("1.Register Student\n2.Update Result\n3.Check Particular student Result\n4.Check All student Result\n5.Check Topper\n6.Delete\nEnter: ")
    if ck == "1":
        print("Wel Come to Registration Module")
        register2()
    elif ck == "2":
        print("Wel come to update score card")
        score_update2()
    elif ck == "3":
        print("Wel come for checking result")
        show2()
    elif ck == "4":
        print("All student Result")
        all_student()
    elif ck == "5":
        print("Checking topper")
        topper2()
    elif ck == '6':
        print("Delete")
        delete2()
    else:
        print("Invalid Input")

option = input("Enter Class: ")
if option == "1":
    print("Open Class 1")
    class1()
elif option == "2":
    print("Open Class 2")
    class2()


