
from tkinter import *
import parser
from math import factorial
from tkinter import ttk, messagebox
from ttkbootstrap import Style

style = Style(theme="flatly")
i = 0

def get_variables(num):
    global i
    display.insert(i,num)
    i += 1
   
def get_operation(operator):
    global i 
    length = len(operator)
    display.insert(i,operator)
    i+=length
    style.configure("Custon.TEntry", foreground="red")


def clear_all():
    display.delete(0,END)

def calcualte():
    entire_string = display.get()
    try:
        a = parser.expr(entire_string).compile()
        result = eval(a)
        clear_all()
        display.insert(0,result)
    except Exception:
        clear_all()
        display.insert(0,"Error try again")

def undo():
    entire_string = display.get()
    if len (entire_string):
        new_string = entire_string[:-1]
        clear_all()
        display.insert(0, new_string)
    else:
        clear_all()
        display.insert(0,"Error try again")

root = Tk()
root.geometry("400x600")
root.resizable(True,True)
root.title("Calculator by Wasi Emmanuela")

display = Entry(root, font = 'arial 20 bold', justify= RIGHT)
display.grid(row = 1, columnspan = 6, sticky = N+E+W+S)


Grid.rowconfigure(root,1,weight=1)
Grid.rowconfigure(root,2,weight=1)
Grid.rowconfigure(root,3,weight=1)
Grid.rowconfigure(root,4,weight=1)
Grid.rowconfigure(root,5,weight=1)
Grid.rowconfigure(root,6,weight=1)
Grid.columnconfigure(root,0,weight=1)
Grid.columnconfigure(root,1,weight=1)
Grid.columnconfigure(root,2,weight=1)
Grid.columnconfigure(root,3,weight=1)



Button(root, text= "1", height= 5, width=10, command = lambda :get_variables(1)).grid(row=2,column=0, sticky=N+S+E+W)
Button(root, text= "2", height= 5, width=10, command = lambda :get_variables(2)).grid(row=2,column=1, sticky=N+S+E+W)
Button(root, text= "3", height= 5, width=10, command = lambda :get_variables(3)).grid(row=2,column=2, sticky=N+S+E+W)

Button(root, text= "4", height= 5, width=10, command = lambda :get_variables(4)).grid(row=3,column=0, sticky=N+S+E+W)
Button(root, text= "5", height= 5, width=10, command = lambda :get_variables(5)).grid(row=3,column=1, sticky=N+S+E+W)
Button(root, text= "6", height= 5, width=10, command = lambda :get_variables(6)).grid(row=3,column=2, sticky=N+S+E+W)

Button(root, text= "7", height= 5, width=10, command = lambda :get_variables(7)).grid(row=4,column=0, sticky=N+S+E+W)
Button(root, text= "8", height= 5, width=10, command = lambda :get_variables(8)).grid(row=4,column=1, sticky=N+S+E+W)
Button(root, text= "9", height= 5, width=10, command = lambda :get_variables(9)).grid(row=4,column=2, sticky=N+S+E+W)

Button(root, text= "AC", height= 5, width=10, command = lambda :clear_all()).grid(row=5,column=0, sticky=N+S+E+W)
Button(root, text= "0", height= 5, width=10, command = lambda :get_variables(0)).grid(row=5,column=1, sticky=N+S+E+W)
Button(root, text= ".", height= 5, width=10, command = lambda :get_variables(".")).grid(row=5,column=2, sticky=N+S+E+W)



Button(root, text= "+", height= 5, width=10, command = lambda :get_operation("+")).grid(row=2,column=3, sticky=N+S+E+W)
Button(root, text= "-", height= 5, width=10, command = lambda :get_operation("-")).grid(row=3,column=3, sticky=N+S+E+W)
Button(root, text= "*", height= 5, width=10, command = lambda :get_operation("*")).grid(row=4,column=3, sticky=N+S+E+W)
Button(root, text= "/", height= 5, width=10, command = lambda :get_operation("/")).grid(row=5,column=3, sticky=N+S+E+W)

Button(root,text="=", height= 5, width=10, command= lambda :calcualte()).grid(row=6,column=0, sticky=N+S+E+W)
Button(root, text= "(", height= 5, width=10, command = lambda :get_variables("(")).grid(row=6,column=1, sticky=N+S+E+W)
Button(root, text= ")", height= 5, width=10, command = lambda :get_variables(")")).grid(row=6,column=2, sticky=N+S+E+W)
Button(root,text="<-", height= 5, width=10, command= lambda :undo()).grid(row=6,column=3, sticky=N+S+E+W)

root.mainloop()