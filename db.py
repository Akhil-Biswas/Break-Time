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
        pass        
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
        self.enrolled_date = datetime.now()
        
    def saveindatabase(self):
        '''Save '''
        try:       
            conn= connectToMysqlServer()
            cursor = conn.cursor()

            # insert in users 
            query = """
                INSERT INTO users (f_name,m_name, l_name, mobile_number,email_id,pass, enrolled_date ,last_modify_date) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """
            values = (self.fname, self.mname, self.lname, self.tel, self.email,self.password,self.enrolled_date,self.enrolled_date)
            
            cursor.execute(query,values)
             # insert in student table
            userId = cursor.lastrowid
            query = """
                INSERT INTO student (students_id, department, section)
                VALUES (%s, %s,%s)
                """
            values = (userId,self.departmentid, self.sectionid)
            cursor.execute(query,values)
            print("user created.. as student")
        except Exception as e :
            print(e)
        finally :
            conn.commit()
            cursor.close()
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
    userid=None, 
    fname="Krishna",
    mname="A",
    lname="B",
    departmentid=1,
    sectionid=1,
    tel="1234567890",
    email="krishna@example.com",
    password = 'ytfitcitc'
    )
    user1.saveindatabase()
    
    user2 = User(
    userid=None,
    fname="Radhe",
    mname="A",
    lname="B",
    departmentid=0,
    sectionid=1,
    tel="1237890",
    email="radhe@example.com",
    password = 'ytfitcitc'
    )
    #user2.saveindatabase()
    
    user = Login(
    tel="8016327566",
    password = "akhil"
    )
    #user.authenticate()
    #connectToMysqlServer()