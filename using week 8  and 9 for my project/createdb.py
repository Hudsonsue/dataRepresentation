import pymysql 
db =pymysql.connect(host="localhost", user="root", password = "root",database = "datarepresentation", datcursorclass = pymysql.cursors.DictCursor)
cursor=db.cursor()
#cursor.execute("CREATE DATABASE datarepresentation)
cursor.execute("CREATE TABLE student (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age INT)")