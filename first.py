from tkinter import *
import time

root = Tk()
root.geometry("1600x800")
root.config(bg="blue")
lab = Label(root,text="WEL COME",font= ("courier",100,"bold"),fg="orange",bg="blue").place(x = 500,y=100)
lab1 = Label(root,text="TO",font=("courier",100,"bold"),fg="white",bg="blue").place(x=700,y=250)
lab2 = Label(root,text="QUIZ GAME",font=("courier",100,"bold"),fg= "green",bg="blue").place(x=465,y=400)

def hello():
    user = StringVar
    pas = StringVar
    root2 = Tk()
    root2.geometry("1600x800")
    root2.config(bg = "white")

    lab1 = Label(root2,text="QUIZ GAME",font=("courier",80,"bold"),fg="red",bg="white").place(x = 450,y = 50)
    lab2 = Label(root2,text="LOGIN",font=("courier",80,"bold"),fg="black",bg="white").place(x = 500,y = 150)
    lab3 = Label(root2,text="USER NAME     :",font=("courier",40,"bold"),fg="black",bg="white").place(x = 200,y = 350)
    lab4 = Label(root2,text="PASSWORD      :",font=("courier",40,"bold"),fg="black",bg="white").place(x = 200,y = 450)

    entry1 = Entry(root2,textvariable=user,font=("courier",40,"bold"),fg="black",bg="white").place(x = 720,y = 350)
    entry2 = Entry(root2,textvariable=pas,font=("courier",40,"bold"),fg="black",bg="white",show="*").place(x = 720,y = 450)

    but1 = Button(root2,text="SUBMIT",font=("courier",60,"bold"),fg="blue",bg="white").place(x = 750,y=550)
    but1 = Button(root2,text="CREATE",font=("courier",60,"bold"),fg="blue",bg="white").place(x = 200,y=550)
    
    root2.mainloop()


def start():
    root1 = Tk()
    root1.geometry("1600x800")
    root1.config(bg="green")
    but1 = Button(text="START",font=("courier",100,"bold"),fg="red",bg = "green",command=hello).place(x=550,y=200)
    
    root1.mainloop()
def countdown(time):
    if time == -1:
        root.destroy()
        start()

    root.after(1000, countdown, time-1)


countdown(3)

# root.mainloop()
root.mainloop()