from dbConnection.DbModels.Base import *


# Соотношение характеристик и продуктов
class Relat_prod_char(Base):
    __tablename__ = 'relat_prod_char'
    id = Column(Integer, primary_key=True)
    prod_id = Column(Integer, ForeignKey('products.id'))
    char_id = Column(Integer, ForeignKey('characteristics.id'))

    def __repr__(self):
        return f'{self.id} {self.prod_id} {self.char_id}'
