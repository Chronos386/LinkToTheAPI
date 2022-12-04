from flask import Flask
from flask_restful import Api
from apiDIr.resources.BasketRes import BasketRes
from apiDIr.resources.AccRes import AccRes
from apiDIr.resources.ProductRes import ProductRes
from apiDIr.resources.ProductsRes import ProductsRes


class ApiClass:
    def __init__(self):
        self.app = Flask(__name__)
        self.api = Api()

    def run(self):
        self.__initServe()
        self.app.run(debug=False, port=80, host="192.168.100.3")

    def __initServe(self):
        self.api.add_resource(ProductsRes, "/api/products/", "/api/")
        self.api.add_resource(ProductRes, "/api/product/<int:prod_id>/")
        self.api.add_resource(AccRes, "/api/login/")
        self.api.add_resource(BasketRes, "/api/basket/")
        self.api.init_app(app=self.app)
