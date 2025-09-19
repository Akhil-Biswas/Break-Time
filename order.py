import mysql.connector
from config import Mysql
from datetime import datetime
def connectToMysqlServer():
    '''Connect to MySQL using mysql config '''
    try:
        conn = mysql.connector.connect(
        host=Mysql.MYSQL_HOST,
        port=Mysql.MYSQL_PORT,
        user=Mysql.MYSQL_USER,
        password=Mysql.MYSQL_PASSWORD,
        database=Mysql.MYSQL_DATABASE
        )
        if conn.is_connected():
            print("------------------------------------------------------------")
            print(f"Connected to {Mysql.MYSQL_HOST}")
        return conn
    except:
        print("***************************************************************")
        
class Order:
    def __init__(self, userId, items: dict, orderStatusId, orderId=None):
        """
        items = {
                    item_id: quantity,
                    item_id: quantity, ...
                }
        """
        self.orderId = orderId  #set by database 
        self.time = datetime.now()
        self.userId = userId #from session
        self.items = items
        self.orderStatusId = orderStatusId
    
    
    def placeOrder(self):
        try:
            conn= connectToMysqlServer()
            cursor= conn.cursor()
            # select database 
            cursor.execute(f"USE {Mysql.MYSQL_DATABASE}")
            print(f"using database {Mysql.MYSQL_DATABASE}" )
            
            # 1️⃣  insert data in orders
            query ='''
            INSERT INTO orders (`time`, `user_id`, `status_id`, `payment_id`) values(%s,%s,%s,%s)
            '''
            values =(self.time,self.userId,self.orderStatusId,None)
            cursor.execute(query,values)
            
            
            #  2️⃣  insert data in orders_item
            orderId = cursor.lastrowid
            items = self.items.items() # items() is a dict function to get key value pair
            for itemId, quantity in items:
                print(f"itemId: {itemId}, quantity: {quantity}")
                query ='''
                INSERT INTO `orders_items` (order_id, item_id, quantity, status_id) VALUES (%s,%s,%s,%s)
                '''
                values =(orderId, int(itemId),int(quantity),1)
                cursor.execute(query,values)
            conn.commit()
            
            print("Order placed..")
            conn.close()
            return #msg to user
        except Exception as e:
            print(e)
    def updateOder():
        pass
     
     
    def fetchOrder():
         pass
         
if __name__ == "__main__":
    
    Order(
       # orderId  #set by database 
       userId = 1, #from session
       items = {'1': 4, '2': 2},
       orderStatusId = 1 #one for place order
    ).placeOrder()