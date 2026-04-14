from model.Retail import Retail

class Vendita:
    def __init__(self, anno:str, brand:str, retailer:Retail, ricavo: float):
        self._anno=anno
        self._brand=brand
        self._retailer=retailer
        self._ricavo=ricavo

    def __str__(self):
        return f"{self._anno} {self._brand} {self._retailer} {self._ricavo}"

