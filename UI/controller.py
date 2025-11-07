import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.museo_selezionato = None
        self.epoca_selezionata = None

    # POPOLA DROPDOWN
    def popolaDropdownMusei(self):
        importaListaMusei = self._model.get_musei()
        listaMusei = [ft.dropdown.Option(m.nome) for m in importaListaMusei]

        #aggiungo l'opzione "Nessun filtro"
        listaMusei.insert(0, ft.dropdown.Option('Nessun filtro'))
        print('popolaDropdownMusei()')
        return listaMusei

    def popolaDropdownEpoca(self):
        importaListaEpoche = self._model.get_epoche()
        listaEpoche = [ft.dropdown.Option(e) for e in importaListaEpoche]

        #aggiungo l'opzione "Nessun filtro"
        listaEpoche.insert(0, ft.dropdown.Option('Nessun filtro'))
        print('popolaDropdownEpoca()')
        return listaEpoche
    # TODO

    # CALLBACKS DROPDOWN
    def on_change_Dropdown(self, e):
        if self.museo_selezionato is not None and self.epoca_selezionata is not None:
            self.mostraArtefatti(e)
            self._view.update()

    # TODO

    # AZIONE: MOSTRA ARTEFATTI
    def mostraArtefatti(self, e):
        museo = self._view._musei_Dropdown.value
        epoca = self._view._epoca_Dropdown.value
        self.museo_selezionato = museo
        self.epoca_selezionata = epoca

        print('View.btn_mostra_artefatti -> Controller.mostraArtefatti(e)')
        if museo is None and epoca is None:
            print('None, None : Valori Dropdown non validi')
            self._view.show_alert('Inserire valori negli appositi Dropdown')

        elif museo == 'Nessun filtro' and epoca is None:
            self._view.show_alert('Inserire valori negli appositi Dropdown')
            print('Nessun filtro, None : Valori Dropdown non validi')

        elif museo is None and epoca == 'Nessun filtro':
            self._view.show_alert('Inserire valori negli appositi Dropdown')
            print('Nome, Nessun filtro : Valori Dropdown non validi')

        elif museo == 'Nessun filtro' and epoca == 'Nessun filtro':
            lista_artefatti = self._model._artefatto_dao.get_artefatti()
            print('Lista artefatti ottenuta!')
            self._view._lst_artefatti.clean()

            # se nella lista c'è almeno un artefatto, appendo i controlli testuali alla lista della _view,
            # altrimenti la lista si svuota
            for artefatto_str_ in lista_artefatti:
                self._view._lst_artefatti.controls.append(ft.Text(artefatto_str_))
            self._view.update()

        else: # selezionati il museo e l'epoca
            lista_artefatti = self._model.get_artefatti_filtrati(museo, epoca)
            print('Lista artefatti ottenuta!')
            self._view._lst_artefatti.clean()

            # se nella lista c'è almeno un artefatto, appendo i controlli testuali alla lista della _view,
            # altrimenti la lista si svuota
            if lista_artefatti:
                for artefatto_str_ in lista_artefatti:
                    self._view._lst_artefatti.controls.append(ft.Text(artefatto_str_))
            else:
                print('Lista vuota')
                self._view.show_alert(f'Il Museo non possiede opere del periodo {epoca}')
            self._view.update()
        print()
    # TODO
