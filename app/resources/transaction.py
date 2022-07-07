from flask import request
from models.txn import Txn as TxnModel
from models.user import User as UserModel
from schemas.txn import Txn as TxnSchema
from flask_restful import Resource
from flask_pydantic import validate


class Transaction(Resource):
    def get(self):
        try:
            user_id = request.args.get("user_id")
            if user_id:
                txns = TxnModel.find_by_user_id(user_id)
                if txns:
                    return {"txns": [txn.json() for txn in txns]}, 200
                else:
                    return {"msg": "No transactions found"}, 404
            else:
                txns = TxnModel.find_all()
                if txns:
                    return {"txns": [txn.json() for txn in txns]}, 200
                else:
                    return {"msg": "No transactions found"}, 404
        except Exception as e:
            return {"msg": str(e)}, 500

    @validate()
    def post(self, body: TxnSchema):
        try:
            user = UserModel.find_by_id(body.user_id)
            if not user:
                return {"msg": "User not found"}, 404
            txn = TxnModel(body.user_id, body.txn, body.amount)
            txn.save_to_db()
        except Exception as e:
            if txn:
                txn.rollback()
            return {"msg": str(e)}, 500
        else:
            if txn:
                txn.commit()
                return {"txn": txn.json()}, 201
