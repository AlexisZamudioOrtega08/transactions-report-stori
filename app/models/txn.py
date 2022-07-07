from operator import index
from db import db
from datetime import datetime
from sqlalchemy import Column, Float, Integer, Boolean, DateTime


class Txn(db.Model):
    __tablename__ = "txns"
    id = Column(
        Integer, primary_key=True, autoincrement=True, nullable=False, index=True
    )
    user_id = db.Column(
        db.Integer, db.ForeignKey("users.id"), nullable=False, index=True
    )
    txn = Column(Boolean, nullable=False)
    amount = Column(Float, nullable=False)
    date = Column(DateTime, nullable=False)

    def __init__(self, user_id, txn, amount):
        self.user_id = user_id
        self.txn = txn
        self.amount = amount
        self.date = datetime.now()

    def json(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "txn": int(self.txn),
            "amount": self.amount,
            "date": str(self.date),
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
    def find_by_user_id(cls, user_id: int) -> list:
        """
        Find all transactions by user id.
        :param user_id: The id of the user.
        :return: The transactions.
        """
        return cls.query.filter_by(user_id=user_id).all()

    def save_to_db(self):
        db.session.add(self)

    def commit(self, id: bool = False) -> int:
        """
        Commit the changes to the database.
        :return: The id of the object if required.
        """
        db.session.commit()
        if id:
            db.session.refresh(self)
            return self.id

    def rollback(self):
        db.session.rollback()
