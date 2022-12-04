from flask_restful import reqparse
from apiDIr.resources.MainRes import MainRes
from dbConnection.PostingModel.PostBasket import PostBasket


class BasketRes(MainRes):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument("api_key", type=str)
        req = parser.parse_args()
        resp = self.dbClass.getBasket(key=req.api_key)
        return resp

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("api_key", type=str)
        parser.add_argument("prod_id", type=int)
        req = parser.parse_args()
        basket = PostBasket(api_key=req.api_key, prod_id=req.prod_id)
        self.dbClass.addNewProdBasket(basket=basket)
        return {}, 200

    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument("api_key", type=str)
        parser.add_argument("prod_id", type=int)
        req = parser.parse_args()
        basket = PostBasket(api_key=req.api_key, prod_id=req.prod_id)
        return self.dbClass.delProdBasket(basket=basket)

    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument("api_key", type=str)
        parser.add_argument("prod_id", type=int)
        parser.add_argument("count", type=int)
        req = parser.parse_args()
        basket = PostBasket(api_key=req.api_key, prod_id=req.prod_id)
        return self.dbClass.changeCountProdBasket(basket=basket, count=req.count)
