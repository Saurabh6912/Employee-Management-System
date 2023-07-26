from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import mysql.connector

class Employee:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title('Employee Management System')

    # Creating variables for taking information of Employees
        self.var_dep=StringVar()
        self.var_name=StringVar()
        self.var_des=StringVar()
        self.var_email=StringVar()
        self.var_add=StringVar()
        self.var_married=StringVar()
        self.var_dob=StringVar()
        self.var_doj=StringVar()
        self.var_idproof=StringVar()
        self.var_idnum=StringVar()
        self.var_gender=StringVar()
        self.var_mobile=StringVar()
        self.var_country=StringVar()
        self.var_salary=StringVar()




        lbl_title = Label(self.root,text='EMPLOYEE MANAGEMENT SYSTEM',font=('times new roman',37,'bold'),fg='darkblue',bg='yellow')
        lbl_title.place(x=0,y=0,width=1530,height=50)

# logo
        img_logo = Image.open('images/employee_logo.png')
        img_logo = img_logo.resize((50,50))
        self.photo_logo = ImageTk.PhotoImage(img_logo) #it's a module for loading an image.

        self.logo = Label(self.root,image=self.photo_logo)
        self.logo.place(x=270,y=0,width=50,height=50)

# frame for images
        img_frame = Frame(self.root,bd=2,relief=RIDGE,bg='white') #bd=border,boreder_style=relief,bg=background
        img_frame.place(x=0,y=50,width=1530,height=160)

        # 1st image
        img1 = Image.open('images/image_1.png')
        img1 = img1.resize((510,160))
        self.photo_1 = ImageTk.PhotoImage(img1)

        self.img_1 = Label(img_frame,image=self.photo_1)
        self.img_1.place(x=0,y=0,width=510,height=157)

        # 2nd image
        img2 = Image.open('images/images_2.jpeg')
        img2 = img2.resize((510,160))
        self.photo_2 = ImageTk.PhotoImage(img2)

        self.img_2 = Label(img_frame,image=self.photo_2)
        self.img_2.place(x=510,y=0,width=510,height=160)

        # 3rd image
        img3 = Image.open('images/image_2.jpg')
        img3 = img3.resize((510,160))
        self.photo_3 = ImageTk.PhotoImage(img3)

        self.img_3 = Label(img_frame,image=self.photo_3)
        self.img_3.place(x=1020,y=0,width=510,height=160)

