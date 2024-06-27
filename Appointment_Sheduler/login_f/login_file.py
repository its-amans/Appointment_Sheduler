from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql 
from Appointyment_Seeker.book_seeker import *
from Appointyment_Seeker.cancel_seeker import *
from Appointyment_Seeker.veiw_seeker import *
from Appointment_Taker.set_taker import *
from Appointment_Taker.cancel_taker import *
from Appointment_Taker.veiw_taker import *

def manage_appointment():
    f3=Frame(bg="#FAFAD2")
    f3.place(x=0,y=0,height=500,width=500)

    l2=Label(f3,text="Cancel Appointment:",font=("Verdena 15"),fg="#000000",bg="#FAFAD2")
    l3=Label(f3,text="Veiw Appointment:",font=("Verdena 15"),fg="#000000",bg="#FAFAD2")

    l2.place(x=100,y=200)
    l3.place(x=100,y=250)

    b2=Button(f3,text="Click Here",font=("Verdena 15"),fg="#000000",bg="#DAA520",command=cancel_ap_taker)
    b3=Button(f3,text="Click Here",font=("Verdena 15"),fg="#000000",bg="#DAA520",command=veiw_ap_taker)
    b2.place(x=300,y=200)
    b3.place(x=300,y=250)
    b1=Button(f3,text="Go To Homepage",font=("Verdena 15"),fg="#000000",bg="#DAA520",command=appointmenttaker)
    b1.place(x=150,y=400)
def appointmentseeker():
    
    f3=Frame(bg="#F08080")
    f3.place(x=0,y=0,height=500,width=500)
    l=Label(f3,text="Welcome to Appointment Sheduler",font=("Verdena 20"),fg="white",bg="#F08080")
        
    l1=Label(f3,text="Book Appointment:",font=("Verdena 15"),fg="white",bg="#F08080")
    l2=Label(f3,text="Cancel Appointment:",font=("Verdena 15"),fg="white",bg="#F08080")
    l3=Label(f3,text="Veiw Appointment:",font=("Verdena 15"),fg="white",bg="#F08080")
        
    l.place(x=30,y=50)
    l1.place(x=100,y=200)
    l2.place(x=100,y=250)
    l3.place(x=100,y=300)
        
    b1=Button(f3,text="Click Here",font=("Verdena 15"),fg="white",bg="#8B0000",command=book_appointment)
    b2=Button(f3,text="Click Here",font=("Verdena 15"),fg="white",bg="#8B0000",command=cancel_ap_seeker)
    b3=Button(f3,text="Click Here",font=("Verdena 15"),fg="white",bg="#8B0000",command=veiw_ap_seeker)
    b1.place(x=300,y=200)
    b2.place(x=300,y=250)
    b3.place(x=300,y=300)
    b1=Button(f3,text="Go To Homepage",font=("Verdena 15"),fg="white",bg="#8B0000",command=login)
    b1.place(x=180,y=420)


def appointmenttaker():    
    f4=Frame(bg="#F5FFFA")
    f4.place(x=0,y=0,height=500,width=500)
        
    l=Label(f4,text="Welcome to Appointment Sheduler",font=("Verdena 20"),fg="#006400",bg="#F5FFFA")
    l1=Label(f4,text="Manage Appointment:",font=("Verdena 15"),fg="#006400",bg="#F5FFFA")
    l2=Label(f4,text="Set Availability:",font=("Verdena 15"),fg="#006400",bg="#F5FFFA")
        
    l.place(x=30,y=50)
    l1.place(x=90,y=200)
    l2.place(x=90,y=250)
        
    b1=Button(f4,text="Click Here",font=("Verdena 15"),fg="white",bg="#2E8B57",command=manage_appointment)
    b3=Button(f4,text="Click Here",font=("Verdena 15"),fg="white",bg="#2E8B57",command=set_availability)
    b1.place(x=300,y=200)
    b3.place(x=300,y=250)
        
    b4=Button(f4,text="Go To Homepage",font=("Verdena 15"),fg="white",bg="#2E8B57",command=login)
    b4.place(x=150,y=400)
