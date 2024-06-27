from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql 
from login_f.login_file import login

def register():
    def click_register():
        id=entry_id.get()
        name=entry_name.get()
        email=entry_email.get()
        psw=entry_password.get()
        role=var.get()

        if (id=="" or psw=="" or name=="" or email=="" or role==""):
            MessageBox.showinfo("Alert","Enter all Credentials")
        else:
            con=mysql.connect(host="localhost",user="root",password="AMAN9598",database="appointmentlogin",auth_plugin='mysql_native_password')
            cursor=con.cursor()
            cursor.execute("insert into registration values('"+id+"','"+name+"','"+email+"','"+psw+"','"+role+"')")
            cursor.execute("commit")

            MessageBox.showinfo("Alert","Registration completed Successfully")
            con.close()
            login()

    f1=Frame(bg="#ADD8E6")
    f1.place(x=0,y=0,height=500,width=500)
    
    var = StringVar()
    var.set("Appointment Taker") 
    
    l1=Label(f1,text="User Id:",font=("Verdena 15"),fg="#000080",bg="#ADD8E6")
    l2=Label(f1,text="Name:",font=("Verdena 15"),fg="#000080",bg="#ADD8E6")
    l3=Label(f1,text="Email",font=("Verdena 15"),fg="#000080",bg="#ADD8E6")
    l4=Label(f1,text="Password:",font=("Verdena 15"),fg="#000080",bg="#ADD8E6")
    l5=Label(f1,text="Select Your Role:",font=("Verdena 15"),fg="#000080",bg="#ADD8E6")
    radiobutton1 = Radiobutton(f1, text="Appointment Taker  ", variable=var, value="Appointment Taker",fg="#000080",bg="#ADD8E6")
    radiobutton2 = Radiobutton(f1, text="Appointment Seeker", variable=var, value="Appointment Seeker",fg="#000080",bg="#ADD8E6")

    l1.place(x=100,y=100)
    l2.place(x=100,y=150)
    l3.place(x=100,y=200)
    l4.place(x=100,y=250)
    l5.place(x=100,y=300)
    radiobutton1.place(x=280,y=300)
    radiobutton2.place(x=280,y=330)

    entry_id=Entry(f1,font=("Verdena 15"))
    entry_name=Entry(f1,font=("Verdena 15"))
    entry_email=Entry(f1,font=("Verdena 15"))
    entry_password=Entry(f1,font=("Verdena 15"),show="*")

    entry_id.place(x=200,y=100)
    entry_name.place(x=200,y=150)
    entry_email.place(x=200,y=200)
    entry_password.place(x=200,y=250)

    b1=Button(f1,text="Register",font=("Verdena 15"),fg="#000080",bg="#FFFFFF",command=click_register)
    b2=Button(f1,text="LogIn",font=("Verdena 15"),fg="#000080",bg="#FFFFFF",command=login)
    b1.place(x=150,y=450)
    b2.place(x=250,y=450)