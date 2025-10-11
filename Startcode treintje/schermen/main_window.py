# Opmerkingen in deze code zijn door mij geschreven ter verduidelijking van de werking. 

from PyQt6.QtWidgets import QMainWindow, QStackedWidget, QWidget
from schermen.startscherm import Startscherm                   # Startscherm zit in de map /schermen
from schermen.homepagina import Homepagina                     # Homepagina uit map /schermen
from schermen.scherm1 import Scherm1                           # Eerste functionele scherm
from schermen.scherm2 import Scherm2                           # Tweede functionele scherm
from schermen.scherm3 import Scherm3                           # Derde functionele scherm
from schermen.scherm4 import Scherm4                           # Vierde functionele scherm
from db_connect import DatabaseConnectie                       # Databaseklasse importeren


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # titel en vensterinstellingen
        self.setWindowTitle("Lake Side Mania - GUI")
        self.setGeometry(100, 100, 1024, 768)

        # maak databaseverbinding als privé-attribuut
        self._database = DatabaseConnectie()
        self._database.open_verbinding()

        # nieuw attribuut om de huidige attractie op te slaan
        self._geselecteerde_attractie = None

        # gebruik een QStackedWidget om tussen schermen te wisselen
        self._stack = QStackedWidget()
        self.setCentralWidget(self._stack)

        # schermen als privé-attributen (encapsulatie toegepast)
        self._startscherm = Startscherm(self)
        self._homepagina = Homepagina(self)
        self._scherm1 = Scherm1(self)
        self._scherm2 = Scherm2(self)
        self._scherm3 = Scherm3(self)
        self._scherm4 = Scherm4(self)

        # schermen toevoegen aan de stack
        self._stack.addWidget(self._startscherm)
        self._stack.addWidget(self._homepagina)
        self._stack.addWidget(self._scherm1)
        self._stack.addWidget(self._scherm2)
        self._stack.addWidget(self._scherm3)
        self._stack.addWidget(self._scherm4)

        # standaard startscherm tonen bij het opstarten
        self._stack.setCurrentWidget(self._startscherm)

    def toon_pagina(self, widget: QWidget):
        """Toont het opgegeven scherm in de GUI."""
        self._stack.setCurrentWidget(widget)

    def get_database(self):
        """Geeft gecontroleerde toegang tot de databaseverbinding."""
        return self._database

    def get_scherm1(self):
        """Geeft gecontroleerde toegang tot scherm1 vanuit andere schermen."""
        return self._scherm1

    # nieuwe functies om attractienaam te beheren
    def set_geselecteerde_attractie(self, attractie_naam: str):
        """Slaat de gekozen attractienaam tijdelijk op."""
        self._geselecteerde_attractie = attractie_naam
        print(f"Geselecteerde attractie ingesteld op: {attractie_naam}")

    def get_geselecteerde_attractie(self):
        """Geeft de momenteel gekozen attractie terug."""
        return self._geselecteerde_attractie

    def closeEvent(self, event):
        """Wordt uitgevoerd bij het afsluiten van de applicatie."""
        self._database.sluit_verbinding()
        event.accept()