def login():
    def click_login(role_input):
        id=entry_id.get()
        email=entry_email.get()
        psw=entry_password.get()
        
        con=mysql.connect(host="localhost",user="root",password="AMAN9598",database="appointmentlogin",auth_plugin='mysql_native_password')
        cursor=con.cursor()
        cursor.execute("SELECT Userid FROM registration")
        database_id=cursor.fetchall()
        cursor.execute("SELECT Email FROM registration")
        database_email=cursor.fetchall()
        cursor.execute("SELECT Password FROM registration")
        database_psw=cursor.fetchall()
        cursor.execute("SELECT Role FROM registration")
        database_role=cursor.fetchall()
        
        var1=0
        var2=0
        var3=0
        var4=0
        var5=0
        
        
        for userrole in database_role:
            url=userrole[0]
            if url==role_input=="Appointment Taker":
                var4=1
            elif url==role_input=="Appointment Seeker":
                var5=1
                
        for userid in database_id:
            uid=userid[0]
            u=str(uid)
            if(u==id):
                var1=1    
        for useremail in database_email:
            uml=useremail[0]
            if(uml==email):
                var2=1    
        for userpsw in database_psw:
            upw=userpsw[0]
            if(upw==psw):
                var3=1    
                
        if (id=="" or psw=="" or email==""):
            MessageBox.showinfo("Alert","Enter all Credentials")
        elif(var1==1 and var2==1 and var3==1) :
            if(var4==1):
                appointmenttaker()
            elif(var5==1):
                appointmentseeker()        
        else:
            MessageBox.showinfo("Alert","There is error")
            
        
    f1=Frame(bg="#E0FFFF")
    f1.place(x=0,y=0,height=500,width=500)
    
    label_head=Label(f1,text="Fill credentials To Login",font=("Verdena 25"),fg="#2F4F4F",bg="#E0FFFF")
    label_head.place(x=80,y=10)
    
    var = StringVar()
    var.set("Appointment Taker") 
    
    l1=Label(f1,text="User Id:",font=("Verdena 15"),fg="#2F4F4F",bg="#E0FFFF")
    l2=Label(f1,text="Email",font=("Verdena 15"),fg="#2F4F4F",bg="#E0FFFF")
    l3=Label(f1,text="password",font=("Verdena 15"),fg="#2F4F4F",bg="#E0FFFF")
    l4=Label(f1,text="Select Your Role:",font=("Verdena 15"),fg="#2F4F4F",bg="#E0FFFF")
    radiobutton1 = Radiobutton(f1, text="Appointment Taker  ", variable=var, value="Appointment Taker",fg="#2F4F4F",bg="#E0FFFF")
    radiobutton2 = Radiobutton(f1, text="Appointment Seeker", variable=var, value="Appointment Seeker",fg="#2F4F4F",bg="#E0FFFF")
    
    l1.place(x=100,y=100)
    l2.place(x=100,y=150)
    l3.place(x=100,y=200)
    l4.place(x=100,y=250)
    radiobutton1.place(x=280,y=250)
    radiobutton2.place(x=280,y=280)
    
    entry_id=Entry(f1,font=("Verdena 15"))
    entry_email=Entry(f1,font=("Verdena 15"))
    entry_password=Entry(f1,font=("Verdena 15"),show="*")

    entry_id.place(x=200,y=100)
    entry_email.place(x=200,y=150)
    entry_password.place(x=200,y=200)
    
    b1=Button(f1,text="LogIn",font=("Verdena 15"),fg="white",bg="#008080",command=lambda:click_login(var.get()))
    from registration.register_f import register
    b2=Button(f1,text="Register",font=("Verdena 15"),fg="white",bg="#008080",command=register)
    b1.place(x=150,y=400)
    b2.place(x=250,y=400)
