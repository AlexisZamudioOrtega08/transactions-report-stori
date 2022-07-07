from db import db

from config import config

from flask import Flask
from flask_restful import Api

from resources.user import User
from resources.report import Report
from resources.transaction import Transaction

def create_app():
    app = Flask(__name__, template_folder="templates")
    api = Api(app)
    api_prefix = config["development"].API_PREFIX


    @app.before_first_request
    def create_tables():
        db.create_all()


    api.add_resource(
        Transaction, "{}/transactions".format(api_prefix), methods=["GET", "POST"]
    )
    api.add_resource(Report, "{}/reports".format(api_prefix), methods=["POST"])
    api.add_resource(User, "{}/users".format(api_prefix), methods=["GET", "POST"])


    def error_404(error):
        return {"msg": "page not found"}, 404


    def error_405(error):
        return {"msg": "method not allowed"}, 405


    def error_500(error):
        print(error)
        return {"msg": "internal server error"}, 500

    app.config.from_object(config["development"])
    app.secret_key = config["development"].SECRET_KEY
    db.init_app(app)
    app.register_error_handler(404, error_404)
    app.register_error_handler(405, error_405)
    app.register_error_handler(500, error_500)
    
    return app