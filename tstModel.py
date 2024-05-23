from database.DAO import DAO
from model.model import Model

mymodel = Model()

mymodel.creaGrafo("White", 2018)

for n in mymodel._grafo.nodes:
    print(n)

for u, v in mymodel._grafo.edges:
    print(f"{u} --- {v}")

print(DAO.getAllColors())
for c in DAO.getAllColors():
    print(f"{c}")


lista_tuple = [(1, 2), (3, 4), (5, 6), (4, 5), (5, 7), (7, 8)]
lista_nodi_archi = []
for u, v in lista_tuple:
    lista_nodi_archi.append(u)
    lista_nodi_archi.append(v)
print(lista_nodi_archi)

lista_nodi_ripetuti = []
for n in lista_nodi_archi:
    count = 0
    for nn in lista_nodi_archi:
        if n == nn:
            count += 1
    if count > 1 and n not in lista_nodi_ripetuti:
        lista_nodi_ripetuti.append(n)
print(lista_nodi_ripetuti)
