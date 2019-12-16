from Tkinter import *
from tkMessageBox import *
import sqlite3
con = sqlite3.Connection('Phonebook_007')
cur = con.cursor()
cur.execute("create table if not exists user_info(ph_id integer primary key AUTOINCREMENT, Fname varchar(20), Mname varchar(20), Lname varchar(20), Company varchar(20), Address varchar(30), City varchar(25), Pin integer, Website varchar(80), DOB varchar(10) )")
cur.execute("create table if not exists phone_info(ph_id integer,ph_type varchar (15), Ph_no varchar(20) ,foreign key(ph_id)REFERENCES user_info(ph_id))")
cur.execute("create table if not exists email_info(ph_id integer, email_type  varchar(15), email_id varchar(40),foreign key(ph_id) REFERENCES user_info(ph_id))")

a = []
def new_window():
    ph=Tk()
    ph.propagate(0)
    
    def clear():
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        e5.delete(0,END)
        e6.delete(0,END)
        e7.delete(0,END)
        e8.delete(0,END)
        e9.delete(0,END)
        e10.delete(0,END)
        e11.delete(0,END)
        v1.set(None)
        v2.set(None)


    def close():
        ph.destroy()

    def save():
        
        if len(e1.get() or e2.get() or e3.get() or e4.get() or e5.get() or e6.get() or e7.get() or e8.get() or e9.get() or e10.get()  or e11.get() or v1.get() or v2.get()) == 0:
            showinfo("Warning!","Fill the required fields!!!",icon = 'warning')

        else:
            
            cur.execute("insert into user_info(Fname,Mname,Lname,Company,Address,City,Pin,Website,Dob)values(?,?,?,?,?,?,?,?,?)",(e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get(),e7.get(),e8.get(),e9.get()))
            cur.execute("select max(ph_id) from user_info")
            x = cur.fetchall()
            idd = x[0][0]
            cur.execute("insert into  phone_info(ph_id,ph_type,Ph_no) values(?,?,?)",(idd,v1.get(),e10.get()))
            cur.execute("insert into email_info(ph_id,email_type,email_id) values(?,?,?)",(idd,v2.get(),e11.get()))            
            clear()
            showinfo("Information","Your contact is saved successfully!!!!!")
            con.commit()

    def search():
        #close()
        
        ph1 = Tk()
        ph1.propagate(0)
        ph1.geometry('750x700')
        Label(ph1,text = "Search Contact", font = 'courier 30 bold underline').grid(row =0, column = 2)
        Label(ph1,text = "Enter Name:  ", font = 'Times 20 bold ').grid(row = 6, column = 0)
        search = Entry(ph1)
        search.grid(row = 6 , column = 2)
        lb = Listbox(ph1,width=60,height=30)
        lb.grid(row = 10,column = 2)
        def key_press(e = 0):
            s = search.get()
            lb.delete(0,END)
            key = "select ph_id,Fname, Mname,Lname from user_info where Fname LIKE '%{}%' OR Mname LIKE '%{}%' OR Lname LIKE '%{}%'".format(s,s,s)
            cur.execute(key)
            global a
            a = cur.fetchall()
            for k in range (len(a)):
                fn = a[k][1]+' '+a[k][2]+' '+a[k][3]
                lb.insert(0,fn)
        def retrieve(e = 0):
            global a
            per = lb.curselection()
            #print per
            index = per[0]
            lb.delete(0,END)
            index = len(a) - index - 1
            #print index
            pid = a[index][0]
            qq = 'select * from  user_info where ph_id = ?'
            cur.execute(qq,[(pid)])
            k = cur.fetchall()
            pp = 'select * from phone_info where ph_id = ?'
            cur.execute(pp,[(pid)])
            d = cur.fetchall()
            print d,
            rr = 'select * from email_info where ph_id =?'
            cur.execute(rr,[(pid)])
            c = cur.fetchall()
            print c,
            #lb.insert(0,k)
            ph = Tk()
            ph.geometry("600x500")
            Label(ph,text="Name: ",font = 20).grid(row = 2, column = 1)
            Label(ph,text = k[0][1] +' '+k[0][2]+' '+k[0][3],font = 20).grid(row = 2,column = 2)
            Label(ph,text = "Company Name: ",font = 20).grid(row = 3,column = 1)
            Label(ph,text = k[0][4],font = 20).grid(row = 3,column = 2)
            Label(ph,text = "Address: ",font = 20).grid(row = 4,column = 1)
            Label(ph,text = k[0][5],font = 20).grid(row = 4,column = 2)
            Label(ph,text = "City: ",font = 20).grid(row = 5,column = 1)
            Label(ph,text = k[0][6],font = 20).grid(row = 5,column = 2)
            Label(ph,text = "Pin Code: ",font = 20).grid(row = 6,column = 1)
            Label(ph,text = k[0][7],font = 20).grid(row = 6,column = 2)
            Label(ph,text = "Website URL: ",font = 20).grid(row = 7,column = 1)
            Label(ph,text = k[0][8],font = 20).grid(row = 7,column = 2)
            Label(ph,text = "Date of Birth: ",font = 20).grid(row = 8,column = 1)
            Label(ph,text = k[0][9],font = 20).grid(row = 8,column = 2)
            Label(ph,text = "Phone Type: ",font = 20).grid(row = 9,column = 1)
            Label(ph,text = d[0][1], font = 20).grid(row = 9,column = 2)
            Label(ph,text = "Phone Number: ",font =20).grid(row = 10, column = 1)
            Label(ph,text = d[0][2],font = 20).grid(row = 10, column =2)
            Label(ph,text = "Email Type: ", font = 20).grid(row = 11, column =1)
            Label(ph,text = c[0][1],font = 20).grid(row = 11, column = 2)
            Label(ph,text = "Email Id: ", font= 20).grid(row = 12, column = 1)
            Label(ph,text = c[0][2],font = 20).grid(row = 12, column = 2)
            def Delete():
                dd = "delete from user_info where ph_id = ?"
                cur.execute(dd,[(pid)])
                ph.destroy()
                showinfo("Information","Contact Deleted Successfully!!!")
                con.commit()
            def Close():
                ph.destroy()
            def Confirmation():
                if True == askyesno("Alert!!!", "Do you want to delete this contact ?"):
                    Delete()
            def Delete1():
                dd = "delete from user_info where ph_id = ?"
                cur.execute(dd,[(pid)])
                con.commit()
            def Edit():
                Close()
                Delete1()
                e1.insert(0,k[0][1])
                e2.insert(0,k[0][2])
                e3.insert(0,k[0][3])
                e4.insert(0,k[0][4])
                e5.insert(0,k[0][5])
                e6.insert(0,k[0][6])
                e7.insert(0,k[0][7])
                e8.insert(0,k[0][8])
                e9.insert(0,k[0][9])
                e10.insert(0,d[0][2])
                e11.insert(0,c[0][2])
                
            Button(ph,text = "Delete",command = Confirmation).grid(row = 17, column = 7)
            Button(ph,text = "Edit",command = Edit).grid(row = 17, column = 12)
            Button(ph,text = "Close",command = Close).grid(row = 17, column = 17)

        lb.bind('<Double-Button-1>',retrieve)
        search.bind('<Button-1>',key_press)
        ph1.bind('<Key>', key_press)
  
    ph.configure(background = "#800020")
    a=PhotoImage(file="contact.gif")
    a=a.subsample(2,2)
    v1= StringVar()
    v2 = StringVar()
    Label(ph,image=a,bg="#E9967A",bd=3).grid(row=1,column=1,columnspan=10)
    Label(ph,text="First Name: ",font = 20,bg = "#800020").grid(row = 2, column = 1)
    e1 = Entry(ph)
    e1.grid(row = 2, column = 8)
    Label(ph,text = "Middle Name: ",font = 20,bg = "#800020").grid(row = 3,column =1)
    e2 = Entry(ph)
    e2.grid(row = 3,column = 8)
    Label(ph,text = "Last Name: ",font = 20,bg = "#800020").grid(row = 4,column = 1)
    e3 = Entry(ph)
    e3.grid(row = 4, column = 8)
    Label(ph,text = "Company Name: ",font = 20,bg = "#800020").grid(row = 5,column = 1)
    e4 = Entry(ph)
    e4.grid(row = 5,column = 8)
    Label(ph,text = "Address: ",font = 20,bg = "#800020").grid(row = 6,column = 1)
    e5 = Entry(ph)
    e5.grid(row = 6,column = 8)
    Label(ph,text = "City: ",font = 20,bg = "#800020").grid(row = 7,column = 1)
    e6 = Entry(ph)
    e6.grid(row = 7,column = 8)
    Label(ph,text = "Pin Code: ",font = 20,bg = "#800020").grid(row = 8,column = 1)
    e7 = Entry(ph)
    e7.grid(row = 8,column = 8)
    Label(ph,text = "Website URL: ",font = 20,bg = "#800020").grid(row = 9,column = 1)
    e8 = Entry(ph)
    e8.grid(row = 9,column = 8)
    Label(ph,text = "Date of Birth: ",font = 20,bg = "#800020").grid(row = 10,column = 1)
    e9 = Entry(ph)
    e9.grid(row = 10,column =8)
    Label(ph,text = "Phone Number ",font = 20,bg = "#800020").grid(row = 11,column = 1)
    e10 = Entry(ph)
    e10.grid(row = 11,column = 8)
    Button(ph,text = "+").grid(row = 11, column =9)
    Label(ph,text = "Select Phone Type: ",fg = "#DC8F25",font = 25,bg = "#800020").grid(row = 12,column = 1)
    Radiobutton(ph,text="Office", variable=v1, value = 'Office',font = 15,bg = "#800020",tristatevalue = 0).grid(row = 12,column = 7)
    Radiobutton(ph,text="Home",variable=v1,value = 'Home',font = 15,bg = "#800020",tristatevalue = 0).grid(row = 12,column = 8)
    Radiobutton(ph,text="Mobile",variable = v1, value = 'Mobile',font = 15,bg = "#800020",tristatevalue = 0).grid(row = 12,column = 9)
    Label(ph,text = "Email id: ",font = 20,bg = "#800020").grid(row =13,column = 1)
    e11 = Entry(ph)
    e11.grid(row = 13,column = 8)
    Label(ph,text = "Select Email Type: ",fg = "#DC8F25",font = 25,bg = "#800020").grid(row = 14,column = 1)
    Radiobutton(ph,text = "Professional",variable = v2, value = 'Professional',font =15,bg = "#800020",tristatevalue = 0).grid(row = 14,column = 8)
    Radiobutton(ph,text = "Personal", variable = v2, value = 'Personal',font = 15,bg = "#800020",tristatevalue = 0).grid(row = 14,column = 9)
    Button(ph,text="Save",command = save).grid(row=15,column=2)
    Button(ph,text="Search",command = search).grid(row=15,column=7)
    Button(ph,text="Edit", command = search).grid(row=15,column=8)
    Button(ph,text="Close",command = close).grid(row=15,column=9)

    ph.mainloop()




