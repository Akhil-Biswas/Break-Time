from typing import Final

from dotenv import find_dotenv, dotenv_values

env: dict[str, str | None] = dotenv_values(find_dotenv())

class ApiConfig:
    NAME: Final = "Break Time API"
    VERSION: Final = "0.1.0"
    DESCRIPTION: Final = "Backend API for the Break Time application."

    DEVELOPER_NAME: Final= "Your Name"
    DEVELOPER_EMAIL: Final = "your@email.com"
    GITHUB: Final = "Akhil-Biswas"
    CONTACT_URL: Final = "https://yourwebsite.com"

class Database:
    """Database configuration."""

    MYSQL_HOST: Final[str] = env.get("MYSQL_HOST") or "localhost"
    MYSQL_USER: Final[str] = env.get("MYSQL_USER") or "root"
    MYSQL_PORT: Final[int] = int(env.get("MYSQL_PORT") or "3306")
    MYSQL_PASSWORD: Final[str] = env.get("MYSQL_PASSWORD") or ""
    MYSQL_DATABASE: Final[str] = env.get("MYSQL_DATABASE") or "break_time"


if __name__ == "__main__":
    print(Database.MYSQL_HOST)
    print(Database.MYSQL_USER)
    print(Database.MYSQL_PORT)
    print(Database.MYSQL_DATABASE)