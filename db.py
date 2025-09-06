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
    except:
        print("***************************************************************")
class User:
    def __init__(self,userid,fname, mname, lname, departmentid, sectionid, tel, email, password):
        self.userid = userid
        self.fname = fname
        self.mname = mname
        self.lname = lname
        self.departmentid = departmentid
        self.sectionid = sectionid
        self.tel = tel
        self.email = email
        self.password = password

    def saveindatabase(self):
        '''Save '''
        try:       
            conn= connectToMysqlServer()
            cursor = conn.cursor()

            cursor.execute("USE railway;")
            query = '''
                CREATE TABLE IF NOT EXISTS user (
                userid INT AUTO_INCREMENT PRIMARY KEY,
                fname VARCHAR(50),
                mname VARCHAR(50),
                lname VARCHAR(50),
                departmentid INT,
                sectionid INT,
                tel VARCHAR(15),
                email VARCHAR(50),
                password VARCHAR(50)
                );
                '''
            cursor.execute(query)
            conn.commit()     
            print("Table created successfully!")
            # SQL for add insert data
            insert_query = """
                INSERT INTO user (fname, mname, lname, departmentid, sectionid, tel, email, password)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """
            values = (self.fname, self.mname, self.lname,self.departmentid, self.sectionid, self.tel, self.email,self.password)
            cursor.execute(insert_query,values)
             
            conn.commit()
            cursor.close()
        except :
            print("Server connection Failed")
class Login:
        def __init__(self,tel,password):
            self.tel = tel
            self.password = password
        def authenticate(self):
            try:
                conn= connectToMysqlServer()
                cursor = conn.cursor()
                cursor.execute("USE railway;")
                query = ''' SELECT userid, fname, mname ,lname, departmentid,sectionid,tel,email FROM user WHERE  tel = %s AND password = %s'''
                values = (self.tel, self.password)
                cursor.execute(query,values)
                result = cursor.fetchone()
                cursor.close()
                
                print(self.tel, self.password)
                print(result)
                if result :
                    print("login succesfully")
                    return result
                else:
                    print("No user Found")
       
            except Exception as e:
                print(e)

if __name__ == "__main__":
    # Example usage
    user1 = User(
    userid=1,
    fname="Sita",
    mname="Ram",
    lname="Chandra",
    departmentid=1,
    sectionid=1,
    tel="1234567890",
    email="ram@example.com",
    password = 'sita'
    )
    #user1.saveindatabase()
    
    user2 = User(
    userid=2,
    fname="Radhe",
    mname="",
    lname="Krishna",
    departmentid=0,
    sectionid=1,
    tel="123890",
    email="radhe@example.com",
    password = 'radhe'
    )
    #user2.saveindatabase()
    
    user = Login(
    tel="123890",
    password = "radhe"
    )
    user.authenticate()