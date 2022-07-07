import os
from dotenv import load_dotenv


class Config:
    def __init__(self):
        self.SECRET_KEY = "your_secret_key"
        self.load_environment()
        self.DEBUG = True
        self.TESTING = True
        self.DB_CONFIG = {
            "host": os.getenv("MYSQL_DATABASE_HOST_DEV"),
            "user": os.getenv("MYSQL_DATABASE_USER_DEV"),
            "password": os.getenv("MYSQL_DATABASE_PASSWORD_DEV"),
            "db": os.getenv("MYSQL_DATABASE_DB_DEV"),
        }
        self.SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{}:{}@{}/{}".format(
            self.DB_CONFIG["user"],
            self.DB_CONFIG["password"],
            self.DB_CONFIG["host"],
            self.DB_CONFIG["db"],
        )
        self.SQLALCHEMY_TRACK_MODIFICATIONS = False
        self.API_PREFIX = os.getenv("API_PREFIX")

    def load_environment(self) -> None:
        # Please create a .env file in the root directory of the project
        path = os.path.abspath(os.path.dirname(".")) + "/.env"
        print(path)
        if os.path.exists(path=path):
            load_dotenv(path)
            while os.getenv("FLAG") is None:
                load_dotenv(path)
        else:
            raise FileNotFoundError("File .env not found")


class ConfigMail:
    def __init__(self):
        self.MAIL_SERVER = os.getenv("MAIL_SERVER")
        self.MAIL_PORT = os.getenv("MAIL_PORT")
        self.MAIL_USERNAME = os.getenv("MAIL_USERNAME")
        self.MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")


config = {"development": Config(), "email": ConfigMail()}
