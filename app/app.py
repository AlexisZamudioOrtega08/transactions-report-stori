import os

from config import config
from common.util import EMailer
from common.util import TxnHelper

from flask import Flask, render_template, request

app = Flask(__name__)
txns = (
    TxnHelper(path=os.path.dirname(os.path.abspath(__file__)) + "/data/txns.csv")
    .build()
    .json()
)
emailer = EMailer(config["email"])


@app.route("/statements", methods=["POST"])
def index():
    receiver = request.args.get("email")
    if receiver is None:
        return {"msg": "email not provided"}, 400
    rendered = render_template("email.html", data=txns)
    emailer.set_content(rendered)
    if emailer.send(receiver=receiver):
        return {"msg": "success"}, 201
    else:
        return {"msg": "error"}, 500


def error_404(error):
    return {"msg": "page not found"}, 404


def error_405(error):
    return {"msg": "method not allowed"}, 405


def error_500(error):
    return {"msg": "internal server error"}, 500


if __name__ == "__main__":
    app.config.from_object(config["development"])
    app.secret_key = config["development"].SECRET_KEY
    app.register_error_handler(404, error_404)
    app.register_error_handler(405, error_405)
    app.register_error_handler(500, error_500)
    app.run(host="0.0.0.0", port=5000)
