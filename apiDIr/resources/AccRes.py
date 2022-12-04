from flask_restful import reqparse
from apiDIr.resources.MainRes import MainRes
from dbConnection.SendModel.ApiKey import ApiKey
from dbConnection.PostingModel.PostAccount import PostAccount


class AccRes(MainRes):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("login", type=str)
        parser.add_argument("password", type=str)
        req = parser.parse_args()
        acc = PostAccount(log=req.login, psw=req.password)
        resp = self.dbClass.login(account=acc)
        if resp is None:
            return {}, 401
        else:
            return resp

    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument("api_key", type=str)
        req = parser.parse_args()
        api_key = ApiKey()
        api_key.setApiKey(api_key=req.api_key)
        self.dbClass.logOut(api_key=api_key)
        return {}, 200
