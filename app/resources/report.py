import threading
from config import config
from common.util import EMailer
from common.util import TxnHelperDB

from flask import request
from flask import render_template
from flask_restful import Resource
from flask_pydantic import validate
from models.user import User as UserModel


class Report(Resource):
    @validate()
    def post(self):
        try:
            user_id = request.args.get("user_id")
            if not user_id:
                return {"msg": "user_id is required"}, 400
            if not user_id.isdigit():
                return {"msg": "user_id must be an integer"}, 400
            user = UserModel.find_by_id(user_id)
            if not user:
                return {"msg": "user not found"}, 404
            user = user.json()
            txns = TxnHelperDB(user_id)
            if len(txns.txns) != 0:
                txns = txns.json()
                txns["first_name"] = user["first_name"].capitalize()
                txns["last_name"] = user["last_name"].capitalize()
                emailer = EMailer(config=config["email"])
                curr_thread = threading.Thread(
                    target=emailer.send,
                    args=(user["email"], render_template("email.html", data=txns)),
                )
                curr_thread.start()
                if curr_thread.is_alive():
                    return {"msg": "email sent"}, 201
                else:
                    return {"msg": "email not sent"}, 500
            else:
                return {"msg": "no transactions found"}, 404

        except Exception as e:
            print(e)
            return {"msg": "email not sent"}, 500
