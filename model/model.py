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