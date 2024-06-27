# This file is used to cancel the appointment by the appointment seeker
from tkinter import Button, Frame, Label, Radiobutton, StringVar, Entry
import mysql.connector as mysql
import tkinter.messagebox as MessageBox

def cancel_ap_seeker():  
    def cancelled(entry_speciality,entry_availability,entry_appointment):
        con=mysql.connect(host="localhost",user="root",password="AMAN9598",database="appointmentlogin",auth_plugin='mysql_native_password')
        cursor=con.cursor()
        cursor.execute("SELECT Speciality FROM appointment_details")
        database_sp=cursor.fetchall()
        cursor.execute("SELECT Availability FROM appointment_details")
        database_av=cursor.fetchall()
        cursor.execute("SELECT Appointment FROM appointment_details")
        database_ap=cursor.fetchall()

        var1=0
        var2=0
        var3=0

        for speciality in database_sp:
            sp=speciality[0]
            if sp==entry_speciality:
                var1=1
 
        for time in database_av:
            av=time[0]
            if av==entry_availability:
                var2=1
        for appointment in database_ap:
            ap=appointment[0]
            if ap==entry_appointment:
                var3=1   

        if (entry_speciality=="" or entry_availability=="" or entry_appointment==""):
            MessageBox.showinfo("Alert","Enter all Credentials")
        elif(var1==1 and var2==1 and var3==1) :
            MessageBox.showinfo("Alert","Deleted Succesfully")
            cursor.execute("DELETE FROM appointment_details WHERE Speciality=%s and Availability=%s and Appointment=%s",(entry_speciality,entry_availability,entry_appointment))   
            cursor.execute("commit")
        else:
            MessageBox.showinfo("Alert","There is error")

                
    f5=Frame(bg="#90EE90")
    f5.place(x=0,y=0,height=500,width=500)
    l=Label(f5,text="Cancel Your Appointment",font=("Verdena 20"),fg="Black",bg="#90EE90")
    l.place(x=70,y=50)
            
    con=mysql.connect(host="localhost",user="root",password="AMAN9598",database="appointmentlogin",auth_plugin='mysql_native_password')
    cursor=con.cursor()
    cursor.execute("SELECT * FROM appointment_details")
    ap_detail=cursor.fetchall()
        
    var=StringVar()
    var.set("Doctor")
    l1=Label(f5,text="Speciality:",font=("Verdena 15"),fg="Black",bg="#90EE90")
    radiobutton1 = Radiobutton(f5, text="Doctor", variable=var, value="Doctor",fg="Black",bg="#90EE90")
    radiobutton2 = Radiobutton(f5, text="BussinessMan", variable=var, value="BussinessMan",fg="Black",bg="#90EE90")
    radiobutton3 = Radiobutton(f5, text="Influencer", variable=var, value="Influencer",fg="Black",bg="#90EE90")
    radiobutton4 = Radiobutton(f5, text="Star", variable=var, value="Star",fg="Black",bg="#90EE90")
    radiobutton5 = Radiobutton(f5, text="Movie Director", variable=var, value="Movie Director",fg="Black",bg="#90EE90")
    radiobutton6 = Radiobutton(f5, text="Advocate", variable=var, value="Advocate",fg="Black",bg="#90EE90")
    radiobutton7 = Radiobutton(f5, text="Other", variable=var, value="Other",fg="Black",bg="#90EE90")
            
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
    l1=Label(f5,text="Choose Your Speciality:",font=("Verdena 20"),fg="white",bg="#90EE90")
    radiobutton1 = Radiobutton(f5, text="7am to 9am", variable=var1, value="7am to 9am",fg="Black",bg="#90EE90")
    radiobutton2 = Radiobutton(f5, text="9am to 11am", variable=var1, value="9am to 11am",fg="Black",bg="#90EE90")
    radiobutton3 = Radiobutton(f5, text="11am to 1pm", variable=var1, value="11am to 1pm",fg="Black",bg="#90EE90")
    radiobutton4 = Radiobutton(f5, text="1pm to 3pm", variable=var1, value="1pm to 3pm",fg="Black",bg="#90EE90")
    radiobutton5 = Radiobutton(f5, text="3pm to 5pm", variable=var1, value="3pm to 5pm",fg="Black",bg="#90EE90")
    radiobutton6 = Radiobutton(f5, text="5pm to 7pm", variable=var1, value="5pm to 7pm",fg="Black",bg="#90EE90")
    radiobutton7 = Radiobutton(f5, text="7pm to 9pm", variable=var1, value="7pm to 9pm",fg="Black",bg="#90EE90")
            
    l1.place(x=70,y=100)
    radiobutton1.place(x=250,y=150)
    radiobutton2.place(x=250,y=180)
    radiobutton3.place(x=250,y=210)
    radiobutton4.place(x=250,y=240)
    radiobutton5.place(x=250,y=270)
    radiobutton6.place(x=250,y=300)
    radiobutton7.place(x=250,y=330)
            
    l4=Label(f5,text="Appointment:",font=("Verdena 15"),fg="Black",bg="#90EE90")
    l4.place(x=70,y=370)
    entry_appointment=Entry(f5,font=("Verdena 15"))
    entry_appointment.place(x=250,y=370)

    from login_f.login_file import appointmentseeker        
    b1=Button(f5,text="Go To Homepage",font=("Verdena 15"),fg="white",bg="#006400",command=appointmentseeker)
    b1.place(x=250,y=420)
    b2=Button(f5,text="Click Here",font=("Verdena 15"),fg="white",bg="#006400",command=lambda:cancelled(var.get(),var1.get(),entry_appointment.get()))
    b2.place(x=100,y=420)