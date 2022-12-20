from flask_restful import reqparse
from apiDIr.resources.MainRes import MainRes


class MyBasketRes(MainRes):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("api_key", type=str)
        req = parser.parse_args()
        resp = self.dbClass.getBasket(key=req.api_key)
        return resp
