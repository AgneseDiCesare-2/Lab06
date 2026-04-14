import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff

        self._page = page
        self._page.title = "Template application using MVC and DAO"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self._anno = None
        self._brand = None
        self._retail = None

        self.btn_top = None
        self.btn_analizza = None
        self.txt_result = None
        self.txt_container = None

    def load_interface(self):
        # title
        self._title = ft.Text("Analizza Vendite", color="blue", size=24)
        self._page.controls.append(self._title)

        #ROW with some controls
        # dropdown field for the year
        self._anno = ft.Dropdown(
            label="anno",
            width=200,
           options=[ft.dropdown.Option("Nessun Filtro")]
        )
        self._controller.riempi_anni()

        # dropdown field for the brand
        self._brand = ft.Dropdown(
            label="brand",
            width=200,
            options=[ft.dropdown.Option("Nessun Filtro")],
            expand=True,
        )
        self._controller.riempi_brand()

        # dropdown field for the year
        self._retail = ft.Dropdown(
            label="retail",
            width=200,
            options=[ft.dropdown.Option("Nessun Filtro")],
            expand=True,
        )
        self._controller.riempi_retail()

        row1 = ft.Row([self._anno,  self._brand, self._retail],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)

        # button for the "hello" reply
        self.btn_top = ft.ElevatedButton(text="Top Vendite", on_click=self._controller.top_vendite)
        self.btn_analizza = ft.ElevatedButton(text="Analizza Vendite", on_click=self._controller.analizza_vendite)
        row2 = ft.Row([self.btn_top, self.btn_analizza],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)

        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
