from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import pyodbc
class Reg:
    def __init__(self,root):
        self.root=root
        self.root.title("LOGIN Window")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        # for background image

        self.bg=ImageTk.PhotoImage(file="istockphoto-1214476616-612x612.jpg")
        bg=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        #for background image

        #self.left=ImageTk.PhotoImage(file="left.jpg")
        #left=Label(self.root,image=self.left).place(x=0,y=0,relwidth=0,relheight=0)
        # frame
        frame1=Frame(self.root,bg="white")
        frame1.place(x=480,y=100,width=700,height=500)
        
        title=Label(frame1,text="LOGIN HERE",font=("times new roman",20,"bold"),bg="white",fg="green").place(x=200,y=30)
        self.var_uname=StringVar()
        u_name=Label(frame1,text="User Name",font=("times new roman",15,"bold"),bg="white",fg="green").place(x=200,y=80)
        txt_frame=Entry(frame1,font=("times new roman",15),bg="lightgray",textvariable=self.var_uname).place(x=200,y=120,width=250)
        
        self.var_password=StringVar()
        pass_word=Label(frame1,text="Password",font=("times new roman",15,"bold"),bg="white",fg="green").place(x=200,y=240)
        txt_frame=Entry(frame1,font=("times new roman",15),bg="lightgray",textvariable=self.var_password).place(x=200,y=280,width=250)
        


        # button
        #chk=Button(frame1,text="Rigister Account").place(x=200,y=390)
        
        #self.btn=ImageTk.PhotoImage(file=new_image)
        btn_signup=Button(frame1,text="SIG IN",font=("times new roman",10),bg="green",command=self.login).place(x=200,y=420,width=100)
        btn_login=Button(self.root,text="SIGN UP ",font=("times new roman",10),bg="green",command=self.register_window).place(x=250,y=520,width=100)
        
    def register_window(self):
        self.root.destroy()
        import reg_form
    def login(self):
    
        if(self.var_uname.get()=="" or  self.var_password.get()==""):
           messagebox.showerror("Error","All FIELDS ARE REQUIRD",parent=self.root)
        
        else:

            try:
                conx = pyodbc.connect('DRIVER={SQL Server}; SERVER=WAQARKHAN; Database=sensor; TRUSTED_CONNECTION=yes')
                cursor=conx.cursor()
                cursor.execute("select * from SIGN_UP where username=? and  password_=?",(self.var_uname.get(),self.var_password.get()))
                row=cursor.fetchone()
                
                if row==None:
                    messagebox.showerror("Error"," InValid user name or password ",parent=self.root)
                    
                else:
                    #SIGIN_data()
                    messagebox.showinfo("SUCCESFUL"," Account Login",parent=self.root)
                    self.root.destroy ()
                    import TODO
                conx.close()
                   
                
                
            except Exception as es:
                messagebox.showerror("Error",f"Error due to :{str(es)}",parent=self.root)


root=Tk()
obj=Reg(root)
root.mainloop()                
