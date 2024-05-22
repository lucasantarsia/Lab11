from database.DB_connect import DBConnect
from model.product import Product


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getProducts(color):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select *
                from go_products p
                where p.Product_color = %s"""

        cursor.execute(query, (color,))

        for row in cursor:
            result.append(Product(**row))

        cursor.close()
        conn.close()
        return result
