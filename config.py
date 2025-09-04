from dotenv import dotenv_values

env = dotenv_values("/storage/emulated/0/Break-Time/.env")

class Mysql:
    MYSQL_HOST = env.get("MYSQL_HOST")
    MYSQL_PORT = env.get("MYSQL_PORT")
    MYSQL_USER = env.get("MYSQL_USER")
    MYSQL_PASSWORD = env.get("MYSQL_PASSWORD")
    MYSQL_DATABASE = env.get("MYSQL_DATABASE")
    
if __name__ =="__main__":
    print(type(Mysql.MYSQL_HOST))