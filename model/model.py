import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._allProducts = DAO.getAllProducts()
        self._products = []
        self._productMap = {}

        self._grafo = nx.Graph()

    def creaGrafo(self, color, year):
        self._grafo.clear()

        self._products = DAO.getProducts(color)
        for p in self._products:
            self._productMap[p.Product_number] = p

        self._grafo.add_nodes_from(self._products)
        self.addEdges(color, year)

    def addEdges(self, color, year):
        self._grafo.clear_edges()

        for p1 in self._products:
            for p2 in self._products:
                if p2.Product_number != p1.Product_number:
                    peso = DAO.getPeso(year, color, p1.Product_number, p2.Product_number)
                    if peso > 0:
                        self._grafo.add_edge(p1, p2, weight=peso)

    def getArchiPesoMaggiore(self):
        edgesTuple = []
        for u, v in self._grafo.edges:
            edgesTuple.append((u, v, self._grafo[u][v]["weight"]))
        edgesTuple.sort(key=lambda x: x[2], reverse=True)
        return edgesTuple[:3]

    def getNodiRipetuti(self):
        edgesTuple = self.getArchiPesoMaggiore()
        nodi_archiPesoMaggiore = []
        for e in edgesTuple:
            nodi_archiPesoMaggiore.append(e[0])
            nodi_archiPesoMaggiore.append(e[1])
        nodi_ripetuti = []
        for n in nodi_archiPesoMaggiore:
            count = 0
            for nn in nodi_archiPesoMaggiore:
                if n == nn:
                    count += 1
            if count > 1 and n.Product_number not in nodi_ripetuti:
                nodi_ripetuti.append(n.Product_number)
        return nodi_ripetuti

    def getColorProducts(self):
        colorList = []
        for p in self._allProducts:
            if p.Product_color not in colorList:
                colorList.append(p.Product_color)
        return colorList

    def getNumNodes(self):
        return len(self._grafo.nodes)

    def getNumEdges(self):
        return len(self._grafo.edges)
