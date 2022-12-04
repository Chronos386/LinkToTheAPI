from dbConnection.DbModels.Base import *


# Характеристики продуктов
class Characteristics(Base):
    __tablename__ = 'characteristics'
    id = Column(Integer, primary_key=True)
    title = Column(String(300))
    body = Column(String(300))

    def __repr__(self):
        return f'{self.id} {self.title} {self.body}'
