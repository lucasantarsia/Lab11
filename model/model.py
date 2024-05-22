import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._products = []
        self._productMap = {}

        self._grafo = nx.Graph()

    def creaGrafo(self, color):
        for p in self._products:
            self._productMap[p.Product_number] = p

        self._products = DAO.getProducts(color)
        self._grafo.add_nodes_from(self._products)
        self.addEdges()

    def addEdges(self):
        pass

    def getColorProducts(self):
        colorList = []
        for p in self._products:
            if p.Product_color not in colorList:
                colorList.append(p.Product_color)
        return colorList
