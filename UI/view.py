import flet as ft
from UI.alert import AlertManager

'''
    VIEW:
    - Rappresenta l'interfaccia utente
    - Riceve i dati dal MODELLO e li presenta senza modificarli
'''

class View:
    def __init__(self, page: ft.Page):
        # Page
        self.page = page
        self.page.title = "Lab07"
        self.page.horizontal_alignment = "center"
        self.page.theme_mode = ft.ThemeMode.DARK

        # Alert
        self.alert = AlertManager(page)

        # Controller
        self._controller = None

    def show_alert(self, messaggio):
        self.alert.show_alert(messaggio)

    def set_controller(self, controller):
        self.controller = controller

    def update(self):
        self.page.update()

    def load_interface(self):
        """ Crea e aggiunge gli elementi di UI alla pagina e la aggiorna. """
        # --- Sezione 1: Intestazione ---
        self.txt_titolo = ft.Text(value="Musei di Torino", size=38, weight=ft.FontWeight.BOLD)

        # --- Sezione 2: Filtraggio ---
        self._musei_Dropdown = ft.Dropdown(label="Museo", width = 400, on_change= self.controller.on_change_Dropdown)
        self._musei_Dropdown.options = self.controller.popolaDropdownMusei()

        self._epoca_Dropdown = ft.Dropdown(label="Epoca", width = 400, on_change=self.controller.on_change_Dropdown)
        self._epoca_Dropdown.options = self.controller.popolaDropdownEpoca()
        # TODO

        # Sezione 3: Artefatti
        btn_mostra_artefatti = ft.ElevatedButton(text='Mostra Artefatti',
                                                 width=200,
                                                 on_click=self.controller.mostraArtefatti)
        self._lst_artefatti = ft.ListView(expand=True, spacing=10, padding=20, auto_scroll=True)
        # TODO

        # --- Toggle Tema ---
        self.toggle_cambia_tema = ft.Switch(label="Tema scuro", value=True, on_change=self.cambia_tema)

        # --- Layout della pagina ---
        self.page.add(
            self.toggle_cambia_tema,

            # Sezione 1
            self.txt_titolo,
            ft.Divider(),

            # Sezione 2: Filtraggio
            ft.Row(controls=[self._musei_Dropdown, self._epoca_Dropdown], alignment= ft.MainAxisAlignment.CENTER),
            ft.Divider(),
            # TODO

            # Sezione 3: Artefatti
            ft.Row(controls=[btn_mostra_artefatti], alignment=ft.MainAxisAlignment.CENTER),
            self._lst_artefatti,
            # TODO
        )

        #self.page.scroll = "adaptive"
        self.page.update()

    def cambia_tema(self, e):
        """ Cambia tema scuro/chiaro """
        self.page.theme_mode = ft.ThemeMode.DARK if self.toggle_cambia_tema.value else ft.ThemeMode.LIGHT
        self.toggle_cambia_tema.label = "Tema scuro" if self.toggle_cambia_tema.value else "Tema chiaro"
        self.page.update()
