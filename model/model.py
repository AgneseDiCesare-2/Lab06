from database.DAO import DAO


class Model:
    def __init__(self):
        pass

    def getAllAnni(self):
        return DAO.getAllAnni() #lista di anni

    def getAllBrands(self):
        return DAO.getAllBrands() #lista di brands

    def getAllRetails(self):
        return DAO.getAllRetails() #dizionario


    def getAllVendite(self, anno, brand, retail):
        vendite = DAO.getAllVendite() #lista con tutte le vendite
        vendite_filtrate=[] #voglio i risultati filtrati

        for vendita in vendite:
            anno_vendita=vendita.getAnno()
            if (
                    (anno is None or anno_vendita == anno) and
                    (brand is None or vendita.brand == brand) and
                    (retail is None or str(vendita.retailer) == str(retail.Retailer_code))
            ):
                vendite_filtrate.append(vendita)

        vendite_filtrate.sort(key=lambda s: s.ricavo, reverse=True)  # top vendite prima
        return vendite_filtrate

