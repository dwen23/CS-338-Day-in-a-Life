from cProfile import label
from tkinter import *
from tkinter import ttk
import tkinter
from main import input
window = Tk()
name = tkinter.StringVar()
wakeup = tkinter.StringVar()
hobbies = tkinter.StringVar()
ocupation = tkinter.StringVar()
work = tkinter.StringVar()
sleep = tkinter.StringVar()
food = tkinter.StringVar()

window.title("Welcome to TutorialsPoint")
window.geometry('1600x1600')
window.configure(background = "grey");
a = Label(window ,text = "Enter your name",font=("Arial",25)).grid(row = 0,column = 4,columnspan=3)
b = Label(window ,text = "What do you do when you wake up?",font=("Arial",25)).grid(row = 1,column = 4,columnspan=3)
c = Label(window ,text = "What are your hobbies?",font=("Arial",25)).grid(row = 2,column = 4,columnspan=3)
d = Label(window ,text = "What is your ocupation?",font=("Arial",25)).grid(row = 3,column = 4,columnspan=3)
e = Label(window ,text = "Where do you study/work?",font=("Arial",25)).grid(row = 4,column = 4,columnspan=3)
f = Label(window ,text = "What do you do before going to sleep?",font=("Arial",25)).grid(row = 5,column = 4,columnspan=3)
g = Label(window ,text = "What is your favorite food",font=("Arial",25)).grid(row = 6,column = 4,columnspan=3)

a1 = ttk.Entry(window,textvariable=name).grid(row = 0,column = 8, columnspan=3)
b1 = Entry(window,textvariable=wakeup).grid(row = 1,column = 8,columnspan=3)
c1 = Entry(window,textvariable=hobbies).grid(row = 2,column = 8,columnspan=3)
d1 = Entry(window,textvariable=ocupation).grid(row = 3,column = 8,columnspan=3)
e1 = Entry(window,textvariable=work).grid(row = 4,column = 8,columnspan=3)
f1 = Entry(window,textvariable=sleep).grid(row = 5,column = 8,columnspan=3)
g1 = Entry(window,textvariable=food).grid(row = 6,column = 8,columnspan=3)

def createStory():
    answers = {"name": name.get(), "wakeup": wakeup.get(),"ocupation": ocupation.get(),"workplace": work.get(), "hobbies": hobbies.get(), "food": food.get(), "sleep": sleep.get()}

    Label(window, text = input(answers),wraplength=1000, font=("Arial",36)).grid(row = 10, column = 0)

#myFont = tkinter.font.Font(size = 30)
btn = ttk.Button(window ,text="Submit",command=createStory).grid(row=7,column=4)
#btn['font'] = myFont
window.mainloop()