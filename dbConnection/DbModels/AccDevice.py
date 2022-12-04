from dbConnection.DbModels.Base import *


# API ключи
class AccDevice(Base):
    __tablename__ = 'acc_device'
    id = Column(Integer, primary_key=True)
    api_key = Column(String(30))
    acc_id = Column(Integer, ForeignKey('account.id'))

    def __repr__(self):
        return f'{self.id} {self.api_key} {self.acc_id}'
