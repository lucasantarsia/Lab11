from database.DAO import DAO
from model.model import Model

mymodel = Model()

mymodel.creaGrafo("Blue")

for n in mymodel._grafo.nodes:
    print(n)
