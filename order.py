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
    def __init__(self, time, userId, itemId, quantity, orderStatus, paymentStatus, orderId=None):
        self.orderId = orderId  #set by database 
        self.time = time
        self.userId = userId
        self.itemId = itemId
        self.quantity = quantity
        self.orderStatus = orderStatus
        self.paymentStatus = paymentStatus
    
    
    def placeOrder(self):
        try:
            conn= connectToMysqlServer()
            cursor= conn.cursor()
            # select database 
            cursor.execute(f"USE {Mysql.MYSQL_DATABASE}")
            print(f"using database {Mysql.MYSQL_DATABASE}" )
            #Creating Order table 
            query = '''
            CREATE TABLE IF NOT EXISTS orders(
            order_id INT PRIMARY KEY AUTO_INCREMENT,
            order_time DATETIME,
            user_id INT,
            item_id INT,
            item_quantity INT,
            order_status VARCHAR(50),
            payment_status VARCHAR(50)
            );
            '''
            cursor.execute(query)
            # insert data
            query ='''
            INSERT INTO orders(order_time,user_id,item_id,item_quantity) values(%s,%s,%s,%s)
            '''
            values =(self.time,self.userId,self.itemId,self.quantity)
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
       time =datetime.now(),
       userId = 12,
       itemId =24,
       quantity = 2,
       orderStatus = "ok",
       paymentStatus = "paid",
    ).placeOrder()