from apiDIr.resources.MainRes import MainRes


class ProductRes(MainRes):
    def get(self, prod_id):
        resp = self.dbClass.getProductById(prod_id=prod_id)
        return resp
