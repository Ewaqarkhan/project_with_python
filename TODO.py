from tkinter import *
from tkinter import messagebox
import tkinter
from PIL import Image,ImageTk
import pyodbc
class MAIN:
    def __init__(self,root):
        
        # for background image
         self.root=root
         self.root.title("TO DO Window")
         self.root.geometry("1350x700+0+0")
         
         self.root.config(bg="white")
         frame2=Frame(self.root,bg="white")
         frame2.place(x=480,y=100,width=700,height=500)
         #frame3=Frame(self.root,bg="gray")
         #frame3.place(x=150,y=20,width=100,height=50)
         
         #TOdo=Label(frame3,text="TO DO",font=("times new roman",15,"bold"),fg="green",anchor='w')
         #TOdo.pack(side=TOP)
         btn_signout=Button(frame2,text="SIGN OUT",font=("times new roman",10),bg="green",command=root.destroy).place(x=100,y=7,width=100)
         
         frame4=Frame(self.root,bg="gray")
         frame4.place(x=500,y=150,width=500,height=100)
         WECOME_label=Label(frame4,text="WELCOME TO DO LIST",font=("times new roman",15,"bold"),fg="green",anchor='w').place(x=10,y=60)
         btn_cret_task=Button(frame4,text="CREATE NEW TASK",font=("times new roman",10),bg="green",command=self.NEWTASK).place(x=300,y=60,width=200)
         frame3=Frame(self.root,bg="gray")
         frame3.place(x=500,y=350,width=350,height=50)
         btn_Delete=Button(frame3,text="DELETE",font=("times new roman",10),bg="green").place(x=300,y=15,width=50)
         btn_Eidt=Button(frame3,text="EDIT",font=("times new roman",10),bg="green").place(x=250,y=15,width=50)
         SET_out=Label(frame3,text="SET OUT Garbage",font=("times new roman",15,"bold"),bg="gray",fg="green",anchor='w').place(x=10,y=10)
         frame5=Frame(self.root,bg="gray")
         frame5.place(x=500,y=450,width=350,height=50)
         btn_Delete=Button(frame5,text="DELETE",font=("times new roman",10),bg="green").place(x=300,y=15,width=50)
         btn_Eidt=Button(frame5,text="EDIT",font=("times new roman",10),bg="green").place(x=250,y=15,width=50)
         u_name=Label(frame5,text="Empty the dishwashwer",font=("times new roman",15,"bold"),bg="gray",fg="green",anchor='w').place(x=10,y=10)
         frame6=Frame(self.root,bg="gray")
         frame6.place(x=500,y=550,width=350,height=50)
         btn_Delete=Button(frame6,text="DELETE",font=("times new roman",10),bg="green").place(x=300,y=15,width=50)
         btn_Eidt=Button(frame6,text="EDIT",font=("times new roman",10),bg="green").place(x=250,y=15,width=50)
         u_name=Label(frame6,text="Play Dota",font=("times new roman",15,"bold"),bg="gray",fg="green",anchor='w').place(x=10,y=10)
         frame7=Frame(self.root,bg="gray")
         frame7.place(x=500,y=650,width=350,height=50)
         btn_Delete=Button(frame7,text="DELETE",font=("times new roman",10),bg="green").place(x=300,y=15,width=50)
         btn_Eidt=Button(frame7,text="EDIT",font=("times new roman",10),bg="green").place(x=250,y=15,width=50)
         u_name=Label(frame7,text="DO the groceries",font=("times new roman",15,"bold"),bg="gray",fg="green",anchor='w').place(x=10,y=10)
        

    def NEWTASK(self):
        self.root.destroy()
        import NEWTASK
    
        
     
root=Tk()
obj=MAIN(root)
root.mainloop()
    

