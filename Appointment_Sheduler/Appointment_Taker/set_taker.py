# This file is used to set the availability and speciality of the appointment taker.
from tkinter import Button, Frame, Label, Radiobutton, StringVar, Entry
import mysql.connector as mysql
import tkinter.messagebox as MessageBox
def set_availability():
    def clickset(value):
        con=mysql.connect(host="localhost",user="root",password="AMAN9598",database="appointmentlogin",auth_plugin='mysql_native_password')
        cursor=con.cursor()
        availability_value=value
        sql = "INSERT INTO appointment_details (Availability) VALUES (%s)"
        cursor.execute(sql, (availability_value,))
        cursor.execute("commit")

        MessageBox.showinfo("Alert","Availability is set Succesfully")
        con.close()
                
        def set_speciality(availability_value):
            value2=availability_value
            def clickset(value,availability_value):
                con=mysql.connect(host="localhost",user="root",password="AMAN9598",database="appointmentlogin",auth_plugin='mysql_native_password')
                cursor=con.cursor()
                cursor.execute("UPDATE appointment_details SET Speciality=%s WHERE Availability=%s",(value,availability_value))
                cursor.execute("commit")

                MessageBox.showinfo("Alert","Speciality is set Succesfully")
                con.close()
                f12=Frame(bg="#F5FFFA")
                f12.place(x=0,y=0,height=500,width=500)
                from login_f.login_file import appointmenttaker
                b1=Button(f12,text="Go To Homepage",font=("Verdena 15"),fg="white",bg="#008080",command=appointmenttaker)
                b1.place(x=180,y=230)
                
            f9=Frame(bg="#F0F8FF")
            f9.place(x=0,y=0,height=500,width=500)
            var=StringVar()
            var.set("Doctor")
            l1=Label(f9,text="Choose Your Speciality:",font=("Verdena 20"),fg="#000080",bg="#F0F8FF")
            radiobutton1 = Radiobutton(f9, text="Doctor", variable=var, value="Doctor",fg="#000080",bg="#F0F8FF")
            radiobutton2 = Radiobutton(f9, text="BussinessMan", variable=var, value="BussinessMan",fg="#000080",bg="#F0F8FF")
            radiobutton3 = Radiobutton(f9, text="Influencer", variable=var, value="Influencer",fg="#000080",bg="#F0F8FF")
            radiobutton4 = Radiobutton(f9, text="Star", variable=var, value="Appointment Seeker",fg="#000080",bg="#F0F8FF")
            radiobutton5 = Radiobutton(f9, text="Movie Director", variable=var, value="Movie Director",fg="#000080",bg="#F0F8FF")
            radiobutton6 = Radiobutton(f9, text="Advocate", variable=var, value="Advocate",fg="#000080",bg="#F0F8FF")
            radiobutton7 = Radiobutton(f9, text="Other", variable=var, value="Other",fg="#000080",bg="#F0F8FF")

            l1.place(x=70,y=100)
            radiobutton1.place(x=250,y=150)
            radiobutton2.place(x=250,y=180)
            radiobutton3.place(x=250,y=210)
            radiobutton4.place(x=250,y=240)
            radiobutton5.place(x=250,y=270)
            radiobutton6.place(x=250,y=300)
            radiobutton7.place(x=250,y=330)

            b2=Button(f9,text="Click To Set",font=("Verdena 15"),fg="white",bg="#4682B4",command=lambda:clickset(var.get(),availability_value))
            b2.place(x=180,y=400)

    # b2=Button(f4,text="Click Here",font=("Verdena 15"),fg="white",bg="#4682B4",command=set_availability)  
    # b2.place(x=300,y=250)
        set_speciality(availability_value)
        
    f10=Frame(bg="#F0F8FF")
    f10.place(x=0,y=0,height=500,width=500)
    var=StringVar()
    var.set("7am to 9am")
    l1=Label(f10,text="Choose Your Speciality:",font=("Verdena 20"),fg="#000080",bg="#F0F8FF")
    radiobutton1 = Radiobutton(f10, text="7am to 9am", variable=var, value="7am to 9am",fg="#000080",bg="#F0F8FF")
    radiobutton2 = Radiobutton(f10, text="9am to 11am", variable=var, value="9am to 11am",fg="#000080",bg="#F0F8FF")
    radiobutton3 = Radiobutton(f10, text="11am to 1pm", variable=var, value="11am to 1pm",fg="#000080",bg="#F0F8FF")
    radiobutton4 = Radiobutton(f10, text="1pm to 3pm", variable=var, value="1pm to 3pm",fg="#000080",bg="#F0F8FF")
    radiobutton5 = Radiobutton(f10, text="3pm to 5pm", variable=var, value="3pm to 5pm",fg="#000080",bg="#F0F8FF")
    radiobutton6 = Radiobutton(f10, text="5pm to 7pm", variable=var, value="5pm to 7pm",fg="#000080",bg="#F0F8FF")
    radiobutton7 = Radiobutton(f10, text="7pm to 9pm", variable=var, value="7pm to 9pm",fg="#000080",bg="#F0F8FF")
            
    l1.place(x=70,y=100)
    radiobutton1.place(x=250,y=150)
    radiobutton2.place(x=250,y=180)
    radiobutton3.place(x=250,y=210)
    radiobutton4.place(x=250,y=240)
    radiobutton5.place(x=250,y=270)
    radiobutton6.place(x=250,y=300)
    radiobutton7.place(x=250,y=330)
    
    from login_f.login_file import appointmenttaker       
    b1=Button(f10,text="Go To Homepage",font=("Verdena 15"),fg="white",bg="#4682B4",command=appointmenttaker)
    b1.place(x=270,y=400)
    b2=Button(f10,text="Click To Set",font=("Verdena 15"),fg="white",bg="#4682B4",command=lambda:clickset(var.get()))
    b2.place(x=70,y=400)
        