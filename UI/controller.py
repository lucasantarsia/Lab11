import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._listYear = [2015, 2016, 2017, 2018]
        self._listColor = self._model.getColorProducts()

    def fillDD(self):
        # riempio ddyear
        for y in self._listYear:
            self._view._ddyear.options.append(ft.dropdown.Option(str(y)))

        # riempio ddcolor
        for c in self._listColor:
            self._view._ddcolor.options.append(ft.dropdown.Option(str(c)))

        self._view.update_page()


    def handle_graph(self, e):
        self._model.creaGrafo(self._view._ddcolor.value, int(self._view._ddyear.value))
        self._view.txtOut.controls.clear()
        self._view.txtOut.controls.append(ft.Text(f"Numero di vertici: {self._model.getNumNodes()}"))
        self._view.txtOut.controls.append(ft.Text(f"Numero di archi: {self._model.getNumEdges()}"))

        archiPesoMaggiore = self._model.getArchiPesoMaggiore()
        for u, v, peso in archiPesoMaggiore:
            self._view.txtOut.controls.append(ft.Text(f"Arco da {u} a {v}, peso={peso}"))
        self._view.update_page()

        nodiRipetuti = self._model.getNodiRipetuti()
        if nodiRipetuti == []:
            self._view.txtOut.controls.append(ft.Text("Non ci sono nodi ripetuti"))
            self._view.update_page()
        else:
            self._view.txtOut.controls.append(ft.Text(f"I nodi ripetuti sono: {nodiRipetuti}"))
            self._view.update_page()


    def fillDDProduct(self):
        pass


    def handle_search(self, e):
        pass
