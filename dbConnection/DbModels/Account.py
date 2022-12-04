from dbConnection.DbModels.Base import *


# Аккаунт
class Account(Base):
    __tablename__ = 'account'
    id = Column(Integer, primary_key=True)
    login = Column(String(300))
    password = Column(String(300))

    def __repr__(self):
        return f'{self.id} {self.login} {self.password}'
