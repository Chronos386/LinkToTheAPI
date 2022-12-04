import json
from sqlalchemy.ext.declarative import DeclarativeMeta

from dbConnection.SendModel.SendBasket import SendBasket
from dbConnection.SendModel.SendProduct import SendProduct


class AlchemyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            fields = {}
            for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                data = obj.__getattribute__(field)
                if field != "registry":
                    try:
                        json.dumps(data)
                        fields[field] = data
                    except TypeError:
                        fields[field] = None
            return fields
        return json.JSONEncoder.default(self, obj)


class PersonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, SendProduct):
            return obj.__dict__
        return json.JSONEncoder.default(self, obj)


class SendBasketEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, SendBasket):
            return obj.__dict__
        return json.JSONEncoder.default(self, obj)
