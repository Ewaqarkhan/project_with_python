from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import pyodbc
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Regiseration Window")
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
        
        title=Label(frame1,text="REGISTER HERE",font=("times new roman",20,"bold"),bg="white",fg="green").place(x=200,y=30)
        self.var_uname=StringVar()
        u_name=Label(frame1,text="User Name",font=("times new roman",15,"bold"),bg="white",fg="green").place(x=200,y=80)
        txt_frame=Entry(frame1,font=("times new roman",15),bg="lightgray",textvariable=self.var_uname).place(x=200,y=120,width=250)
        self.var_email=StringVar()
        e_mail=Label(frame1,text="Email",font=("times new roman",15,"bold"),bg="white",fg="green").place(x=200,y=160)
        txt_frame=Entry(frame1,font=("times new roman",15),bg="lightgray",textvariable=self.var_email).place(x=200,y=200,width=250)
        pass_word=Label(frame1,text="Password",font=("times new roman",15,"bold"),bg="white",fg="green").place(x=200,y=240)
        self.var_password=StringVar()
        txt_frame=Entry(frame1,font=("times new roman",15),bg="lightgray",textvariable=self.var_password).place(x=200,y=280,width=250)
        Cpass_word=Label(frame1,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="green").place(x=200,y=320)
        self.var_cpassword=StringVar()
        txt_frame=Entry(frame1,font=("times new roman",15),bg="lightgray",textvariable=self.var_cpassword).place(x=200,y=360,width=250)


        # button
        #chk=Checkbutton(frame1,text="I Agree the Terms and Conditions ").place(x=200,y=390)
        
        #self.btn=ImageTk.PhotoImage(file=new_image)
        btn_signup=Button(frame1,text="SIGN UP",font=("times new roman",10),bg="green",command=self.register_data).place(x=200,y=420,width=100)
        btn_login=Button(self.root,text="SIG IN",font=("times new roman",10),bg="green",command=self.sigin_window).place(x=250,y=520,width=100)
    def sigin_window(self):
        self.root.destroy()
        import login   
   
    def register_data(self):
    
        if(self.var_uname.get()=="" or self.var_email.get()=="" or self.var_password.get()=="" or self.var_cpassword.get()=="" ):
            messagebox.showerror("Error","All FIELDS ARE REQUIRD",parent=self.root)
        elif(self.var_password.get()!=self.var_cpassword.get()):
            messagebox.showerror("Error"," Password are not same ",parent=self.root)
        else:

            try:
                conx = pyodbc.connect('DRIVER={SQL Server}; SERVER=WAQARKHAN; Database=sensor; TRUSTED_CONNECTION=yes')
                cursor=conx.cursor()
                cursor.execute("select * from SIGN_UP where email=?",self.var_email.get())
                row=cursor.fetchone()
                
                if row!=None:
                    messagebox.showerror("Error"," user already have account  ",parent=self.root)
                else:
                    cursor.execute("INSERT INTO SIGN_UP(username,email,password_,c_password ) VALUES(?,?,?,?)",(self.var_uname.get(),self.var_email.get(),self.var_password.get(),self.var_cpassword.get()))
                    conx.commit()
                    conx.close()
                    messagebox.showinfo("SUCCESFUL"," account is register",parent=self.root)
                   
                
                
            except Exception as es:
                messagebox.showerror("Error",f"Error due to :{str(es)}",parent=self.root)
                


    
    
    
root=Tk()
obj=Register(root)
root.mainloop()
    
