from tkinter import *
from tkinter import ttk
import tkinter
from main import mockfunction
window = Tk()
name = tkinter.StringVar()
wakeup = tkinter.StringVar()
hobbies = tkinter.StringVar()
ocupation = tkinter.StringVar()
work = tkinter.StringVar()
sleep = tkinter.StringVar()
food = tkinter.StringVar()

window.title("Welcome to TutorialsPoint")
window.geometry('400x400')
window.configure(background = "grey");
a = Label(window ,text = "Enter your name").grid(row = 0,column = 0)
b = Label(window ,text = "What do you do when you wake up?").grid(row = 1,column = 0)
c = Label(window ,text = "What are your hobbies?").grid(row = 2,column = 0)
d = Label(window ,text = "What is your ocupation?").grid(row = 3,column = 0)
e = Label(window ,text = "Where do you study/work?").grid(row = 4,column = 0)
f = Label(window ,text = "What do you do before going to sleep?").grid(row = 5,column = 0)
g = Label(window ,text = "What is your favorite food").grid(row = 6,column = 0)

a1 = ttk.Entry(window,textvariable=name).grid(row = 0,column = 1)
b1 = Entry(window,textvariable=wakeup).grid(row = 1,column = 1)
c1 = Entry(window,textvariable=hobbies).grid(row = 2,column = 1)
d1 = Entry(window,textvariable=ocupation).grid(row = 3,column = 1)
e1 = Entry(window,textvariable=work).grid(row = 4,column = 1)
f1 = Entry(window,textvariable=sleep).grid(row = 5,column = 1)
g1 = Entry(window,textvariable=food).grid(row = 6,column = 1)
def clicked():
   res = "Welcome to " + txt.get()
   lbl.configure(text= res)
def createStory():
    answers = [name.get(),wakeup.get(),hobbies.get(),ocupation.get(),work.get(),sleep.get(),food.get() ]
    
btn = ttk.Button(window ,text="Submit",command=createStory).grid(row=7,column=0)
window.mainloop()