import os, csv
import smtplib
import datetime
from typing_extensions import Self
from email.message import EmailMessage


class TxnHelper:
    def __init__(self, path: str) -> None:
        """
        :param file_name: name of the csv file or full path
        """

        self.file_path = os.path.abspath(path)
        self.debit_avg = 0
        self.credit_avg = 0
        self.total_balance = 0

        if not os.path.exists(self.file_path):
            raise FileNotFoundError("File not found")

    def build(self) -> Self:
        try:
            self.group_by_month()
            self.set_averages()
            self.count_monthly_transactions()
            return self
        except Exception as e:
            print(e)
            return None

    def group_by_month(self) -> list:
        self.curr_year = datetime.datetime.now().year
        self.curr_day = datetime.datetime.now().day
        self.curr_month = datetime.date(
            self.curr_year, int(datetime.datetime.now().month), 1
        ).strftime("%B")
        txns = self.read_csv()
        self.monthly_txns = {}
        for txn in txns[1:]:
            month = txn[1].split("/")[0]
            month = datetime.date(self.curr_year, int(month), 1).strftime("%B")
            if month not in self.monthly_txns:
                self.monthly_txns[month] = [txn]
            else:
                self.monthly_txns[month].append(txn)

    def read_csv(self):
        with open(self.file_path, "r") as f:
            reader = csv.reader(f)
            return list(reader)

    def set_averages(self):
        for month in self.monthly_txns:
            for txn in self.monthly_txns[month]:
                if txn[2][0] == "-":
                    self.debit_avg -= float(txn[2][1:])
                    self.total_balance -= float(txn[2][1:])
                if txn[2][0] == "+":
                    self.credit_avg += float(txn[2][1:])
                    self.total_balance += float(txn[2][1:])

        self.debit_avg /= len(self.monthly_txns)
        self.debit_avg = round(self.debit_avg, 2)
        self.credit_avg /= len(self.monthly_txns)
        self.credit_avg = round(self.credit_avg, 2)

    def json(self) -> dict:
        return {
            "adb": self.debit_avg,
            "aca": self.credit_avg,
            "tb": self.total_balance,
            "txns": self.monthly_txns,
            "date": list(
                {
                    "day": self.curr_day,
                    "month": self.curr_month,
                    "year": self.curr_year,
                }.items()
            ),
        }

    def count_monthly_transactions(self) -> None:
        for month in self.monthly_txns:
            self.monthly_txns[month] = len(self.monthly_txns[month])
        self.monthly_txns = list(self.monthly_txns.items())

    def __str__(self) -> str:
        return f"debit_avg: {self.debit_avg}, \ncredit_avg: {self.credit_avg}, \ntotal_balance: {self.total_balance}"


class EMailer:
    def __init__(self, config: object) -> None:
        self.config = config
        self.msg = EmailMessage()
        self.msg["Subject"] = "Your statement is ready!"
        self.msg["From"] = self.config.MAIL_USERNAME

    def set_content(self, body: str) -> None:
        self.msg.set_content(body, subtype="html")

    def send(self, receiver: str) -> None:
        try:
            self.receiver = receiver
            self.msg["To"] = self.receiver
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
                smtp.login(self.config.MAIL_USERNAME, self.config.MAIL_PASSWORD)
                smtp.send_message(self.msg)
            return True
        except Exception as e:
            print(e)
            return False
