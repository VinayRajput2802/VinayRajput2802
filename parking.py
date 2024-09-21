import time
def entry():
    car_name = input('Car Owner Name: ')
    no_plate = input("Enter last Four digit of Your Number Plate: ")
    data = open("park.txt",'r')
    
    sp = open('space.txt','r')
    for i in sp:
        old = i
    if int(old) <= 50:

    
        for k in data:
            car_name1,secret1,time2,plate = k.split(',')
            plate = plate.strip()
            if car_name == car_name1 and plate == no_plate:
                print(f"Your car already parked at no. {secret1}")
                break
        else:

            print("FEES OF 1HOUR PARKING: 50")
            time1 = time.strftime("%H:%M")
            print(time1)
            car = open('car_no.txt','r')

            for i in car:
                old_car_no = i
                car_no = int(i)+1
                car_no = str(car_no)
            with open('car_no.txt','r') as file:
                file_data = file.read()
            file_data = file_data.replace(old_car_no,car_no)

            with open('car_no.txt','w') as file:
                file.write(file_data)


            print(f"Your parking no.{no_plate} = {old_car_no} ")
            car1 = open("park.txt",'a')
            car1.write(car_name+','+old_car_no+','+time1+','+no_plate+'\n')
            print("your car parked successfully")
            new = str(int(old)+1)
            space = 'space.txt'
            with open(space,'r') as file1:
                file_data1 = file1.read()
            file_data1 = file_data1.replace(old,new)
            with open(space,'w') as file1:
                file1.write(file_data1) 
    else:
        print("Sorry Vinay Parking station is full")

def exit():
    secret2 = input("Enter secret Number: ")
    no = input("Enter Number of Number plate: ")
    data = open('park.txt','r')
    count = 0
    # secret = input("Secret Number: ")
    for j in data:
        car_name1,secret1,time2,plate = j.split(',')
        plate = plate.strip()
        count += 1
        if secret2 == secret1 and plate == no:
            h,m = time2.split(':')
            time3 = time.strftime("%H:%M")
            h1,m1 = time3.split(':')
            fees = 30*((int(h1)-int(h))*60 + (int(m1)-int(m)))
            print(f"Total Time Parking: {((int(h1)-int(h))*60 + (int(m1)-int(m)))}min")
            print(f"Total fees: {30+fees//60}")
            print("Thankyou For visiting in Vinay Parking Management")
            new = str(int(old)-1)
            sp = open('space.txt','r')
            for i in sp:
                old = i
            space = 'space.txt'
            with open(space,'r') as file1:
                file_data1 = file1.read()
            file_data1 = file_data1.replace(old,new)
            with open(space,'w') as file1:
                file1.write(file_data1)
            
            
            break 
    else:
        print("Your car not parked in Vinay Parking Station")
    c = 'park.txt'
    with open(c,'r') as file:
        file_data = file.readlines()
        file_line = 1
        with open(c,'w') as file:
            for text in file_data:
                if count != file_line:
                    file.write(text)
                file_line += 1
                
            
chk = input("1. Entry\n2. Exit\nEnter: ")
if chk == '1' or chk == 'Entry':
    print("Welcome to Vinay Parking Management")
    entry()
elif chk == '2' or chk == 'Exit':
    exit()