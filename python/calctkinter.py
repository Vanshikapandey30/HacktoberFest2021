from tkinter import * #importing everything from tkinter module
x = '' #global var to keep track every entry
root = Tk()  #formation of root window
var = StringVar() #declaring string var that can change in widgets


def var_set(v): #func to set value of StringVar
    global x
    x += v  #adding entry to x each time a button pressed
    var.set(x)


def eval_fun(): #for evalution of string
    r = e.get() #get entry value as string
    var.set(eval(r)) #evalution of string

def clr_fun(): #to clear entry widget
    global x
    x = ''
    var.set('')


def bk_sp(): #function to perform backspacing
    global x
    x = x[:-1] #removing last char from string
    var.set(x) #updating var's value

e = Entry(root,textvariable=var,width=50,bg="#000000",fg="#FFFFFF",relief=RIDGE,bd=23) #Entry widget to take entries and show them
e.grid(row=0,column=0,columnspan=3,sticky='WE') #placing entry widget into root window

bk = Button(root,text='DEL',command=lambda:bk_sp(),width=16,height=3,bg='#666666',fg='#FFFFFF',relief=RIDGE,bd=5) #back space button
bk.grid(row=0,column=3) #attaching the backspace button to it's place

bclr = Button(root,text='CLR',command=lambda:clr_fun(),width=16,height=2,bg='#666666',fg='#FFFFFF',relief=RIDGE,bd=5) #Clear Button
bclr.grid(row=5,column=1) #crating a Clear button which will wipe the screen for next calcultation

bq = Button(root,text='QUIT',command=lambda:root.destroy(),width=16,height=2,bg='#666666',fg='#FFFFFF',relief=RIDGE,bd=5) #Quit Button
bq.grid(row=5,column=0)


b9 = Button(root,text="9",command=lambda:var_set('9'),width=16,height=2, bg='#666666', fg='#FFFFFF',relief=RIDGE,bd=5)
b8 = Button(root,text="8",command=lambda:var_set('8'),width=16,height=2, bg='#666666', fg='#FFFFFF',relief=RIDGE,bd=5)
b7 = Button(root,text="7",command=lambda:var_set('7'),width=16,height=2, bg='#666666', fg='#FFFFFF',relief=RIDGE,bd=5)
b6 = Button(root,text="6",command=lambda:var_set('6'),width=16,height=2, bg='#666666', fg='#FFFFFF',relief=RIDGE,bd=5)
b5 = Button(root,text="5",command=lambda:var_set('5'),width=16,height=2, bg='#666666', fg='#FFFFFF',relief=RIDGE,bd=5)
b4 = Button(root,text="4",command=lambda:var_set('4'),width=16,height=2, bg='#666666', fg='#FFFFFF',relief=RIDGE,bd=5)
b3 = Button(root,text="3",command=lambda:var_set('3'),width=16,height=2, bg='#666666', fg='#FFFFFF',relief=RIDGE,bd=5)
b2 = Button(root,text="2",command=lambda:var_set('2'),width=16,height=2, bg='#666666', fg='#FFFFFF',relief=RIDGE,bd=5)
b1 = Button(root,text="1",command=lambda:var_set('1'),width=16,height=2, bg='#666666', fg='#FFFFFF',relief=RIDGE,bd=5)
b0 = Button(root,text="0",command=lambda:var_set('0'),width=16,height=2, bg='#666666', fg='#FFFFFF',relief=RIDGE,bd=5)


b9.grid(row=1,column=0)
b8.grid(row=1,column=1)
b7.grid(row=1,column=2)
b6.grid(row=2,column=0)
b5.grid(row=2,column=1)
b4.grid(row=2,column=2)
b3.grid(row=3,column=0)
b2.grid(row=3,column=1)
b1.grid(row=3,column=2)
b0.grid(row=4,column=1)

bb = Button(root,text=".",command=lambda:var_set('.'),width=16,height=2, bg='#666666', fg='#FFFFFF',relief=RIDGE,bd=5)
be = Button(root,text="=",command=lambda:eval_fun(),  width=16,height=2, bg='#666666', fg='#FFFFFF',relief=RIDGE,bd=5)
bp = Button(root,text="+",command=lambda:var_set('+'),width=16,height=2, bg='#666666', fg='#FFFFFF',relief=RIDGE,bd=5)
bs = Button(root,text="-",command=lambda:var_set('-'),width=16,height=2, bg='#666666', fg='#FFFFFF',relief=RIDGE,bd=5)
bm = Button(root,text="*",command=lambda:var_set('*'),width=16,height=2, bg='#666666', fg='#FFFFFF',relief=RIDGE,bd=5)
bd = Button(root,text="/",command=lambda:var_set('/'),width=16,height=2, bg='#666666', fg='#FFFFFF',relief=RIDGE,bd=5)
pb = Button(root,text="**",command=lambda:var_set('**'),width=16,height=2,bg='#666666',fg='#FFFFFF',relief=RIDGE,bd=5)
mb = Button(root,text="%",command=lambda:var_set('%'),width=16,height=2,  bg='#666666',fg='#FFFFFF',relief=RIDGE,bd=5)



bb.grid(row=4,column=0)
be.grid(row=4,column=2)
bp.grid(row=1,column=3)
bs.grid(row=2,column=3)
bm.grid(row=3,column=3)
bd.grid(row=4,column=3)
pb.grid(row=5,column=2)
mb.grid(row=5,column=3)


root.wm_resizable(0,0) #will not be resizalbe hight or width of the window

root.wm_title("BASIC CALCULATOR") #setting up title for the window

img = PhotoImage(file="small.gif") #open image small.gif from current folder (place one gif image with name small.gif in current directory)
root.wm_iconphoto(root,img) #set img as icon on window
root.bell()#rings a display's bell
mainloop() #window starts from here
