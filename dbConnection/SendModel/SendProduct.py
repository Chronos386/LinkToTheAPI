from typing import List
from dbConnection.HelpClasses.HelpCharacteristic import HelpCharacteristic


class SendProduct:
    def __init__(self, product, help_characteristics: List[HelpCharacteristic]):
        self.id = product.id
        self.name = product.name
        self.count = product.count
        self.price = product.price
        self.picturl = product.picturl
        self.characteristics = help_characteristics