# Main Frame
        Main_frame = Frame(self.root,bd=2,relief=RIDGE,bg='white') 
        Main_frame.place(x=5,y=215,width=1515,height=560)

    #Upper Frame
        # in label frame we can also give some text so using this
        Upper_frame = LabelFrame(Main_frame,bd=2,relief=RIDGE,bg='white',
                                text='Employee Information',font=('times new roman',15,'bold'),fg='red') 
        Upper_frame.place(x=5,y=5,width=1500,height=250)
    
        # Labels and Entry fields
        # Department
        lbl_dept = Label(Upper_frame,text='Department',font=('arial',11,'bold'),bg='white')
        lbl_dept.grid(row=0,column=0,padx=2,sticky=W)

        combo_dept = ttk.Combobox(Upper_frame,textvariable=self.var_dep,font=('arial',12,'bold'),width=17,state='readonly')
        combo_dept['value'] = ('Select Department','HR','Accountm& Finance','Learning & Development','IT Services','Infrastructures')
        combo_dept.current(0) #to show first option initially
        combo_dept.grid(row=0,column=1,padx=2,pady=7,sticky=W)

        # Name
        lbl_name = Label(Upper_frame,text='Name',font=('arial',11,'bold'),bg='white')
        lbl_name.grid(row=0,column=2,padx=2,sticky=W)

        txt_name = ttk.Entry(Upper_frame,textvariable=self.var_name,width=22,font=('arial',11,'bold'))
        txt_name.grid(row=0,column=3,padx=2,pady=7,sticky=W)
       
        # Designation
        lbl_desg = Label(Upper_frame,text='Designition',font=('arial',11,'bold'),bg='white')
        lbl_desg.grid(row=1,column=0,padx=2,pady=7,sticky=W)

        txt_desg = ttk.Entry(Upper_frame,textvariable=self.var_des,width=22,font=('arial',11,'bold'))
        txt_desg.grid(row=1,column=1,padx=2,pady=7,sticky=W)

        # Email
        lbl_email = Label(Upper_frame,text='Email',font=('arial',11,'bold'),bg='white')
        lbl_email.grid(row=1,column=2,padx=2,pady=7,sticky=W)

        txt_email = ttk.Entry(Upper_frame,textvariable=self.var_email,width=22,font=('arial',11,'bold'))
        txt_email.grid(row=1,column=3,padx=2,pady=7,sticky=W)

        # Address
        lbl_add = Label(Upper_frame,text='Address',font=('arial',11,'bold'),bg='white')
        lbl_add.grid(row=2,column=0,padx=2,pady=7,sticky=W)

        txt_add = ttk.Entry(Upper_frame,textvariable=self.var_add,width=22,font=('arial',11,'bold'))
        txt_add.grid(row=2,column=1,padx=2,pady=7,sticky=W)

        # Married
        lbl_married = Label(Upper_frame,text='Married Status',font=('arial',11,'bold'),bg='white')
        lbl_married.grid(row=2,column=2,padx=2,pady=7,sticky=W)

        combo_married = ttk.Combobox(Upper_frame,textvariable=self.var_married,font=('arial',12,'bold'),width=17,state='readonly')
        combo_married['value'] = ('Select Status','Married','Unmarried')
        combo_married.current(0) #to show first option initially
        combo_married.grid(row=2,column=3,padx=2,pady=7,sticky=W)

        # DOB
        lbl_dob = Label(Upper_frame,text='DOB',font=('arial',11,'bold'),bg='white')
        lbl_dob.grid(row=3,column=0,padx=2,pady=7,sticky=W)

        txt_dob = ttk.Entry(Upper_frame,textvariable=self.var_dob,width=22,font=('arial',11,'bold'))
        txt_dob.grid(row=3,column=1,padx=2,pady=7,sticky=W)

        # Date of Joining
        lbl_doj = Label(Upper_frame,text='DOJ',font=('arial',11,'bold'),bg='white')
        lbl_doj.grid(row=3,column=2,padx=2,pady=7,sticky=W)

        txt_doj = ttk.Entry(Upper_frame,textvariable=self.var_doj,width=22,font=('arial',11,'bold'))
        txt_doj.grid(row=3,column=3,padx=2,pady=7,sticky=W)

        # ID proof
        combo_Id = ttk.Combobox(Upper_frame,textvariable=self.var_idproof,font=('arial',12,'bold'),width=17,state='readonly')
        combo_Id['value'] = ('Select ID Proof','ADHAR CARD','PAN CARD','DRIVING LICENCE','VOTER ID')
        combo_Id.current(0) #to show first option initially
        combo_Id.grid(row=4,column=0,padx=2,pady=7,sticky=W)

        txt_proof = ttk.Entry(Upper_frame,textvariable=self.var_idnum,width=22,font=('arial',11,'bold'))
        txt_proof.grid(row=4,column=1,padx=2,pady=7,sticky=W)

        # Gender
        lbl_gender = Label(Upper_frame,text='Gender',font=('arial',11,'bold'),bg='white')
        lbl_gender.grid(row=4,column=2,padx=2,pady=7,sticky=W)

        combo_gender = ttk.Combobox(Upper_frame,textvariable=self.var_gender,font=('arial',12,'bold'),width=17,state='readonly')
        combo_gender['value'] = ('Male','Female','Other')
        combo_gender.current(0) #to show first option initially
        combo_gender.grid(row=4,column=3,padx=2,pady=7,sticky=W)

        # phone
        lbl_m_no = Label(Upper_frame,text='Mobile No.',font=('arial',11,'bold'),bg='white')
        lbl_m_no.grid(row=0,column=4,padx=2,pady=7,sticky=W)

        txt_m_no = ttk.Entry(Upper_frame,textvariable=self.var_mobile,width=22,font=('arial',11,'bold'))
        txt_m_no.grid(row=0,column=5,padx=2,pady=7,sticky=W)

        # Country
        lbl_country = Label(Upper_frame,text='Country',font=('arial',11,'bold'),bg='white')
        lbl_country.grid(row=1,column=4,padx=2,pady=7,sticky=W)

        txt_country = ttk.Entry(Upper_frame,textvariable=self.var_country,width=22,font=('arial',11,'bold'))
        txt_country.grid(row=1,column=5,padx=2,pady=7,sticky=W)

        # CTC
        lbl_ctc = Label(Upper_frame,text='Salary(CTC)',font=('arial',11,'bold'),bg='white')
        lbl_ctc.grid(row=2,column=4,padx=2,pady=7,sticky=W)

        txt_ctc = ttk.Entry(Upper_frame,textvariable=self.var_salary,width=22,font=('arial',11,'bold'))
        txt_ctc.grid(row=2,column=5,padx=2,pady=7,sticky=W)

        # photo id
        # code

        # Button frame
        Buttton_frame = Frame(Upper_frame,bd=2,relief=RIDGE,bg='white') 
        Buttton_frame.place(x=1280,y=10,width=190,height=175)

        # save
        btn_add = Button(Buttton_frame,text='Save',command=self.add_data,font=('arial',11,'bold'),width=20,bg='blue',fg='white')
        btn_add.grid(row=0,column=0,padx=1,pady=5)

        # Delete
        btn_dlt = Button(Buttton_frame,text='Delete',command=self.delete_data,font=('arial',11,'bold'),width=20,bg='blue',fg='white')
        btn_dlt.grid(row=1,column=0,padx=1,pady=5)

        # update
        btn_update = Button(Buttton_frame,text='Update',command=self.update_data,font=('arial',11,'bold'),width=20,bg='blue',fg='white')
        btn_update.grid(row=2,column=0,padx=1,pady=5)

        # clear
        btn_clear = Button(Buttton_frame,text='Clear',command=self.reset_data,font=('arial',11,'bold'),width=20,bg='blue',fg='white')
        btn_clear.grid(row=3,column=0,padx=1,pady=5)

    # Down Frame
        Down_frame = LabelFrame(Main_frame,bd=2,relief=RIDGE,bg='white',
                                text='Employee Information Table',font=('times new roman',15,'bold'),fg='red') 
        Down_frame.place(x=5,y=260,width=1500,height=290)

        # Search frame
        Search_frame = LabelFrame(Down_frame,bd=2,relief=RIDGE,bg='white',font=('times new roman',13,'bold'),text='Search Employee',fg='red')
        Search_frame.place(x=5,y=0,width=1485,height=60)

        search_by = Label(Search_frame,font=('arial',11,'bold'),text='Search By:',fg='white',bg='red')
        search_by.grid(row=0,column=0,sticky=W,padx=5)

        # Search
        # create variable
        self.var_com_search=StringVar()

        # combobox
        com_txt_search=ttk.Combobox(Search_frame,textvariable=self.var_com_search,state='readonly',font=('arial',12,'bold'),width=18)
        com_txt_search['value']=('Select Serch Method','Mobile_No','Id_number')
        com_txt_search.grid(row=0,column=1,sticky=W,padx=5)

        # create variable
        self.var_search = StringVar()

        # taking input for search
        txt_search = ttk.Entry(Search_frame,textvariable=self.var_search,width=22,font=('arial',11,'bold'))
        txt_search.grid(row=0,column=2,padx=5)

        btn_search = Button(Search_frame,text='Search',command=self.search_data,font=('arial',11,'bold'),width=14,bg='blue',fg='white')
        btn_search.grid(row=0,column=3,padx=5)

        # show all button
        btn_showall = Button(Search_frame,text='Show All',command=self.fetch_data,font=('arial',11,'bold'),width=14,bg='blue',fg='white')
        btn_showall.grid(row=0,column=4,padx=5)

        # text stay updated
        stay_updt = Label(Search_frame,text='Stay Updated',font=('times new roman',22,'bold'),fg='red',bg='white')
        stay_updt.place(x=800,y=0,width=600,height=35)

        img_s = Image.open('images/image_3.jpeg')
        img_s = img_s.resize((100,35))
        self.stay_updt = ImageTk.PhotoImage(img_s)

        self.stay_update = Label(Search_frame,image=self.stay_updt)
        self.stay_update.place(x=905,y=0,width=100,height=35)


