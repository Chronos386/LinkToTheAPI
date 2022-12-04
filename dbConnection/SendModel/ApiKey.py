import uuid


class ApiKey:
    def __init__(self):
        self.api_key = uuid.uuid4().hex[:30].upper()

    def setApiKey(self, api_key):
        self.api_key = api_key
