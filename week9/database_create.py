import pymysql


db =pymysql.connect(host="localhost", user="root", password = "root", db="datarep" ,cursorclass = pymysql.cursors.DictCursor)