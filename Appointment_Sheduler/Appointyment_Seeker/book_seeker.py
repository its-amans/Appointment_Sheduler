# This file is used to book the appointment for the seeker
from tkinter import Button, Frame, Label, Radiobutton, StringVar, Entry
import mysql.connector as mysql
import tkinter.messagebox as MessageBox
def book_appointment():
    def book(entry_speciality,entry_time,entry_appointment):
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
            if av==entry_time:
                var2=1
        if var1==1 and var2==1:
            cursor.execute("UPDATE appointment_details SET Appointment=%s WHERE Availability=%s AND Speciality=%s", (entry_appointment, entry_time, entry_speciality))
            cursor.execute("commit")
            MessageBox.showinfo("Alert","Appointment Booked Succesfully")
        else:
            MessageBox.showinfo("Alert","There is error")
                
    f7=Frame(bg="#E0FFFF")
    f7.place(x=0,y=0,height=500,width=500)
    l=Label(f7,text="Book Your Appointments",font=("Verdena 20"),fg="#000000",bg="#E0FFFF")
    l.place(x=70,y=50)
            
            
    var=StringVar()
    var.set("Doctor")
    l1=Label(f7,text="Choose Your Speciality:",font=("Verdena 15"),fg="#000000",bg="#E0FFFF")
    radiobutton1 = Radiobutton(f7, text="Doctor", variable=var, value="Doctor",fg="#000000",bg="#E0FFFF")
    radiobutton2 = Radiobutton(f7, text="BussinessMan", variable=var, value="BussinessMan",fg="#000000",bg="#E0FFFF")
    radiobutton3 = Radiobutton(f7, text="Influencer", variable=var, value="Influencer",fg="#000000",bg="#E0FFFF")
    radiobutton4 = Radiobutton(f7, text="Star", variable=var, value="Appointment Seeker",fg="#000000",bg="#E0FFFF")
    radiobutton5 = Radiobutton(f7, text="Movie Director", variable=var, value="Movie Director",fg="#000000",bg="#E0FFFF")
    radiobutton6 = Radiobutton(f7, text="Advocate", variable=var, value="Advocate",fg="#000000",bg="#E0FFFF")
    radiobutton7 = Radiobutton(f7, text="Other", variable=var, value="Other",fg="#000000",bg="#E0FFFF")
            
    l1.place(x=70,y=100)
    radiobutton1.place(x=100,y=150)
    radiobutton2.place(x=100,y=180)
    radiobutton3.place(x=100,y=210)
    radiobutton4.place(x=100,y=240)
    radiobutton5.place(x=100,y=270)
    radiobutton6.place(x=100,y=300)
    radiobutton7.place(x=100,y=330)
            
    var1=StringVar()
    var1.set("7am to 9am")
    l1=Label(f7,text="Choose Your Speciality:",font=("Verdena 20"),fg="#000000",bg="#E0FFFF")
    radiobutton1 = Radiobutton(f7, text="7am to 9am", variable=var1, value="7am to 9am",fg="#000000",bg="#E0FFFF")
    radiobutton2 = Radiobutton(f7, text="9am to 11am", variable=var1, value="9am to 11am",fg="#000000",bg="#E0FFFF")
    radiobutton3 = Radiobutton(f7, text="11am to 1pm", variable=var1, value="11am to 1pm",fg="#000000",bg="#E0FFFF")
    radiobutton4 = Radiobutton(f7, text="1pm to 3pm", variable=var1, value="1pm to 3pm",fg="#000000",bg="#E0FFFF")
    radiobutton5 = Radiobutton(f7, text="3pm to 5pm", variable=var1, value="3pm to 5pm",fg="#000000",bg="#E0FFFF")
    radiobutton6 = Radiobutton(f7, text="5pm to 7pm", variable=var1, value="5pm to 7pm",fg="#000000",bg="#E0FFFF")
    radiobutton7 = Radiobutton(f7, text="7pm to 9pm", variable=var1, value="7pm to 9pm",fg="#000000",bg="#E0FFFF")
            
    l1.place(x=70,y=100)
    radiobutton1.place(x=250,y=150)
    radiobutton2.place(x=250,y=180)
    radiobutton3.place(x=250,y=210)
    radiobutton4.place(x=250,y=240)
    radiobutton5.place(x=250,y=270)
    radiobutton6.place(x=250,y=300)
    radiobutton7.place(x=250,y=330)
            
    l4=Label(f7,text="Appointment:",font=("Verdena 15"),fg="#000000",bg="#E0FFFF")
    l4.place(x=70,y=370)
    entry_appointment=Entry(f7,font=("Verdena 15"))
    entry_appointment.place(x=250,y=370)
            
    b2=Button(f7,text="Book",font=("Verdena 15"),fg="#000000",bg="#A9A9A9",command=lambda:book(var.get(),var1.get(),entry_appointment.get()))
    b2.place(x=100,y=420)

    from login_f.login_file import appointmentseeker       
    b1=Button(f7,text="Go To Homepage",font=("Verdena 15"),fg="#000000",bg="#A9A9A9",command=appointmentseeker)
    b1.place(x=250,y=420)