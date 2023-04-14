#install requirements - Wamp server
#WAMP=Windows Apache MySQL Php
#it is used to host PHP Pages
#PHP is server side scripting language
#MySQL is a most popular Open Source SQL database
#command for installing mysqllite-connector : pip install mysql-connector-python
#To install tabulate module "pip install tabulate"
import mysql.connector
from tabulate import tabulate
import re
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
con = mysql.connector.connect(host="localhost",user="root",password="",database="registeration")

def insert():
    name=input("Enter Name : ")
    age =input("Enter Age : ")
    if not int(age)>=18 or not age.isdigit():
        age = None
    address=input("Enter Address : ")
    contact=input("Enter Contact : ")
    if len(contact) != 10:
        contact = None
    mail=input("Enter Mail : ")
    if not (re.fullmatch(regex, mail)):
       mail = None
    if age==None:
        print("Invalid Age")
    if contact==None:
        print("Invalid Phone Number")
    if mail==None:
        print("Invalid Email")
    if age==None or contact==None or mail==None:
        print("Record Inserted Unsuccessfully")
        insert()
    else:
        print("Record Inserted Successfully")
        

    res=con.cursor()
    sql = "insert into data (NAME,AGE,ADDRESS,CONTACT,MAIL) values (%s,%s,%s,%s,%s)"
    res.execute(sql,(name,age,address,contact,mail))
    con.commit()#After the commit the data can inserted
    

def select():
    res = con.cursor()
    sql = "SELECT * from data"
    res.execute(sql)
    result = res.fetchall()#Ella record um kedachidhum
    print(tabulate(result,headers=["ID","NAME","AGE","ADDRESS","CONTACT","MAIL"]))

def update():
    print("1.Name")
    print("2.Age") 
    print("3.Address")
    print("4.Contact")
    print("5.Mail")
    option=int(input("Which field you want to update : "))
    if option==1:
        pid=input("Enter your ID : ")
        name = input("Enter your Name : ")
        cur = con.cursor()
        sql="UPDATE data set NAME=%s where PID=%s"
        cur.execute(sql,(name,pid))
        con.commit()
        select()
        print("Update Successfully")
    elif option==2:
        pid=input("Enter your ID : ")
        age = input("Enter your Age : ")
        if not int(age)>=18 or not age.isdigit():
            print("Invalid age or age should be greater than 18")
            update()
        else:
            cur = con.cursor()
            sql="UPDATE data set AGE=%s where PID=%s"
            cur.execute(sql,(age,pid))
            con.commit()
            select()
            print("Update Successfully")
    elif option==3:
        pid=input("Enter your ID : ")
        address = input("Enter your Address : ")
        cur = con.cursor()
        sql="UPDATE data set ADDRESS=%s where PID=%s"
        cur.execute(sql,(address,pid))
        con.commit()
        select()
        print("Update Successfully")
    elif option==4:
        pid=input("Enter your ID : ")
        contact = input("Enter your Contact : ")
        if len(contact)!=10:
            print("Invalid Contact number")
            print("Updation is Unsuccessful")
        else:
            cur = con.cursor()
            sql="UPDATE data set CONTACT=%s where PID=%s"
            cur.execute(sql,(contact,pid))
            con.commit()
            select()
            print("Update Successfully")
    elif option==5:
        pid=input("Enter your ID : ")
        mail = input("Enter your Mail : ")
        if not (re.fullmatch(regex, mail)):
            print("Invalid Mail address")
            print("Updation is Unsuccessful")
        else:
            cur = con.cursor()
            sql="UPDATE data set MAIL=%s where PID=%s"
            cur.execute(sql,(mail,pid))
            con.commit()
            select()
            print("Update Successfully")
    else:
        print("Invalid Syntax")

def delete():
    pid=input("Enter Your Id : ")
    res=con.cursor()
    sql = "delete from data where PID=%s"
    res.execute(sql,(pid,))
    con.commit()
    print("Record Deleted Successfully")

while True:
    print("\n1.Insert Record")
    print("2.Select Record")
    print("3.Update Record")
    print("4.Delete Record")
    print("5.Exit\n")
    choice=int(input("Enter Your Choice : "))
    if choice==1:
        insert()
    elif choice==2:
        select()
    elif choice==3:
        update()
    elif choice==4:
        delete()
    elif choice==5:
        quit()
    else:
        print("Invalid Syntax")
"""Idha validate pannanum"""
    

