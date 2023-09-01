# this is the beginning of Calculator project

# importing required libraries
from tkinter import *
from tkinter import PhotoImage

result = 0

window = Tk()
window.minsize(300,435)
window.maxsize(300,435)
window.title("Calculator")
icon = PhotoImage(file="icon.png")
window.iconphoto(True, icon)
window.config(background='#000')

# Defining Colors
num_color = '#313131'
sym_color = '#F69906'

# Defining click function
def click(event):
    global expressionVal
    global result
    # cget() method is used to get value from button 
    text = event.widget.cget('text')

    if text == "=":
        if expressionVal.get().isdigit():
            result = int(expression.get())
        else:
            try:
                result = eval(expression.get())
                expressionVal.set(result)
            except:
                expressionVal.set("Error")

    elif text == "<<":
        new_exp = expressionVal.get()
        new_exp = new_exp[: -1]
        expressionVal.set(new_exp)

    elif text == 'C':
        result = 0  # Clear the result
        expressionVal.set('')
        expression.update()
    elif text == "%":
        result = int(expressionVal.get())
        result = result/100
        expressionVal.set(result)
    else:
        if result != 0:
            # Clear the result if it's not zero
            result = 0
            expressionVal.set('')
            expression.update()
        expressionVal.set(expressionVal.get() + text)
        expression.update()

     

# Creating variable for storing result of math expression
expressionVal = StringVar()

# Creating Entry widget for Answer Expression
expression = Entry(window, textvariable= expressionVal, font=('Lucida', 40, 'bold'), bg='#000', fg='#fff')
expression.pack(fill=X, ipadx=8, pady=10, padx=10)

# Creating frame for buttons
myframe = Frame(window)
myframe.pack()

# Creating Numbers and Operator Buttons
b1 = Button(myframe, text='C', font=('lucida', 25, 'bold'), width=3, bg=num_color, fg='#fff')
b1.grid(row=0, column=0)
b1.bind('<Button-1>', click)

b2 = Button(myframe, text='<<', font=('lucida', 25, 'bold'), width=3, bg=num_color, fg='#fff')
b2.grid(row=0, column=1)
b2.bind('<Button-1>', click)

b3 = Button(myframe, text='%', font=('lucida', 25, 'bold'), width=3, bg=num_color, fg='#fff')
b3.grid(row=0, column=2)
b3.bind('<Button-1>', click)

b4 = Button(myframe, text='/', font=('lucida', 25, 'bold'), width=3, bg=sym_color, fg='#fff')
b4.grid(row=0, column=3)
b4.bind('<Button-1>', click)

b5 = Button(myframe, text='7', font=('lucida', 25, 'bold'), width=3, bg=num_color, fg='#fff')
b5.grid(row=1, column=0)
b5.bind('<Button-1>', click)

b6 = Button(myframe, text='8', font=('lucida', 25, 'bold'), width=3, bg=num_color, fg='#fff')
b6.grid(row=1, column=1)
b6.bind('<Button-1>', click)

b7 = Button(myframe, text='9', font=('lucida', 25, 'bold'), width=3, bg=num_color, fg='#fff')
b7.grid(row=1, column=2)
b7.bind('<Button-1>', click)

b8 = Button(myframe, text='*', font=('lucida', 25, 'bold'), width=3, bg=sym_color, fg='#fff')
b8.grid(row=1, column=3)
b8.bind('<Button-1>', click)

b9 = Button(myframe, text='4', font=('lucida', 25, 'bold'), width=3, bg=num_color, fg='#fff')
b9.grid(row=2, column=0)
b9.bind('<Button-1>', click)

b10 = Button(myframe, text='5', font=('lucida', 25, 'bold'), width=3, bg=num_color, fg='#fff')
b10.grid(row=2, column=1)
b10.bind('<Button-1>', click)

b11 = Button(myframe, text='6', font=('lucida', 25, 'bold'), width=3, bg=num_color, fg='#fff')
b11.grid(row=2, column=2)
b11.bind('<Button-1>', click)

b12 = Button(myframe, text='-', font=('lucida', 25, 'bold'), width=3, bg=sym_color, fg='#fff')
b12.grid(row=2, column=3)
b12.bind('<Button-1>', click)


b13 = Button(myframe, text='1', font=('lucida', 25, 'bold'), width=3, bg=num_color, fg='#fff')
b13.grid(row=3, column=0)
b13.bind('<Button-1>', click)

b14 = Button(myframe, text='2', font=('lucida', 25, 'bold'), width=3, bg=num_color, fg='#fff')
b14.grid(row=3, column=1)
b14.bind('<Button-1>', click)

b15 = Button(myframe, text='3', font=('lucida', 25, 'bold'), width=3, bg=num_color, fg='#fff')
b15.grid(row=3, column=2)
b15.bind('<Button-1>', click)

b16 = Button(myframe, text='+', font=('lucida', 25, 'bold'), width=3, bg=sym_color, fg='#fff')
b16.grid(row=3, column=3)
b16.bind('<Button-1>', click)

b17 = Button(myframe, text='0', font=('lucida', 25, 'bold'), width=3, bg=num_color, fg='#fff')
b17.grid(row=4,column=0 ,columnspan=2, sticky='nsew')
b17.bind('<Button-1>', click)

b18 = Button(myframe, text='.', font=('lucida', 25, 'bold'), width=3, bg=num_color, fg='#fff')
b18.grid(row=4, column=2)
b18.bind('<Button-1>', click)

b19 = Button(myframe, text='=', font=('lucida', 25, 'bold'), width=3, bg=sym_color, fg='#fff')
b19.grid(row=4, column=3)
b19.bind('<Button-1>', click)

# b20 = Button(myframe, text='\\', font=('lucida', 25, 'bold'), width=3)
# b20.grid(row=4, column=3)
# b20.bind('<Button-1>', click)

window.mainloop()