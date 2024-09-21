from tkinter import *
from functools import partial


class APP:
    def __init__(self,root2) -> None:

        
        self.name = StringVar()
        self.father = StringVar()
        self.dob = IntVar()
        self.add = StringVar()
        self.disease1 = StringVar()
        self.doctor = StringVar()
        self.fees = IntVar()
        self.deposite = IntVar()

        root2.geometry("1600x800")
        root2.config(bg = "white")
        def submit(name,father,dob,add,disease1,doctor,fees,deposite):
            root2.destroy()
        
        def check(self):
            name = self.name.get()
            father = self.father.get()
            dob = self.dob.get()
            add = self.add.get()
            disease = self.disease1.get()
            doctor = self.doctor.get()
            fees = self.disease.get()
            deposite = self.deposite.get()




        lab1 = Label(root2,text="HOSPITAL MANAGEMENT SYSTEM",font=("courier",40,"bold"),fg="red",bg="white").place(x = 450,y = 50)
        lab2 = Label(root2,text="REGISTER PATIENT",font=("courier",40,"bold"),fg="RED",bg="white").place(x = 500,y = 120)

        lab3 = Label(root2,text="NAME                       :",font=("courier",20,"bold"),fg="black",bg="white").place(x = 200,y = 200)
        entry1 = Entry(root2,textvariable=self.name,font=("courier",20,"bold"),fg="black",bg="white").place(x = 700,y = 200)

        lab4 = Label(root2,text="FATHER'S NAME              :",font=("courier",20,"bold"),fg="black",bg="white").place(x = 200,y = 250)
        entry2 = Entry(root2,textvariable=self.father,font=("courier",20,"bold"),fg="black",bg="white").place(x = 700,y = 250)

        lab4 = Label(root2,text="DOB(BIRTH YEAR)            :",font=("courier",20,"bold"),fg="black",bg="white").place(x = 200,y = 300)
        entry2 = Entry(root2,textvariable=self.dob,font=("courier",20,"bold"),fg="black",bg="white").place(x = 700,y = 300)

        lab4 = Label(root2,text="ADDRESS(VILL/TOWN/CITY)    :",font=("courier",20,"bold"),fg="black",bg="white").place(x = 200,y = 350)
        entry2 = Entry(root2,textvariable=self.add,font=("courier",20,"bold"),fg="black",bg="white").place(x = 700,y = 350)

        lab4 = Label(root2,text="DIESEASE NAME              :",font=("courier",20,"bold"),fg="black",bg="white").place(x = 200,y = 400)
        entry2 = Entry(root2,textvariable=self.disease1,font=("courier",20,"bold"),fg="black",bg="white").place(x = 700,y = 400)

        lab4 = Label(root2,text="DOCTOR'S NAME              :",font=("courier",20,"bold"),fg="black",bg="white").place(x = 200,y = 450)
        entry2 = Entry(root2,textvariable=self.doctor,font=("courier",20,"bold"),fg="black",bg="white").place(x = 700,y = 450)

        lab4 = Label(root2,text="FEES                       :",font=("courier",20,"bold"),fg="black",bg="white").place(x = 200,y = 500)
        entry2 = Entry(root2,textvariable=self.fees,font=("courier",20,"bold"),fg="black",bg="white").place(x = 700,y = 500)

        lab4 = Label(root2,text="DEPOSITE AMOUNT            :",font=("courier",20,"bold"),fg="black",bg="white").place(x = 200,y = 550)
        entry2 = Entry(root2,textvariable=self.deposite,font=("courier",20,"bold"),fg="black",bg="white").place(x = 700,y = 550)




        # submit = partial(submit,name,father,dob,add,disease,doctor,fees,deposite)

        but1 = Button(root2,text="SUBMIT",font=("courier",40,"bold"),fg="blue",bg="white",command=submit).place(x = 750,y=630)
        # but1 = Button(root2,text="CREATE",font=("courier",60,"bold"),fg="blue",bg="white").place(x = 200,y=550)
    
root2 = Tk()
obj = APP(root2)
root2.mainloop()
