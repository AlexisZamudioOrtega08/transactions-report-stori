import os
from dotenv import load_dotenv


class Config:
    def __init__(self):
        self.SECRET_KEY = "your_secret_key"
        self.load_environment()

        self.DEBUG = True

    def load_environment(self) -> None:
        # Please create a .env file in the root directory of the project
        path = os.path.abspath('../') + "/.env"
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
