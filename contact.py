def access():
    contact = open('contact.txt','r')
    name = []
    mob = []
    for i in contact:
        nam,mo = i.split(',')
        mo = mo.strip()
        name.append(nam)
        mob.append(mo)
    my_contact = dict(zip(mob,name))
    my_name = dict(zip(name,mob))
    def add():
        no = input("Enter mobile Number: ")
        name1 = input("Enter Name: ")
        if no in mob:
            print('Mobile Number already exists')
            print(my_contact.get(no))
        elif len(no) != 10:
            print('Check Mobile number (length = 10)')
        elif name1 in name:
            print("Name Already Exists")
            print(my_name.get(name1))
        else:
            
            data = open('contact.txt','a')
            data.write(name1+','+no+'\n')
            print("Number Added Successfully")
    def search():
        
        chk = input("1. By name\n2.By Mob Number\n: ")
       
        if chk == '1':
            name2 = input("Enter Name: ")
            print(my_name.get(name2))
        elif chk == '2':
            num2 = input("Enter Number: ")
            print(my_contact.get(num2))

    def delete():
        chk = input("Search: ")
        data = open('contact.txt','r')
        count = 1
        for i in data:
            name1,num= i.split(',')
            num = num.strip()
            if name1 == chk:
                count = count
                break
            elif num == chk:
                count = count
                break
            else:
                count += 1
        else:
            print("This mobile number and name does not exists in contacts list")
        input_file = 'contact.txt'
        with open(input_file,'r') as file:
            file_data = file.readlines()
            count1 = 1
            with open(input_file,'w') as file:
                for text in file_data:
                    if count1 != count:
                        file.write(text)
                    count1 += 1
            print("DELETE SUCCESSFULLY")
    def contact_list():
        contact1 = open('contact.txt','r')
        count = 1
        for j in contact1:
            name2,num2 = j.split(',')
            num2 = num2.strip()
            print(f"{count}. {name2} - {num2}")
            count += 1
    print("1.ADD MOBILE NUMBER\n2.SEARCH\n3.DELETE NUMBER\n4.CONTACT LIST")
    
    while True:
        chk = input("ENTER: ")
        if chk == '1':
            add()
        elif chk == '2':
            search()
        elif chk == '3':
            delete()
        elif chk == '4':
            contact_list()
        else:
            False

  

    
access()
        