import pymysql
"""a=pymysql.connect("localhost","root","","test")
cursor=a.cursor()
sql="CREATE DATABASE sin"
cursor.execute(sql)
a.close()
b=pymysql.connect("localhost","root","","sin")
cursor=b.cursor()
sql="CREATE TABLE mathi(name CHAR(20) NOT NULL,fees CHAR(20) NOT NULL,year CHAR(20))"
cursor.execute(sql)
b.close()
c=pymysql.connect("localhost","root","","sin")
cursor=c.cursor()
sql="INSERT INTO mathi(name,fees,year)VALUES('python',35000,1989),('php',20000,1990),('java',15000,1980)"
try:
    cursor.execute(sql)
    c.commit()
except:
    c.rollback()
c.close()
d=pymysql.connect("localhost","root","","sin")
cursor=d.cursor()
sql="UPDATE mathi set name='ruby' WHERE fees=20000"
cursor.execute(sql)
d.commit()
d.close()"""
e=pymysql.connect("localhost","root","","sin")
cursor=e.cursor()
sql="SELECT * FROM mathi WHERE fees=15000 and name='java'"
cursor.execute(sql)
e.close()


