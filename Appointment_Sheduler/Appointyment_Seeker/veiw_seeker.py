# This file is used to view the appointments of the seeker
from tkinter import Button, Frame, Label
import mysql.connector as mysql
import tkinter as tk
from tkinter import ttk
def veiw_ap_seeker():
            f6=Frame(bg="#a4f4a1")
            f6.place(x=0,y=0,height=500,width=500)
            l1=Label(f6,text="Your Appointments",font=("Verdena 20"),fg="red",bg="#a4f4a1")
            l1.place(x=70,y=30)
            
            from login_f.login_file import appointmentseeker
            b1=Button(f6,text="Go To Homepage",font=("Verdena 15"),fg="white",bg="grey",command=appointmentseeker)
            b1.place(x=180,y=450)
            
            con=mysql.connect(host="localhost",user="root",password="AMAN9598",database="appointmentlogin",auth_plugin='mysql_native_password')
            cursor=con.cursor()
            cursor.execute("SELECT * FROM appointment_details")
            rows=cursor.fetchall()
            
            tree =ttk.Treeview(f6, columns=('Speciality', 'Availability', 'Appointment'), show='headings')
            tree.heading('Speciality', text='Speciality')
            tree.heading('Availability', text='Availability')
            tree.heading('Appointment', text='Appointment')
            
            tree.column('Speciality', width=150)
            tree.column('Availability', width=150)
            tree.column('Appointment', width=150)
            #tree_height = min(len(rows) * 15, 350)
            
            
            for row in rows:
                tree.insert('', tk.END, values=row)
                
            tree.place(x=30, y=70, width=440, height=350)
            con.close()