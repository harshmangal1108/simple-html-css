#C:\Users\Harsh\AppData\Local\Programs\Python\Python37\python.exe
print("Content-Type : text/html") # giving path to pyhton.exe,telling about content type
print()



### getting data from html
import cgi
import cgitb
cgitb.enable()
cgitb.enable(display=0, logdir="C:\Users\Harsh\Desktop\New folder")

print("<h1> Welcome to Python Web Programming</h1>")
print("<hr/")
print("<h2> Using Input Tags</h2>")

form=cgi.FieldStorage()

user_name=form.getvalue("uname")
password=form.getvalue("password")

### storing into database
import mysql.connector
con=mysql.connector.connect(host="localhost",database="mlproject",user="root",password="")
cur=con.cursor()

cur.execute("insert into users values(%s,%s)",(user_name,password))
cur.close()
con.close()