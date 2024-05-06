#TO CREATE NEW DATABASES

import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="username",password="your password")
mycursor=mydb.cursor()

def createDatabase(dbName):
	sql="CREATE DATABASE "+dbName;
	mycursor.execute(sql)
createDatabase("stduManage")

import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="username",password="your password",database="stduManage')
mycursor=mydb.cursor()

#TO CREATE A TABLE IN THAT DATABASE
def createStudenttable():
	sql= "create table student(id int,name varchar(255),age int,primary key(id))"
	mycursor.execute(sql)
createStudenttable()

#TO INSERT VALUES 

def insertValuesIntoTables():
	sql="insert into student(id,name,age)values(%s,%s,%s)"
	values=(int(1),'VGLUG',int(11))
	mycursor.execute(sql,values)
	mydb.commit()
insertValuesIntoTables()

#TO INSERT MULTIPLE VALUES

def insertMultiValuesIntoTable():
	sql="insert into student(id,name,age)values(%s,%s,%s)"
	values=[(int(2),"john",int(24)),(int(7),"Mahi",int(42))]
	mycursor.executemany(sql,values)
	mydb.commit()
insertMultiValuesIntoTable()


#TO UPDATE THE VALUES

def updateValues():
	sql="update student set age='25' where name='john'"
	mycursor.execute(sql)
	mydb.commit()
updateValues()


#TO DELETE VALUES

def deleteValuesIntoTable():
	sql='delete from student where name = "john"'
	mycursor.execute(sql)
	mydb.commit()
deleteValuesIntoTable()

#TO FETCH ALL INFORMATION FROM THE TABLE

def fetchAllFromTable():
	sql="select * from student"
	mycursor.execute(sql)
	print(mycursor.fetchall())
fetchAllFromTable()