# =====================================================Employee Table=============================================================

        # Table frame
        table_frame = Frame(Down_frame,bd=2,relief=RIDGE) 
        table_frame.place(x=5,y=60,width=1485,height=203)

        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.employee_table = ttk.Treeview(table_frame,
                                           column=('Dep','Name','Designation','Email','Address','Married',
                                                   'DOB','DOJ','Id Proof','Id_number','Gender','Mobile No.',
                                                   'Country','Salary(CTC)',),
                                                   xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.employee_table.xview)
        scroll_y.config(command=self.employee_table.yview)

        self.employee_table.heading('Dep',text='Department')
        self.employee_table.heading('Name',text='Name')
        self.employee_table.heading('Designation',text='Designation')
        self.employee_table.heading('Email',text='Email')
        self.employee_table.heading('Address',text='Address')
        self.employee_table.heading('Married',text='Married')
        self.employee_table.heading('DOB',text='DOB')
        self.employee_table.heading('DOJ',text='DOJ')
        self.employee_table.heading('Id Proof',text='Id Proof')
        self.employee_table.heading('Id_number',text='Id_number')
        self.employee_table.heading('Gender',text='Gender')
        self.employee_table.heading('Mobile No.',text='Mobile No.')
        self.employee_table.heading('Country',text='Country')
        self.employee_table.heading('Salary(CTC)',text='Salary(CTC)')

        self.employee_table['show'] = 'headings'
        
        self.employee_table.column('Dep',width=100)
        self.employee_table.column('Name',width=100)
        self.employee_table.column('Designation',width=100)
        self.employee_table.column('Email',width=100)
        self.employee_table.column('Address',width=100)
        self.employee_table.column('Married',width=100)
        self.employee_table.column('DOB',width=100)
        self.employee_table.column('DOJ',width=100)
        self.employee_table.column('Id Proof',width=100)
        self.employee_table.column('Id_number',width=100)
        self.employee_table.column('Gender',width=100)
        self.employee_table.column('Mobile No.',width=100)
        self.employee_table.column('Country',width=100)
        self.employee_table.column('Salary(CTC)',width=100)
        

        self.employee_table.pack(fill=BOTH,expand=1)
        self.employee_table.bind("<ButtonRelease>",self.get_cursor)


        self.fetch_data()

