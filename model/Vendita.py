from dataclasses import dataclass
import datetime
from decimal import Decimal

#i tipi dei dati si capiscono stampando il dao riga per riga
@dataclass
class Vendita:
    data: datetime.date
    brand: str
    retailer: int
    ricavo: Decimal
    prodotto: int

    def getAnno(self):
        return self.data.year

    def __str__(self):
        return f"Data: {self.data}; Ricavo: {self.ricavo}; Retailer: {self.retailer}; Product: {self.prodotto}"