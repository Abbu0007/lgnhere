from tkinter import *
import sqlite3
root = Tk()
lbl=Label(root, text="Employee Manangement System",bg="BLue",font=("Arial Bold",50) )
lbl.place(x=200,y=0)
root.geometry("1500x1500")
root.resizable(0,0)

conn=sqlite3.connect("gender_database.db")
cursor=conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS employee(
               ID INTEGER PRIMARY KEY AUTOINCREMENT,
               uname        TEXT,
               adr          TEXT,
               rl           TEXT,
               slr          INT
               )""")

conn.commit()
conn.close()

label_username=Label(root,text="Username", font=("Arial Bold",20))
label_username.place(x=0,y=90)

label_address=Label(root,text="Address", font=("Arial Bold",20))
label_address.place(x=0,y=140)

label_role=Label(root,text="Role", font=("Arial Bold",20))
label_role.place(x=0,y=190)

label_salary=Label(root,text="Salary", font=("Arial Bold",20))
label_salary.place(x=0,y=240)

label_delete_box=Label(root,text="Delete Box", font=("Arial Bold",20))
label_delete_box.place(x=0,y=370)

label_update_box=Label(root,text="Update Box", font=("Arial Bold",20))
label_update_box.place(x=0,y=450)

username= Entry (root, width = 30)
username.place(x=170, y=100,height=30)

address= Entry (root, width = 30)
address.place(x=170, y=150,height=30)

role= Entry (root, width = 30)
role.place(x=170, y=200,height=30)

salary= Entry (root, width = 30)
salary.place(x=170, y=250,height=30)

delete_box= Entry (root, width = 30)
delete_box.place(x=170, y=370,height=30)

update_box= Entry (root, width = 30)
update_box.place(x=170, y=450,height=30)

def add():
    conn= sqlite3.connect("gender_database.db")
    c=conn.cursor()
    c.execute("INSERT INTO employee(uname,adr,rl,slr) VALUES (?,?,?,?)",(username.get(),address.get(),role.get(),salary.get()))
    conn.commit()
    conn.close()
    username.delete(0,END)
    address.delete(0,END)
    role.delete(0,END)
    salary.delete(0,END)

def retrieve():
    conn=sqlite3.connect("gender_database.db")
    c= conn.cursor()
    c.execute("SELECT * FROM employee")
    records=c.fetchall()
    print_records=''
    for record in records:
        print_records += str(record[0]) + ' ' + str(record[1]) + ' ' + str(str(record[2])) + str(str(record[3])) + str(str(record[4])) + "\n"
    query_label= Label(root, text=print_records)
    query_label.place(x=0,y=450)
    conn.close()

def delete():
    conn=sqlite3.connect("gender_database.db")
    c=conn.cursor()
    c.execute("DELETE FROM employee WHERE ID="+delete_box.get())
    conn.commit()
    conn.close()
    delete_box.delete(0,END)
    retrieve()

def edit():
    
    global editor
    editor=Tk()
    editor.title('Update Data')
    editor.geometry('300x480')
    conn=sqlite3.connect('gender_database.db')
    c=conn.cursor()
    record_id=update_box.get()
    c.execute("SELECT * FROM employee WHERE ID=?", (record_id,))
    records=c.fetchall()
    # print(records)  

    global username_editor
    global address_editor
    global role_editor
    global salary_editor

    username_editor=Entry(editor,width=30)
    username_editor.grid(row=0,column=1,padx=20,pady=(10,0))
    address_editor=Entry(editor,width=30)
    address_editor.grid(row=1,column=1)
    role_editor=Entry(editor,width=30)
    role_editor.grid(row=2,column=1)
    salary_editor=Entry(editor,width=30)
    salary_editor.grid(row=3,column=1)

    username_label=Label(editor,text='Username')
    username_label.grid(row=0,column=0,pady=(10,0))

    Address_label=Label(editor,text="Address")
    Address_label.grid(row=1,column=0)

    role_label=Label(editor,text="Role")
    role_label.grid(row=2,column=0)

    salary_label=Label(editor,text="Salary")
    salary_label.grid(row=3,column=0)

    for record in records:
        username_editor.insert(0,record[1])
        address_editor.insert(0,record[2])
        role_editor.insert(0,record[3])
        salary_editor.insert(0,record[4])
    
    update_box.delete(0,END)
    edit_btn=Button(editor,text="Save",command=lambda:update(record_id))
    edit_btn.grid(row=6,column=0,columnspan=2,pady=10,padx=10,ipadx=125)


def update(record_id):
    conn=sqlite3.connect('gender_database.db')
    c=conn.cursor()
    c.execute("""
            UPDATE employee SET
            uname= :u,
            adr= :a,
            rl= :r,
            slr= :s
              WHERE Id = :id""",
              {
                  'u':username_editor.get(),
                  'a':address_editor.get(),
                  'r':role_editor.get(),
                  's':salary_editor.get(),
                  'id':record_id
              }
    ) 
    conn.commit()
    conn.close()
    editor.destroy()


btn_add=Button (root,text="Add",font=("Arial Bold",20),command=add)
btn_add.place(x=0,y=300)
btn_retrieve=Button (root,text="Retrive",font=("Arial Bold",20),command=retrieve)
btn_retrieve.place(x=100,y=300)
btn_delete=Button (root,text="Delete",font=("Arial Bold",20),command=delete)
btn_delete.place(x=400,y=350)
btn_update=Button (root,text="Update",font=("Arial Bold",20),command=edit)
btn_update.place(x=400,y=450)

root.mainloop()