# ====================================================Functions Declaration==========================================================
    def add_data(self):
        if self.var_dep.get()=='' or self.var_email.get()=='':
            messagebox.showerror('Error',"Mendatory field can't be empty")
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='pw',database='employee_management_sys')
                my_cursor = conn.cursor()
                my_cursor.execute('insert into employees values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(

                                                                                                            self.var_dep.get(),
                                                                                                            self.var_name.get(),
                                                                                                            self.var_des.get(),
                                                                                                            self.var_email.get(),
                                                                                                            self.var_add.get(),
                                                                                                            self.var_married.get(),
                                                                                                            self.var_dob.get(),
                                                                                                            self.var_doj.get(),
                                                                                                            self.var_idproof.get(),
                                                                                                            self.var_idnum.get(),
                                                                                                            self.var_gender.get(),
                                                                                                            self.var_mobile.get(),
                                                                                                            self.var_country.get(),
                                                                                                            self.var_salary.get()                                                                                      
                                                                                                            
                                                                                                                ))
                conn.commit()
                conn.close()
                messagebox.showinfo('Successfuly! Employee has been added',parent=self.root)
            except Exception as es:
                messagebox.showerror('Error',f'Due To:{str(es)}',parent=self.root)

# fetch data
    def fetch_data(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='pw',database='employee_management_sys')
        my_cursor = conn.cursor()
        my_cursor.execute('select * from employees')
        data = my_cursor.fetchall()
        if len(data)!=0:
            self.employee_table.delete(*self.employee_table.get_children())
            for i in data:
                self.employee_table.insert("",END,values=i)
            conn.commit()
        conn.close()

