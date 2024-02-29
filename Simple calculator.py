#SIMPLE CALCULATOR USING PYTHON
from tkinter import*
window =Tk('SIMPLE CALCULATOR')
window.geometry('375x375')
e = Entry(window,width=75,borderwidth=5)
e.place(x=0,y=0)
#Button 
def btclick(num):
    
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(num))
b = Button(window,text='1',width=15,command=lambda:btclick(1))
b.place(x=10,y=60)
b = Button(window,text='2',width=15,command=lambda:btclick(2))
b.place(x=80,y=60)
b = Button(window,text='3',width=15,command=lambda:btclick(3))
b.place(x=170,y=60)
b = Button(window,text='4',width=15,command=lambda:btclick(4))
b.place(x=10,y=120)
b = Button(window,text='5',width=15,command=lambda:btclick(5))
b.place(x=80,y=120)
b = Button(window,text='6',width=15,command=lambda:btclick(6))
b.place(x=170,y=120)
b = Button(window,text='7',width=15,command=lambda:btclick(7))
b.place(x=10,y=180)
b = Button(window,text='8',width=15,command=lambda:btclick(8))
b.place(x=80,y=180)
b = Button(window,text='9',width=15,command=lambda:btclick(9))
b.place(x=170,y=180)
b = Button(window,text='0',width=15,command=lambda:btclick(0))
b.place(x=10,y=240)
#BUTTON FOR OPERATION
#add
def add():
    firstno=e.get()
    global math
    math = 'addition'
    global f
    f=int(firstno)
    e.delete(0,END)
b = Button(window,text='+',width=15,command=add)
b.place(x=80,y=240)


#sub
def sub():
    firstno=e.get()
    global math
    math = 'subtraction'
    global f
    f=int(firstno)
    e.delete(0,END)
b = Button(window,text='-',width=15,command=sub)
b.place(x=170,y=240)


#multiply
def multiply():
    firstno=e.get()
    global math
    math = 'multiplication'
    global f
    f=int(firstno)
    e.delete(0,END)
b = Button(window,text='*',width=15,command=multiply)
b.place(x=10,y=300)


#divide
def divide():
    firstno=e.get()
    global math
    math = 'division'
    global f
    f=int(firstno)
    e.delete(0,END)
b = Button(window,text='/',width=15,command=divide)
b.place(x=80,y=300)


#equal button
def eq():
    secondno=e.get()
    e.delete(0,END)
    if math=='addition':
        e.insert(0,f+int(secondno))
    elif math=='subtraction':
        e.insert(0,f-int(secondno))
    elif math=='multiplication':
        e.insert(0,f*int(secondno))
    elif math=='division':
        e.insert(0,f/int(secondno))
b = Button(window,text='=',width=15,command=eq)
b.place(x=170,y=300)


#clear button
def clear():
    e.delete(0,END)
b = Button(window,text='clear',width=15,command=clear)
b.place(x=10,y=350)
#END OF LOOP 
window.mainloop()
                        
