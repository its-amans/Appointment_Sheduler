# This file is used to cancel the appointment by the appointment taker
from login_f.login_file import *
from tkinter import Button, Frame, Label, Radiobutton, StringVar
import mysql.connector as mysql
import tkinter.messagebox as MessageBox
def cancel_ap_taker():
    def cancelled(entry_speciality,entry_availability):
        con=mysql.connect(host="localhost",user="root",password="AMAN9598",database="appointmentlogin",auth_plugin='mysql_native_password')
        cursor=con.cursor()
        cursor.execute("SELECT Speciality FROM appointment_details")
        database_sp=cursor.fetchall()
        cursor.execute("SELECT Availability FROM appointment_details")
        database_av=cursor.fetchall()

        var1=0
        var2=0

        for speciality in database_sp:
            sp=speciality[0]
            if sp==entry_speciality:
                var1=1

        for time in database_av:
            av=time[0]
            if av==entry_availability:
                var2=1

        if (entry_speciality=="" or entry_availability==""):
            MessageBox.showinfo("Alert","Enter all Credentials")
        elif(var1==1 and var2==1) :
            MessageBox.showinfo("Alert","Deleted Succesfully")
            cursor.execute("DELETE FROM appointment_details WHERE Speciality=%s and Availability=%s",(entry_speciality,entry_availability))   
            cursor.execute("commit")
        else:
            MessageBox.showinfo("Alert","There is error")


    f5=Frame(bg="#FFDAB9")
    f5.place(x=0,y=0,height=500,width=500)
    l=Label(f5,text="Cancel Your Appointment",font=("Verdena 20"),fg="#2F4F4F",bg="#FFDAB9")
    l.place(x=70,y=100)

    con=mysql.connect(host="localhost",user="root",password="AMAN9598",database="appointmentlogin",auth_plugin='mysql_native_password')
    cursor=con.cursor()
    cursor.execute("SELECT * FROM appointment_details")
    ap_detail=cursor.fetchall()

    var=StringVar()
    var.set("Doctor")
    radiobutton1 = Radiobutton(f5, text="Doctor", variable=var, value="Doctor",fg="#2F4F4F",bg="#FFDAB9")
    radiobutton2 = Radiobutton(f5, text="BussinessMan", variable=var, value="BussinessMan",fg="#2F4F4F",bg="#FFDAB9")
    radiobutton3 = Radiobutton(f5, text="Influencer", variable=var, value="Influencer",fg="#2F4F4F",bg="#FFDAB9")
    radiobutton4 = Radiobutton(f5, text="Star", variable=var, value="Appointment Seeker",fg="#2F4F4F",bg="#FFDAB9")
    radiobutton5 = Radiobutton(f5, text="Movie Director", variable=var, value="Movie Director",fg="#2F4F4F",bg="#FFDAB9")
    radiobutton6 = Radiobutton(f5, text="Advocate", variable=var, value="Advocate",fg="#2F4F4F",bg="#FFDAB9")
    radiobutton7 = Radiobutton(f5, text="Other", variable=var, value="Other",fg="#2F4F4F",bg="#FFDAB9")

    radiobutton1.place(x=100,y=150)
    radiobutton2.place(x=100,y=180)
    radiobutton3.place(x=100,y=210)
    radiobutton4.place(x=100,y=240)
    radiobutton5.place(x=100,y=270)
    radiobutton6.place(x=100,y=300)
    radiobutton7.place(x=100,y=330)

    var1=StringVar()
    var1.set("7am to 9am")
    l1=Label(f5,text="Choose Your Speciality:",font=("Verdena 20"),fg="#2F4F4F",bg="#FFDAB9")
    radiobutton1 = Radiobutton(f5, text="7am to 9am", variable=var1, value="7am to 9am",fg="#2F4F4F",bg="#FFDAB9")
    radiobutton2 = Radiobutton(f5, text="9am to 11am", variable=var1, value="9am to 11am",fg="#2F4F4F",bg="#FFDAB9")
    radiobutton3 = Radiobutton(f5, text="11am to 1pm", variable=var1, value="11am to 1pm",fg="#2F4F4F",bg="#FFDAB9")
    radiobutton4 = Radiobutton(f5, text="1pm to 3pm", variable=var1, value="1pm to 3pm",fg="#2F4F4F",bg="#FFDAB9")
    radiobutton5 = Radiobutton(f5, text="3pm to 5pm", variable=var1, value="3pm to 5pm",fg="#2F4F4F",bg="#FFDAB9")
    radiobutton6 = Radiobutton(f5, text="5pm to 7pm", variable=var1, value="5pm to 7pm",fg="#2F4F4F",bg="#FFDAB9")
    radiobutton7 = Radiobutton(f5, text="7pm to 9pm", variable=var1, value="7pm to 9pm",fg="#2F4F4F",bg="#FFDAB9")

    radiobutton1.place(x=250,y=150)
    radiobutton2.place(x=250,y=180)
    radiobutton3.place(x=250,y=210)
    radiobutton4.place(x=250,y=240)
    radiobutton5.place(x=250,y=270)
    radiobutton6.place(x=250,y=300)
    radiobutton7.place(x=250,y=330)

    
    from login_f.login_file import manage_appointment
    b1=Button(f5,text="Go To Homepage",font=("Verdena 15"),fg="white",bg="#8B4513",command=manage_appointment)
    b1.place(x=250,y=420)
    b2=Button(f5,text="Click Here",font=("Verdena 15"),fg="white",bg="#8B4513",command=lambda:cancelled(var.get(),var1.get()))
    b2.place(x=100,y=420)