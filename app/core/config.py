from typing import Final

from dotenv import find_dotenv, dotenv_values

env = dotenv_values(find_dotenv())

class Database:
    """Database configuration."""

    MYSQL_HOST: Final[str] = env.get("MYSQL_HOST", "localhost")
    MYSQL_USER: Final[str] = env.get("MYSQL_USER", "root")
    MYSQL_PORT: Final[int] = int(env.get("MYSQL_PORT", 3306))
    MYSQL_PASSWORD: Final[str] = env.get("MYSQL_PASSWORD", "")
    MYSQL_DATABASE: Final[str] = env.get("MYSQL_DATABASE", "break_time")


if __name__ == "__main__":
    print(Database.MYSQL_HOST)
    print(Database.MYSQL_USER)
    print(Database.MYSQL_PORT)
    print(Database.MYSQL_DATABASE)