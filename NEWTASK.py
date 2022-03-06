from tkinter import *
from tkinter import messagebox
import tkinter
from PIL import Image,ImageTk
import pyodbc
class NEWTASK:
    def __init__(self,root):
        
        # for background image
        self.root=root
        self.root.title("TO DO Window")
        self.root.geometry("1350x700+0+0")
        
        self.root.config(bg="white")
        frame1=Frame(self.root,bg="white")
        frame1.place(x=480,y=100,width=700,height=500)
        title=Label(frame1,text="ADD TASK",font=("times new roman",20,"bold"),bg="white",fg="green").place(x=200,y=30)
        self.var_uname=StringVar()
        task_title=Label(frame1,text="task title",font=("times new roman",15,"bold"),bg="white",fg="green").place(x=200,y=80)
        txt_frame=Entry(frame1,font=("times new roman",15),bg="lightgray",textvariable=self.var_uname).place(x=200,y=120,width=250)
        self.var_email=StringVar()
        priority_title=Label(frame1,text=" Priority",font=("times new roman",15,"bold"),bg="white",fg="green").place(x=200,y=160)
        txt_frame=Entry(frame1,font=("times new roman",15),bg="lightgray",textvariable=self.var_email).place(x=200,y=200,width=250)
        lable_title=Label(frame1,text="LABELS",font=("times new roman",15,"bold"),bg="white",fg="green").place(x=200,y=240)
        self.var_password=StringVar()
        txt_frame=Entry(frame1,font=("times new roman",15),bg="lightgray",textvariable=self.var_password).place(x=200,y=280,width=250)
        btn_signup=Button(frame1,text="ADD TASK",font=("times new roman",10),bg="green",command=self.add_data).place(x=200,y=420,width=200)
    
    def add_data(self):
        if(self.var_uname.get()=="" or self.var_email.get()=="" or self.var_password.get()=="" ):
            messagebox.showerror("Error","All FIELDS ARE REQUIRD",parent=self.root)
        
        else:

            try:
                conx = pyodbc.connect('DRIVER={SQL Server}; SERVER=WAQARKHAN; Database=sensor; TRUSTED_CONNECTION=yes')
                cursor=conx.cursor()
                cursor.execute("INSERT INTO NEWTASK(TASK_title,priority_title,lable_title ) VALUES(?,?,?)",(self.var_uname.get(),self.var_email.get(),self.var_password.get()))
                conx.commit()
                conx.close()
                messagebox.showinfo("SUCCESFUL"," ADD ",parent=self.root)
                self.root.destroy ()
                import TODO
                   
                
                
            except Exception as es:
                messagebox.showerror("Error",f"Error due to :{str(es)}",parent=self.root)
                


root=Tk()
obj=NEWTASK(root)
root.mainloop()
    
