from tkinter import *
from functools import partial



root2 = Tk()
user = StringVar()
pas = StringVar()
root2.geometry("1600x800")
root2.config(bg = "white")
def submit(user,pas):
    root2.destroy()
    print(user.get(),pas.get())

lab1 = Label(root2,text="QUIZ GAME",font=("courier",80,"bold"),fg="red",bg="white").place(x = 450,y = 50)
lab2 = Label(root2,text="LOGIN",font=("courier",80,"bold"),fg="black",bg="white").place(x = 500,y = 150)
lab3 = Label(root2,text="USER NAME     :",font=("courier",40,"bold"),fg="black",bg="white").place(x = 200,y = 350)
lab4 = Label(root2,text="PASSWORD      :",font=("courier",40,"bold"),fg="black",bg="white").place(x = 200,y = 450)

entry1 = Entry(root2,textvariable=user,font=("courier",40,"bold"),fg="black",bg="white").place(x = 720,y = 350)
entry2 = Entry(root2,textvariable=pas,font=("courier",40,"bold"),fg="black",bg="white",show="*").place(x = 720,y = 450)

submit = partial(submit,user,pas)

but1 = Button(root2,text="SUBMIT",font=("courier",60,"bold"),fg="blue",bg="white",command=submit).place(x = 750,y=550)
but1 = Button(root2,text="CREATE",font=("courier",60,"bold"),fg="blue",bg="white").place(x = 200,y=550)

root2.mainloop()