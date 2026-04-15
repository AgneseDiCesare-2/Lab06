from database.DB_connect import DBConnect
from model.Retail import Retail
from model.Vendita import Vendita


class DAO:
    def __init__(self):
        pass

    @staticmethod
    def getAllAnni():
        cnx = DBConnect.get_connection()

        cursor = cnx.cursor()
        query = """ select distinct(year(Date)) as YEAR
                    from go_daily_sales"""  # restituisce una lista di anni
        cursor.execute(query)

        res = []
        for row in cursor:
            res.append(row[0]) #lista di anni --> NB: METTI ZERO SENNO SALVA UNA TUPLA E METTE ,

        cursor.close()
        cnx.close()
        return res  # lista di anni

    @staticmethod
    def getAllBrands():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor()
        query = """ select distinct(Product_brand) as brand
                    from go_products gp """
        cursor.execute(query)
        res = []

        for row in cursor:
            res.append(row[0]) #lista di brand

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    #vogliamo leggere l'oggetto
    def getAllRetails():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """ select *
                    from go_retailers gr  """
        cursor.execute(query)
        res = {}

        for row in cursor:
            res[row["Retailer_code"]]=(Retail(**row))  # dizionario di details (oggetti) con chiave l'id

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    #query che legge tutte le vendite, senza considerare i filtri --> filtro nel model
    def getAllVendite():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """ select gds.`Date`  as data, gp.Product_brand as brand, gds.Retailer_code as retailer, (gds.Unit_sale_price *gds.Quantity) as ricavo, gp.Product_number as prodotto 
                    from go_products gp, go_daily_sales gds
                    where gp.Product_number = gds.Product_number 
"""
        cursor.execute(query)
        res = [] #lista di vendite

        for row in cursor:
            res.append(Vendita(**row))

        cursor.close()
        cnx.close()
        return res
