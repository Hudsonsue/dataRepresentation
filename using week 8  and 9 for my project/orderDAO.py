import pymysql
import pymysql.cursors
class orderDAO:
     db=""
    def __init__(self): 
        self.db = pymysql.connect(
        host="localhost",
        user="root",
        password="root",
        database="datarepresentation")
		    
           
   

    def getAll(self):
        cursor = self.db.cursor()
        sql="select * from ordermenu"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        print(results)
        for result in results:
            print(result)
            returnArray.append(self.convertToDictionary(result))

        return returnArray

    def findByID(self, id):
        cursor = self.db.cursor()
        sql="select * from ordermenu where id = %s"
        values = (id,)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.convertToDictionary(result)

    def update(self, values):
        cursor = self.db.cursor()
        sql="update ordermenu set quantity = %s where id = %s"
        cursor.execute(sql, values)
        self.db.commit()
		
     
    def convertToDictionary(self, result):
        colnames=[ 'Item','Author', "Price", Quantity]
        item = {}
        
        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                item[colName] = value
        
        return item
        
orderDAO = OrderDAO()+