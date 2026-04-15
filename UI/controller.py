import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI

        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._anno=None
        self._brand=None
        self._retail=None


    def top_vendite(self, e):
        self._view.txt_result.controls.clear()
        tutte_vendite=self._model.getAllVendite(self._anno, self._brand, self._retail)

        if len(tutte_vendite)==0:
            self._view.txt_result.controls.append(ft.Text("Nessuna Vendita per i filtri inseriti"))
            self._view.update_page()
            return

        if len(tutte_vendite)<=5:
            vendite=tutte_vendite
        else:
            vendite=tutte_vendite[:5]

        for vendita in vendite:
            self._view.txt_result.controls.append(ft.Text(vendita))
        self._view.update_page()

    def analizza_vendite(self, e):
        pass

    def riempi_anni(self): #NB: QUI NON CI VA e!
        self._view._anno.options.append(ft.dropdown.Option(key="Nessun Filtro", data=None, on_click=self._choiceAnno))
        for anno in self._model.getAllAnni():
            self._view._anno.options.append(
                ft.dropdown.Option(key=anno, data=anno, on_click=self._choiceAnno))
            pass

    def _choiceAnno(self, e):
        self._anno = e.control.data #evento (anno) selezionato nel dropdown

    def riempi_brand(self):
        self._view._brand.options.append(ft.dropdown.Option(key="Nessun Filtro", data=None, on_click=self._choice_brand))
        for brand in self._model.getAllBrands():
            self._view._brand.options.append(
                ft.dropdown.Option(key=brand, data=brand, on_click=self._choice_brand))
            pass

    def _choice_brand(self, e):
        self._brand = e.control.data #evento (anno) selezionato nel dropdown


    def riempi_retail(self):
        self._view._retail.options.append(ft.dropdown.Option(key="Nessun Filtro", data=None, on_click=self._choice_retail))
        retails=self._model.getAllRetails().values()
        for retail in retails: #itero sugli oggetti Retails (valori, non chiavi!)
            self._view._retail.options.append(ft.dropdown.Option(key=retail.Retailer_name, data=retail, on_click=self._choice_retail))

    def _choice_retail(self, e):
        self._retail=e.control.data #oggetto retail