from dataclasses import dataclass

from model.Retail import Retail
@dataclass
class Vendita:
        anno:str
        brand: str
        retailer: Retail
        ricavo: float

def __str__(self):
    return f"Anno: {self._anno}, Brand: {self._brand}, Retailer: {self._retailer}, Ricavo: {self._ricavo}"

