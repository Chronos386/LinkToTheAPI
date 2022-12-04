from flask_restful import Resource
from dbConnection.DbClass import DBClass


class MainRes(Resource):
    def __init__(self):
        self.dbClass = DBClass()