# Get Cursor 
    def get_cursor(self,event=""):
        cursor_row = self.employee_table.focus()
        content = self.employee_table.item(cursor_row)
        data = content['values']

        self.var_dep.set(data[0])
        self.var_name.set(data[1])
        self.var_des.set(data[2])
        self.var_email.set(data[3])
        self.var_add.set(data[4])
        self.var_married.set(data[5])
        self.var_dob.set(data[6])
        self.var_doj.set(data[7])
        self.var_idproof.set(data[8])
        self.var_idnum.set(data[9])
        self.var_gender.set(data[10])
        self.var_mobile.set(data[11])
        self.var_country.set(data[12])
        self.var_salary.set(data[13])

# Update data

    def update_data(self):
        if self.var_dep.get()=='' or self.var_email.get()=='':
            messagebox.showerror('Error',"Mendatory field can't be empty")
        else:
            try:
                update=messagebox.askyesno('Are you sure to update!')
                if update>0:
                    conn=mysql.connector.connect(host='localhost',username='root',password='pw',database='employee_management_sys')
                    my_cursor = conn.cursor()
                    my_cursor.execute('''update employees set Department=%s,Name=%s,Designation=%s,
                                      Email=%s,Address=%s,Married=%s,DOB=%s,DOJ=%s,Id_proof=%s,
                                      Gender=%s,Mobile_No=%s,Country=%s,Salary=%s 
                                      where Id_number=%s''',(
                                                                self.var_dep.get(),
                                                                self.var_name.get(),
                                                                self.var_des.get(),
                                                                self.var_email.get(),
                                                                self.var_add.get(),
                                                                self.var_married.get(),
                                                                self.var_dob.get(),
                                                                self.var_doj.get(),
                                                                self.var_idproof.get(),
                                                                self.var_gender.get(),
                                                                self.var_mobile.get(),
                                                                self.var_country.get(),
                                                                self.var_salary.get(),
                                                                self.var_idnum.get()
                                                            
                                                                ))
                else:
                    if not update:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Successfully Updated",parent=self.root)
            
            except Exception as es:
                messagebox.showerror('Error',f'Due To:{str(es)}',parent=self.root)
                
# Delete
    def delete_data(self):
        if self.var_idnum.get()=="":
            messagebox.showerror('Error','Id_number can not be empty')
        else:
            try:
                Delete=messagebox.askyesno('Are you sure to Delete?')
                
                if Delete>0:
                    conn=mysql.connector.connect(host='localhost',username='root',password='pw',database='employee_management_sys')
                    my_cursor = conn.cursor()
                    my_cursor.execute('delete from employees where Id_number=%s',(self.var_idnum.get(),))
                else:
                    if not Delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Employee successfully Deleted",parent=self.root)
            
            except Exception as es:
                messagebox.showerror('Error',f'Due To:{str(es)}',parent=self.root)
            
# clear (Reset)
    def reset_data(self):
        self.var_dep.set('Select Department')
        self.var_name.set('')
        self.var_des.set('')
        self.var_email.set('')
        self.var_add.set('')
        self.var_married.set('Select Status')
        self.var_dob.set('')
        self.var_doj.set('')
        self.var_idproof.set('Select ID Proof')
        self.var_idnum.set('')
        self.var_gender.set('Male')
        self.var_mobile.set('')
        self.var_country.set('')
        self.var_salary.set('')

# search

    def search_data(self):
        if self.var_com_search.get()=='' or self.var_search.get()=='':
            messagebox.showerror('Error','Please select option and enter valid data')
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='pw',database='employee_management_sys')
                my_cursor = conn.cursor()
                my_cursor.execute('select * from employees where ' +str(self.var_com_search.get())+ " LIKE '%" +str(self.var_search.get())+"%'")
                rows=my_cursor.fetchall()
                if len(rows)!=0:
                    self.employee_table.delete(*self.employee_table.get_children())
                    for i in rows:
                        self.employee_table.insert("",END,values=i)
                conn.commit()
                conn.close()

            except Exception as es:
                messagebox.showerror('Error',f'Due To:{str(es)}',parent=self.root)
            

if __name__=='__main__':
    root=Tk()
    emp = Employee(root)
    root.mainloop()

