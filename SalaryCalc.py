# This is a simple salary calculator.
#It takes total number of hours and rate per hour as the input and spits out the total salary calculated.
#Created by : Aanchal Sharma


from tkinter import *
from tkinter import ttk

SalaryCalc=Tk()
SalaryCalc.title('Salary Calculator')
SalaryCalc.geometry('600x200+200+200')

def Salarycalculator():
     hrs=float(hoursinput.get())
     sal=float(salaryinput.get())
     total=sal*hrs
     FinalResult=ttk.Label( SalaryCalc, text=' Total Salary is : %.2f CAD'%total).grid(row= 12 , column=2)
salaryinput=StringVar()
hoursinput=StringVar()


label1=ttk.Label(SalaryCalc , text='This is a simple Salary Calculator' ,relief=SUNKEN,
                 font=('Courier',14,'bold') , foreground='blue' , background='blue').grid(row=2,column=2)

label2=ttk.Label(SalaryCalc , text='Enter the rate per hour' , justify=LEFT,anchor=W,relief=SUNKEN,
                 font=('Courier',12,'bold') , foreground='red' ).grid(row=8,column=0)
label3=ttk.Label(SalaryCalc , text='Enter total number of hours' ,justify=LEFT,anchor=W,relief=SUNKEN,
                 font=('Courier',12,'bold') , foreground='red' ).grid(row=9,column=0)

Salary=Entry(SalaryCalc , textvariable=salaryinput).grid(row=8 , column=2)
Salary=Entry(SalaryCalc , textvariable=hoursinput).grid(row=9 , column=2)

button1=ttk.Button(SalaryCalc , text='Calculate',command=Salarycalculator)
button1.grid(row=10 , column=0)





SalaryCalc.mainloop()
