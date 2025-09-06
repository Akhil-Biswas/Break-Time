from dotenv import dotenv_values

env = dotenv_values("/storage/emulated/0/Break-Time/.env")

class Mysql:
    """
    Stores MySQL database connection settings from environment variables.
    
    Attributes
    ----------
    MYSQL_HOST : str
        Database host.
    MYSQL_PORT : str
        Database port.
    MYSQL_USER : str
        Database username.
    MYSQL_PASSWORD : str
        Database password.
    MYSQL_DATABASE : str
        Database name.
    """
    MYSQL_HOST = env.get("MYSQL_HOST")
    MYSQL_PORT = env.get("MYSQL_PORT")
    MYSQL_USER = env.get("MYSQL_USER")
    MYSQL_PASSWORD = env.get("MYSQL_PASSWORD")
    MYSQL_DATABASE = env.get("MYSQL_DATABASE")

class Session:
    """
    Stores Session Secret_key from environment variables.
    
    Attributes
    ----------
    secret_key : str
        app secret_key.
    """
    secret_key = env.get("session_secret_key")
if __name__ =="__main__":
    print(f"MYSQL_HOST{MYSQL_HOST}")
    print(f"MYSQL_USER{MYSQL_USER}")