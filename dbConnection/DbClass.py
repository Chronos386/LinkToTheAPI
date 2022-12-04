from sqlalchemy.orm import sessionmaker
from dbConnection.DbModels.Base import *
from dbConnection.GetSet.Getter import Getter
from dbConnection.GetSet.Setter import Setter
from dbConnection.SendModel.ApiKey import ApiKey


class DBClass:
    def __init__(self):
        self.engine = create_engine("postgresql+psycopg2://postgres:Chronos386@localhost/web_db")
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()
        self.getter = Getter(self.session)
        self.setter = Setter(self.session)

    def getCountProd(self):
        return self.getter.getCountProd()

    def getCountChar(self):
        return self.getter.getCountChar()

    def getCountRelat_prod_char(self):
        return self.getter.getCountRelat_prod_char()

    def getCountAccount(self):
        return self.getter.getCountAccount()

    def getCountGroceryBasket(self):
        return self.getter.getCountGroceryBasket()

    def getCountAccDevice(self):
        return self.getter.getCountAccDevice()

    def getAllProducts(self):
        return self.getter.getAllProducts()

    def getProductById(self, prod_id):
        return self.getter.getProductById(prod_id=prod_id)

    def login(self, account):
        acc = self.getter.getAccByPsw(account.login, account.password)
        if acc is None:
            return None
        else:
            key = ApiKey()
            return self.setter.setNewApiKey(key=key, acc_id=acc.id)

    def logOut(self, api_key):
        self.setter.delApiKey(api_key)

    def addNewProdBasket(self, basket):
        self.setter.addNewProdBasket(api_key=basket.api_key, prod_id=basket.prod_id)

    def delProdBasket(self, basket):
        self.setter.delProdBasket(api_key=basket.api_key, prod_id=basket.prod_id)
        return self.getBasket(key=basket.api_key)

    def changeCountProdBasket(self, basket, count):
        self.setter.updProdCountBasket(api_key=basket.api_key, prod_id=basket.prod_id, count=count)
        return self.getBasket(key=basket.api_key)

    def getBasket(self, key):
        return self.getter.getBasket(api_key=key)
