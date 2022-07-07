from operator import le
import smtplib
import datetime
import re, os, csv
from models.txn import Txn as TxnModel
from typing_extensions import Self
from email.message import EmailMessage
from email_validator import validate_email


def is_email(identifier: str) -> bool:
    """
    Check if the given email is valid.
    :param identifier: To define if is mail.
    :return: True if the email is valid, False otherwise.
    """
    try:
        if identifier is None:
            return False
        if validate_email(identifier).email:
            return True
        else:
            return False
    except Exception as e:
        return False


class TxnHelperDB:
    def __init__(self, user_id: int):
        self.user_id = user_id
        self.txns = TxnModel.find_by_user_id(user_id)
        self.debit_avg = 0
        self.credit_avg = 0
        self.total_balance = 0
        self.build()

    def build(self):
        if len(self.txns) > 0:
            self.group_by_month()
            self.set_averages()
            self.count_txns()
        else:
            return None

    def json(self) -> dict:
        return {
            "adb": self.debit_avg,
            "aca": self.credit_avg,
            "tb": self.total_balance,
            "txns": list(self.monthly_txns.items()),
            "date": list(
                {
                    "day": self.curr_day,
                    "month": self.curr_month,
                    "year": self.curr_year,
                }.items()
            ),
        }

    def count_txns(self):
        for txn in self.monthly_txns:
            self.monthly_txns[txn] = len(self.monthly_txns[txn])

    def group_by_month(self):
        self.curr_year = datetime.datetime.now().year
        self.curr_day = datetime.datetime.now().day
        self.curr_month = datetime.date(
            self.curr_year, int(datetime.datetime.now().month), 1
        ).strftime("%B")
        self.monthly_txns = {}
        for txn in self.txns:
            month = txn.date.strftime("%B")
            if month not in self.monthly_txns:
                self.monthly_txns[month] = [txn.json()]
            else:
                self.monthly_txns[month].append(txn.json())

    def set_averages(self):
        debit_txn = 0
        credit_txn = 0
        for month in self.monthly_txns:
            for txn in self.monthly_txns[month]:
                if int(txn["txn"]) == 0:
                    self.debit_avg -= float(txn["amount"])
                    self.total_balance -= float(txn["amount"])
                    debit_txn += 1
                if int(txn["txn"]) == 1:
                    self.credit_avg += float(txn["amount"])
                    self.total_balance += float(txn["amount"])
                    credit_txn += 1
        if debit_txn > 0:
            self.debit_avg /= debit_txn
        self.debit_avg = round(self.debit_avg, 2)
        if credit_txn > 0:
            self.credit_avg /= credit_txn
        self.credit_avg = round(self.credit_avg, 2)
        self.total_balance = round(self.total_balance, 2)


class EMailer:
    def __init__(self, config: object) -> None:
        self.config = config
        self.msg = EmailMessage()
        self.msg["Subject"] = "Your report is ready!"
        self.msg["From"] = self.config.MAIL_USERNAME

    def set_receiver(self, receiver) -> None:
        self.receiver = receiver
        self.msg["To"] = self.receiver

    def set_content(self, body: str) -> None:
        self.msg.set_content(body, subtype="html")

    def send(self, receiver, rendered) -> None:
        try:
            self.set_receiver(receiver=receiver)
            self.set_content(body=rendered)
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
                smtp.login(self.config.MAIL_USERNAME, self.config.MAIL_PASSWORD)
                smtp.send_message(self.msg)
            return True
        except Exception as e:
            raise e
