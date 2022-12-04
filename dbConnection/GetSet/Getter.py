import json
from flask import Response
from dbConnection.DbModels.Account import *
from dbConnection.DbModels.Product import *
from dbConnection.DbModels.Grocery_basket import *
from dbConnection.DbModels.Characteristics import *
from dbConnection.DbModels.Relat_prod_char import *
from dbConnection.DbModels.AccDevice import AccDevice
from dbConnection.SendModel.SendBasket import SendBasket
from dbConnection.SendModel.SendProduct import SendProduct
from dbConnection.HelpClasses.HelpCharacteristic import HelpCharacteristic
from dbConnection.HelpClasses.AlchemyEncoder import AlchemyEncoder, PersonEncoder, SendBasketEncoder


class Getter:
    def __init__(self, session):
        self.session = session

    def getCountProd(self):
        return self.session.query(Products).count()

    def getCountChar(self):
        return self.session.query(Characteristics).count()

    def getCountRelat_prod_char(self):
        return self.session.query(Relat_prod_char).count()

    def getCountAccount(self):
        return self.session.query(Account).count()

    def getCountGroceryBasket(self):
        return self.session.query(Grocery_basket).count()

    def getCountAccDevice(self):
        return self.session.query(AccDevice).count()

    def getAllProducts(self):
        allProducts = self.session.query(Products).all()
        dataTable = json.dumps(allProducts, cls=AlchemyEncoder, ensure_ascii=False, sort_keys=True)
        return Response(dataTable, mimetype='application/json')

    def getProductById(self, prod_id):
        productDB = self.session.query(Products).filter_by(id=prod_id).first()
        all_char_ids = self.session.query(Relat_prod_char).filter_by(prod_id=prod_id).all()
        characteristics = []
        for char_id in all_char_ids:
            characteristic = self.session.query(Characteristics).filter_by(id=char_id.char_id).first()
            characteristics.append(HelpCharacteristic(characteristics=characteristic))
        product = SendProduct(product=productDB, help_characteristics=characteristics)
        dataTable = json.dumps(product, cls=PersonEncoder, default=lambda o: o.__dict__, ensure_ascii=False,
                               sort_keys=True)
        return Response(dataTable, mimetype='application/json')

    def getAccByPsw(self, log, psw):
        accounts = self.session.query(Account).filter_by(login=log, password=psw).all()
        if len(accounts) != 0:
            return accounts[0]
        else:
            return None

    def getBasket(self, api_key):
        user_acc = self.session.query(AccDevice).filter_by(api_key=api_key).first()
        acc_basket = self.session.query(Grocery_basket).filter_by(acc_id=user_acc.acc_id).all()
        basket_arr = []
        for prod_id in acc_basket:
            prod = self.session.query(Products).filter_by(id=prod_id.prod_id).first()
            basket_arr.append(SendBasket(name=prod.name, pict_url=prod.picturl, price=prod.price, count=prod_id.count))
        dataTable = json.dumps(basket_arr, cls=SendBasketEncoder, ensure_ascii=False, sort_keys=True)
        return Response(dataTable, mimetype='application/json')
