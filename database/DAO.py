from database.DB_connect import DBConnect
from model.product import Product


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAllProducts():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select *
                    from go_products p"""

        cursor.execute(query)

        for row in cursor:
            result.append(Product(**row))

        cursor.close()
        conn.close()
        return result

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

    @staticmethod
    def getAllColors():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor()
        query = """select distinct p.Product_color
                from go_products p"""

        cursor.execute(query)

        result = cursor.fetchall()

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getPeso(year, color, num_product1, num_product2):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct ds2.`Date`
                from go_daily_sales ds1, go_daily_sales ds2, go_products p1, go_products p2
                where p1.Product_number = ds1.Product_number and p2.Product_number = ds2.Product_number 
                and ds1.`Date` = ds2.`Date` and ds1.Retailer_code = ds2.Retailer_code 
                and ds1.Product_number = %s and ds2.Product_number = %s
                and year(ds1.`Date`) = %s and year(ds2.`Date`) = %s
                and p1.Product_color = %s and p2.Product_color = %s
                group by ds2.Retailer_code , ds2.`Date` 
                order by ds2.`Date`"""

        cursor.execute(query, (num_product1, num_product2, year, year, color, color,))

        result = cursor.fetchall()

        cursor.close()
        conn.close()
        return len(result)
