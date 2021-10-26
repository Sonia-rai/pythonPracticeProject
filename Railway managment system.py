import mysql.connector
import os
import platform

# import pandas as pd
pnr = 1024
mydb = mysql.connector.connect(host="localhost",
                               user="root",
                               password="tiger",
                               database="rail");
mycursor = mydb.cursor()


def railresmenu():
    print("Railway reservation ")
    print("1.Train detail")
    print("2.Reservation of ticket")
    print("3.Cancellation of ticket")
    print("4.Display pnr status")
    print("5.Quit")

    n = int(input("Enter your choice"))
    if (n == 1):
        traindetail()
    elif (n == 2):
        reservation()
    elif (n == 3):
        cancel()
    elif (n == 4):
        displayPNR()
    elif (n == 5):
        exit(0)
    else:
        print("WRONG CHOICE!!!")


def traindetail():
    print("Train details")
    ch = 'y'
    while (ch == 'y'):
      l = []
      name = input("Enter Train Name :")
      l.append(name)
      tnum = int(input("Enter Train Number :"))
      l.append(tnum)
      ac1 = int(input("Enter Number of AC    1 Class seats"))
      l.append(ac1)
      ac2 = int(input("Enter Number of AC 2 Class seats"))
      l.append(ac2)
      ac3 = int(input("Enter Number of ac 3 class seats"))
      l.append(ac3)
      slp = int(input("enter number of sleeper class seats"))
      l.append(slp)
      train = (l)
      sql = "insert into traindetail(tname,tnum,ac1,ac2,ac3,slp)values(%s,%s,%s,%s,%s,%s)"
      mycursor.execute(sql, train)
      mydb.commit()
      print("insertion complete")
    print("do you want to insert more train detail")
    ch = input("enter yes/no")
    print('\n' * 10)

railresmenu()


def reservation():
    global pnr
    l1 = []
    pname = input("enter passanger name")
    l1.append(pname)
    age = input("enter age of passanger")
    l1.append(age)
    trainno = input("enter train number")
    l1.append(trainno)
    np = int(input("enter number of passanger:"))
    l1.append(np)
    print("select a class you would like to travel in")
    print("1.ac first class")
    print("2.ac second class")
    print("3.ac third class")
    print("4.sleper class")
    cp = int(input("enter your choice"))
    if (cp == 1):
        amount = np * 1000
        cls = 'ac1'
    elif (cp == 2):
        amount = np * 800
        cls = 'ac2'
    elif (cp == 3):
        amount = np * 500
        cls = 'ac3'
    else:
        amount = np * 350
        cls = 'slp'
    l1.append(cls)
    print("total amount to be paid:", amount)
    l1.append(amount)
    pnr = pnr + 1
    print("pnr number:", pnr)
    print("status: confirm")
    sts = 'conf'
    l1.append(sts)
    l1.append(pnr)
    train1 = (l1)
    sql = "insert into passengers(pname,age,trainno,noofpas,cls,amt,status,pnrno)values(%s,%s,%s,%s,%s,%s,%s,%s)"
    mycursor.execute(sql, train1)
    mydb.commit()
    print("insertion complete")
    print("go back to menu")
    print('\n' * 10)

    railresmenu()


def cancel():
    print("ticket cancel window")
    pnr = input("enter pnr for cancellation of ticket")
    pn = (pnr,)
    sql = "update passangers set status='deleted' where pnrno=%s"
    mycursor.execute(sql, pn)
    mydb.commit()
    print("deletion complete")
    print("go back to menu")
    print('\n' * 10)

    railresmenu()
    # railresmenu()


def displayPNR():
    print("pnr status window")
    pnr = input("enter pnr number")
    pn = (pnr,)
    sql = "select * from passengers where pnrno=%s"
    mycursor.execute(sql, pn)
    res = mycursor.fetchall()
    # mydb.commit()
    print("pnr status are as follows ")
    print("(pname,age,trainno, noofpas,cls,amt,status, pnrno)")
    for x in res:
        print(x)
        # print("deletion complete")
    print("go back to menu")
    print('\n' * 10)

    railresmenu()


railresmenu()








