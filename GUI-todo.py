from tkinter import *
from tkinter import ttk # them of tk
from tkinter import messagebox

GUI = Tk()    # นี่คือหน้าจอหลักของโปรแกรม
GUI.title('โปรแกรม ATM') #นี่คือชื่อโปรแกรม
GUI.geometry('500x400') #นี่คือขนาดหน้าจอของโปรแกรม
L1 = Label(GUI, text='โปรแกรม ATM',font=('Angsana New', 30),fg= 'green')
L1.place(x=70,y=20)
money = 4000  #จำนวนเงินในบัญชี
#--------------------------------
def Button1():
    global money
    money -= 100
    text = f'ถอนเงิน 100 ตอนนี้มีเงินอยู่ในบัญชี {money} บาท' 
    messagebox.showinfo('ถอนเงิน',text)
FB1 = LabelFrame(GUI) #คล้ายกระดาน
FB1.place(x=20, y=100)
B1 = ttk.Button(FB1, text = 'ถอนเงิน 100 บาท', command = Button1)
B1.pack(ipadx=20,ipady=15)
#--------------------------------
def Button2():
    global money
    money -= 500
    text = f'ถอนเงิน 500 ตอนนี้มีเงินอยู่ในบัญชี {money} บาท'
    messagebox.showinfo('ถอนเงิน',text)
FB1 = LabelFrame(GUI) #คล้ายกระดาน
FB1.place(x=20, y=180)
B2 = ttk.Button(FB1, text = 'ถอนเงิน 500 บาท', command = Button2)
B2.pack(ipadx=20,ipady=15)
#--------------------------------
def Button3():
    global money
    money -= 1000
    text = f'ถอนเงิน 1000 ตอนนี้มีเงินอยู่ในบัญชี {money} บาท'
    messagebox.showinfo('ถอนเงิน',text)
FB1 = LabelFrame(GUI) #คล้ายกระดาน
FB1.place(x=20, y=260)
B3 = ttk.Button(FB1, text = 'ถอนเงิน 1000 บาท', command = Button3)
B3.pack(ipadx=17,ipady=15)
#--------------------------------

GUI.mainloop()
