#!/usr/bin/python3

from tkinter import *
from tkinter.ttk import *


m = Tk(className = 'ddsb calculator')



# S T Y L I N G : 
#m.geometry('400x250')       # Fix the size of the calculator tab. PS : use character 'x' instead of '*'.
style = Style()

style.configure('TButton', font = ('Calibri', 10, 'bold'), foreground = 'black')
# for styling specific buttons, use 'W.TButton' and then add style = 'W.Tbutton' in that button's parameters.   
# using 'TButton' styles all the buttons.





# D I S P L A Y :
res = ""                  # global var.
result = StringVar()      # to update the display text.
display = Entry(m, textvariable = result, width = 46, justify = 'right', foreground = 'red')     
                   # text can be updated.
                   # can use 'Entry' or 'Label'.

result.set(" E N T E R    Y O U R     E X P R E S S I O N ")
display.grid(columnspan = 4)






# B U T T O N S :

# each button will have m(master), text and a function (same for all buttons except '=' and 'C').

# functions :
def press(num) :    # update var on press
    global res
    res = res + str(num)
    result.set(res)

def equal() :
    global res
    total = str(eval(res))
    result.set(total)
    res = ""

def clear() :
    global res
    res = ""
    result.set("")



# button 'grid layout' : 
b0 = Button(m, text = "0", command = lambda : press(0))
b0.grid(row = 4, column = 1)

b1 = Button(m, text = "1", command = lambda : press(1))
b1.grid(row = 1, column = 0)

b2 = Button(m, text = "2", command = lambda : press(2))
b2.grid(row = 1, column = 1)

b3 = Button(m, text = "3", command = lambda : press(3))
b3.grid(row = 1, column = 2)

b4 = Button(m, text = "4", command = lambda : press(4))
b4.grid(row = 2, column = 0)

b5 = Button(m, text = "5", command = lambda : press(5))
b5.grid(row = 2, column = 1)

b6 = Button(m, text = "6", command = lambda : press(6))
b6.grid(row = 2, column = 2)

b7 = Button(m, text = "7", command = lambda : press(7))
b7.grid(row = 3, column = 0)

b8 = Button(m, text = "8", command = lambda : press(8))
b8.grid(row = 3, column = 1)

b9 = Button(m, text = "9", command = lambda : press(9))
b9.grid(row = 3, column = 2)

b_plus = Button(m, text = "+", command = lambda : press("+"))
b_plus.grid(row = 1, column = 3)

b_minus = Button(m, text = " - ", command = lambda : press("-"))
b_minus.grid(row = 2, column = 3)

b_mul = Button(m, text = " * ", command = lambda : press("*"))
b_mul.grid(row = 3, column = 3)

b_div = Button(m, text = " / ", command = lambda : press("/"))
b_div.grid(row = 4, column = 3)

#button with different function :
b_equal = Button(m, text = "=", command = equal)
b_equal.grid(row = 4, column = 2)

b_clear = Button(m, text = "C", command = clear)
b_clear.grid(row = 4, column = 0)





# E X E C U T E : 
m.mainloop()
