import tkinter as tk
import game as g

root = tk.Tk()
root.config(bg="green")
root.geometry("1600x800")
label1 = tk.Label(root,text = "----Welcome to Snake Game----",bg="green",fg="red",font=("classic",80,"bold"))
label1.grid()

def s(g):
    # root.iconify
    g.access

but1 = tk.Button(root,text="START",bg="black",fg="red",font=("classic",50,"bold"),command = s(g))
but1.grid(padx=330,pady=120)

root.mainloop()