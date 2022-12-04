from dbConnection.DbModels.Base import *


# Продукты
class Products(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String(300))
    count = Column(Integer)
    price = Column(Float)
    picturl = Column(String(500))

    def __repr__(self):
        return f'{self.id} {self.name} {self.count} {self.price} {self.picturl}'
