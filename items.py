import mysql.connector
from config import Mysql

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
    except Exception as e:
        print(e)
        print("***************************************************************")
class Items:
    def __init__(self,itemId,itemName,itemPrice,category,vegFlag,restaurant):
        self.itemId = itemId
        self.itemName = itemName
        self.itemPrice = itemPrice
        self.category = category
        self.vegFlag = vegFlag
        self.restaurant=restaurant
        self.img = f'{itemId}.jpg'
        #defult velue for get item
        self.isfev = False  #only for login user 
        self.totalFev = 0
        
    def saveItemInDatabase(self):
        try :
            conn= connectToMysqlServer()
            cursor = conn.cursor()
             
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {Mysql.MYSQL_DATABASE};")
            print(f"Database {Mysql.MYSQL_DATABASE} created successfully!")
            cursor.execute(f"USE {Mysql.MYSQL_DATABASE};")
            query = '''
                CREATE TABLE IF NOT
                EXISTS items (
                item_id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100),
                price INT,
                veg_flag INT,
                category INT,
                restaurant INT,
                FOREIGN KEY (category) REFERENCES categories(category_id),
                FOREIGN KEY (veg_flag) REFERENCES food_type(type_id),
                FOREIGN KEY (restaurant) REFERENCES restaurants(restaurant_id)
                );
                '''
            cursor.execute(query)
            conn.commit() 
            print("Table Created..") 
            query ='''
            INSERT INTO items(item_id,name,price,category,veg_flag,restaurant) VALUES (%s, %s, %s, %s,%s, %s) 
            '''
            values = (self.itemId,
            self.itemName,
            self.itemPrice,
            self.category,
            self.vegFlag,
            self.restaurant
            )
            print(f'velues are : \n    Name {self.itemName},\n    Price : {self.itemPrice}\n    category: {self.category} \n    veg Flag: {self.vegFlag}\n    Restaurant: {self.restaurant}')
            
            cursor.execute(query,values)
            print(f"Item {cursor.lastrowid} stored to Database ")
            
            return cursor.lastrowid  #return auto_increment velue from database  (for save image with rename to item id)
        except Exception as e:
            print(e)
        finally:
            conn.commit()
            cursor.close()
            conn.close()
            print("+++++++++++++++++++++++++++++")
    @staticmethod
    def getAllItem():
        try:
            conn= connectToMysqlServer()
            cursor = conn.cursor()
            cursor.execute(f"USE {Mysql.MYSQL_DATABASE};")
            
            query = "SELECT * FROM items"
            cursor.execute(query)
            items = cursor.fetchall()
            return items
        except Exception as e :
            print(e)
        finally:
            cursor.close()
            conn.close()
if __name__ == "__main__ ":   
    item1 = Items(
        itemId = None,
        itemName = "samosa",
        itemPrice = 10,
        vegFlag = "1",
        category = 1,
        restaurant = 1
    ).saveItemInDatabase

    item2 = Items(
        itemId = None,
        itemName = "Roti",
        itemPrice = 10,
        vegFlag = 1,
        category ='1',
        restaurant = 1
    ).saveItemInDatabase()

    #for display in html
    items=Items.getAllItem()

    for item in items:
        itemId = item[0],
        itemName = item[1],
        itemPrice = item[2],
        vegFlag = item[3],
        category = item[4],
        restaurant = item[5]
    
        print(item)
        print(itemName)
        print(itemPrice)
        print(vegFlag)
        print('=======')
  
     # {"itemid":"1","name": "Sandwich", "type":"veg","price":"30.00","noFev":"157","img":"sandwich.png"}
 