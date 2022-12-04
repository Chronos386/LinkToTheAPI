from dbConnection.DbModels.Base import *


# Продуктовая корзина
class Grocery_basket(Base):
    __tablename__ = 'grocery_basket'
    id = Column(Integer, primary_key=True)
    prod_id = Column(Integer, ForeignKey('products.id'))
    acc_id = Column(Integer, ForeignKey('account.id'))
    count = Column(Integer)

    def __repr__(self):
        return f'{self.id} {self.prod_id} {self.acc_id} {self.count}'
