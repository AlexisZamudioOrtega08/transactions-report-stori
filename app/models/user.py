from db import db
from datetime import datetime
from sqlalchemy import Column, Integer, DateTime


class User(db.Model):
    __tablename__ = "users"
    id = Column(
        Integer, primary_key=True, autoincrement=True, nullable=False, index=True
    )
    first_name = Column(db.String(30), nullable=False)
    last_name = Column(db.String(30), nullable=False)
    email = Column(db.String(50), nullable=False, unique=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    txns = db.relationship("Txn", backref="user", lazy=True, cascade="all, delete")

    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def json(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "created_at": str(self.created_at),
        }

    @classmethod
    def find_all(cls) -> object:
        """
        Find all transactions by user id.
        :param user_id: The id of the user.
        :return: The transactions.
        """
        return cls.query.all()

    @classmethod
    def find_by_id(cls, id: int) -> object:
        """
        Find a transaction by id.
        :param id: The id of the transaction.
        :return: The transaction.
        """
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_by_email(self, email: str) -> object:
        """
        Find a user by email.
        :param email: The email of the user.
        :return: The user.
        """
        return self.query.filter_by(email=email).first()

    def save_to_db(self):
        db.session.add(self)

    def commit(self, id=False):
        db.session.commit()
        if id:
            db.session.refresh(self)
            return self.id

    def rollback(self):
        db.session.rollback()
