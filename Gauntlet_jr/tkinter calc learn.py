"""
Name: Tkinter Calculator Basic
Description: Basic calculator calc using tkinter library
Author: Jakub
Date:17/05/2024
Note: Geeks for geeks was helpful in setting out the basics, turns out the code
is really simple xD


"""
from tkinter import *

expression = ""
#the function below is to update the expression
def press(num):
    #need expression as a global var
    global expression 
    
    
    expression=expression+str(num)
    
    equation.set(expression)


def equalpress():
    #The try and except loop stops errors like zero erro division from happening
    try:
        global expression
        
        total= str(eval(expression))
        
        equation.set(total)
        
        expression = ""
    
    except:
        
        equation.set("Error")
        expression = ""

def clear():
    
    global expression
    expression = ""
    equation.set("")


#MAIN

calc=Tk()

calc.configure(background="light blue")

calc.title("Calculator")

calc.geometry("400x300")

#Use string var class to make equations
equation = StringVar()

entry = Entry(calc,textvariable=equation)

entry.grid(columnspan=4,ipadx=100)

"""

Ngl this is just copy and paste at this point once everything is set up :)
Basic idea is that it uses lambda functions to do the press function and then
pop up the action on the entry screen. Python does the rest of the magic.
This works for basic functions that are already built-in, however more complex functions will need addons 
and tinkering.

"""

button1 = Button(calc, text=' 1 ', fg='white', bg='red', 
                    command=lambda: press(1), height=1, width=7) 
button1.grid(row=2, column=0) 
 
button2 = Button(calc, text=' 2 ', fg='white', bg='red', 
                    command=lambda: press(2), height=1, width=7) 
button2.grid(row=2, column=1) 
 
button3 = Button(calc, text=' 3 ', fg='white', bg='red', 
                    command=lambda: press(3), height=1, width=7) 
button3.grid(row=2, column=2) 
 
button4 = Button(calc, text=' 4 ', fg='white', bg='red', 
                    command=lambda: press(4), height=1, width=7) 
button4.grid(row=3, column=0) 
 
button5 = Button(calc, text=' 5 ', fg='white', bg='red', 
                    command=lambda: press(5), height=1, width=7) 
button5.grid(row=3, column=1) 
 
button6 = Button(calc, text=' 6 ', fg='white', bg='red', 
                    command=lambda: press(6), height=1, width=7) 
button6.grid(row=3, column=2) 
 
button7 = Button(calc, text=' 7 ', fg='white', bg='red', 
                    command=lambda: press(7), height=1, width=7) 
button7.grid(row=4, column=0) 
 
button8 = Button(calc, text=' 8 ', fg='white', bg='red', 
                    command=lambda: press(8), height=1, width=7) 
button8.grid(row=4, column=1) 
 
button9 = Button(calc, text=' 9 ', fg='white', bg='red', 
                    command=lambda: press(9), height=1, width=7) 
button9.grid(row=4, column=2) 
 
button0 = Button(calc, text=' 0 ', fg='white', bg='red', 
                    command=lambda: press(0), height=1, width=7) 
button0.grid(row=5, column=0) 
 
plus = Button(calc, text=' + ', fg='white', bg='red', 
                command=lambda: press("+"), height=1, width=7) 
plus.grid(row=2, column=3) 
 
minus = Button(calc, text=' - ', fg='white', bg='red', 
                command=lambda: press("-"), height=1, width=7) 
minus.grid(row=3, column=3) 
 
multiply = Button(calc, text=' * ', fg='white', bg='red', 
                    command=lambda: press("*"), height=1, width=7) 
multiply.grid(row=4, column=3) 
 
divide = Button(calc, text=' / ', fg='white', bg='red', 
                    command=lambda: press("/"), height=1, width=7) 
divide.grid(row=5, column=3) 
 
equal = Button(calc, text=' = ', fg='white', bg='red', 
                command=equalpress, height=1, width=7) 
equal.grid(row=5, column=2) 
 
clear = Button(calc, text='Clear', fg='white', bg='red', 
                command=clear, height=1, width=7) 
clear.grid(row=5, column='1') 
 
Decimal= Button(calc, text='.', fg='white', bg='red', 
                    command=lambda: press('.'), height=1, width=7) 
Decimal.grid(row=6, column=0) 

"""

This does the basic calculation, the next section will deal with the logic


"""
greater_than = Button(calc, text=' > ', fg='white', bg='red', 
                    command=lambda: press(">"), height=1, width=7) 
greater_than.grid(row=8,column=0)
less_than = Button(calc, text=' < ', fg='white', bg='red', 
                    command=lambda: press("<"), height=1, width=7) 
less_than.grid(row=8,column=1)

gt_eq= Button(calc, text=' >= ', fg='white', bg='red', 
                    command=lambda: press(">="), height=1, width=7) 
gt_eq.grid(row=9,column=0)

lt_eq= Button(calc, text=' <= ', fg='white', bg='red', 
                    command=lambda: press("<="), height=1, width=7) 
lt_eq.grid(row=9,column=1)

equal_to= Button(calc, text=' == ', fg='white', bg='red', 
                    command=lambda: press("=="), height=1, width=7)
equal_to.grid(row=8,column=3) 

n_equal_to=Button(calc, text=' != ', fg='white', bg='red', 
                    command=lambda: press("!="), height=1, width=7)
n_equal_to.grid(row=9,column=3) 


calc.mainloop()   