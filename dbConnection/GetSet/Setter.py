import json
from flask import Response
from dbConnection.DbModels.AccDevice import AccDevice
from dbConnection.DbModels.Grocery_basket import Grocery_basket
from dbConnection.HelpClasses.AlchemyEncoder import AlchemyEncoder


class Setter:
    def __init__(self, session):
        self.session = session

    def __findFirstFreeID(self, table_db):
        stmt = self.session.query(table_db).order_by(table_db.id.asc()).all()
        count = self.session.query(table_db).count()
        mass = []
        for i in range(1, count + 1):
            if i != stmt[i - 1].id:
                mass.append(i)
        if len(mass) != 0:
            count = mass[0]
        else:
            count += 1
        return count

    def setNewApiKey(self, key, acc_id):
        new_id = self.__findFirstFreeID(AccDevice)
        user_new = AccDevice(id=new_id, api_key=key.api_key, acc_id=acc_id)
        self.session.add(user_new)
        self.session.commit()
        dataTable = json.dumps(key, cls=AlchemyEncoder, default=lambda o: o.__dict__, ensure_ascii=False,
                               sort_keys=True)
        return Response(dataTable, mimetype='application/json')

    def delApiKey(self, key):
        self.session.query(AccDevice).filter_by(api_key=key.api_key).delete(synchronize_session=False)
        self.session.commit()

    def addNewProdBasket(self, api_key, prod_id):
        new_id = self.__findFirstFreeID(Grocery_basket)
        user = self.session.query(AccDevice).filter_by(api_key=api_key).first()
        acc_basket = self.session.query(Grocery_basket).filter_by(acc_id=user.acc_id, prod_id=prod_id).all()
        if len(acc_basket) == 0:
            new_basket = Grocery_basket(id=new_id, prod_id=prod_id, acc_id=user.acc_id, count=1)
            self.session.add(new_basket)
        else:
            basket_prod = self.session.query(Grocery_basket).filter_by(acc_id=user.acc_id, prod_id=prod_id).first()
            basket_prod.count += 1
        self.session.commit()

    def delProdBasket(self, api_key, prod_id):
        user = self.session.query(AccDevice).filter_by(api_key=api_key).first()
        self.session.query(Grocery_basket).filter_by(acc_id=user.acc_id, prod_id=prod_id)\
            .delete(synchronize_session=False)
        self.session.commit()

    def updProdCountBasket(self, api_key, prod_id, count):
        user = self.session.query(AccDevice).filter_by(api_key=api_key).first()
        prod = self.session.query(Grocery_basket).filter_by(acc_id=user.acc_id, prod_id=prod_id).first()
        prod.count = count
        self.session.commit()
