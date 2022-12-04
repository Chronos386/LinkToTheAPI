from apiDIr.resources.MainRes import MainRes


class ProductsRes(MainRes):
    def get(self):
        return self.dbClass.getAllProducts()
