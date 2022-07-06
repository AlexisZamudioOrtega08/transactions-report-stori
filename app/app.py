import os
import threading

from config import config
from common.util import EMailer
from common.util import TxnHelper

from flask import Flask, render_template, request

def create_app():
    app = Flask(__name__)
    txns = (
        TxnHelper(path=os.path.dirname(os.path.abspath(__file__)) + "/data/txns.csv")
        .build()
        .json()
    )

    email_config = config["email"]


    @app.route("/statements", methods=["POST"])
    def index():
        try:
            emailer = EMailer(email_config)
            receiver = request.args.get("email")
            if receiver is None:
                return {"msg": "email not provided"}, 400
            if emailer.is_email(identifier=receiver):
                curr_thread = threading.Thread(
                    target=emailer.send,
                    args=(receiver, render_template("email.html", data=txns)),
                )
                curr_thread.start()
                if curr_thread.is_alive():
                    return {"msg": "email sent"}, 201
                else:
                    return {"msg": "email not sent"}, 500
            else:
                return {"msg": "email not valid"}, 400
        except Exception as e:
            print(e)
            return {"msg": "email not sent"}, 50


    def error_404(error):
        return {"msg": "page not found"}, 404


    def error_405(error):
        return {"msg": "method not allowed"}, 405


    def error_500(error):
        return {"msg": "internal server error"}, 500

    app.config.from_object(config["development"])
    app.secret_key = config["development"].SECRET_KEY
    app.register_error_handler(404, error_404)
    app.register_error_handler(405, error_405)
    app.register_error_handler(500, error_500)

    return app
