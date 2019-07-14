#!/usr/bin/python3
print("Content-type:text/html") # giving path to pyhton.exe,telling about content type
print("")
## getting data from html
import cgi
import cgitb
print("<h1> Welcome to Python Web Programming</h1>")
print("<hr/")
print("<h2> Using Input Tags</h2>")

getdata=cgi.FieldStorage()

guname=getdata.getvalue("uname")
read_pwd=getdata.getvalue("read_passd")
print ("<h2>Hello %s</h2>" % (guname))
print("<h2> your password is %s</h2>" % (read_pwd))
### storing into database
import mysql.connector
con=mysql.connector.connect(host="localhost",database="reko",user="root",password="root11")
cur=con.cursor()

cur.execute("insert into user values(%s,%s)",(guname,read_pwd))
con.commit()
cur.close()
con.close()
print("<h1> RECORDED </h1>")


