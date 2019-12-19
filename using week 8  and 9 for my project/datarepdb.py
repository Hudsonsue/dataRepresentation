import pymysql 

def menutitle():
	db =pymysql.connect(host="localhost", user="root", password = "root", db="datarepresentation" ,cursorclass = pymysql.cursors.DictCursor)
	
	sql = "select * from menu"
	with db:
		try:
			cursor=db.cursor()
			cursor.execute(sql)
			x = cursor.fetchall()
			return(x)
		
		except Exception as e:
			print(e)
		
