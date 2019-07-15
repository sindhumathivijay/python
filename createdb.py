"""""import pymysql
A=pymysql.connect("localhost","root","","test")
cursor=A.cursor()
sql="CREATE DATABASE tech"
cursor.execute(sql)
A.close()
import pymysql
a=pymysql.connect("localhost","root","","tech")
cursor=a.cursor()
sql="CREATE TABLE courses(name CHAR(20) NOT NULL,fees CHAR(20) NOT NULL,year CHAR(20) NOT NULL)"
cursor.execute(sql)
a.close()
import pymysql
db=pymysql.connect("localhost","root","","tech")
cursor=db.cursor()
sql="INSERT INTO courses(name,fees,year)VALUES('python',30000,1990),('php',40000,1980)"
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()
db.close()
import pymysql
B=pymysql.connect("localhost","root","","tech")
cursor=B.cursor()
sql="UPDATE courses SET name='java' WHERE fees=30000"
cursor.execute(sql)
B.commit()
B.close()"""""
import pymysql
x=pymysql.connect("localhost","root","","tech")
cursor=x.cursor()
sql="SELECT * FROM courses WHERE fees>'%s'"%(30000)

cursor.execute(sql)
result=cursor.fetchone()

x.close()

