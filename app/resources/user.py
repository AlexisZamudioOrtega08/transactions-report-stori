from flask import request
from flask_restful import Resource
from flask_pydantic import validate
from models.user import User as UserModel
from schemas.user import User as UserSchema


class User(Resource):
    def get(self):
        try:
            id = request.args.get("id")
            if id:
                if id.isdigit():
                    user = UserModel.find_by_id(id)
                    if user:
                        return {"user": [user.json()]}, 200
                    return {"msg": "user not found"}, 404
                else: 
                    return {"msg": "id must be an integer"}, 400
            else:
                users = UserModel.find_all()
                if users:
                    return {"users": [user.json() for user in users]}, 200
                return {"msg": "no users found"}, 404
        except Exception as e:
            print(e)
            return {"msg": "internal server error"}, 500

    @validate()
    def post(self, body: UserSchema):
        try:
            if UserModel.find_by_email(body.email):
                return {"msg": "user already exists"}, 400
            user = UserModel(**body.dict())
            user.save_to_db()
        except Exception as e:
            if user:
                user.rollback()
            return {"msg": "internal server error"}, 500
        else:
            user.commit()
            return {"msg": [user.json()]}, 201
