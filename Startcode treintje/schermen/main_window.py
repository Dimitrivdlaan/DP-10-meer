# Opmerkingen in deze code zijn door mij geschreven ter verduidelijking van de werking. 

from PyQt6.QtWidgets import QMainWindow, QStackedWidget, QWidget
from .startscherm import Startscherm                    # Startscherm staat buiten de map /schermen
from .schermen.homepagina import Homepagina             # Homepagina zit in map /schermen
from .schermen.scherm1 import Scherm1                   # Eerste functionele scherm
from .schermen.scherm2 import Scherm2                   # Tweede functionele scherm
from .schermen.scherm3 import Scherm3                   # Derde functionele scherm
from .db_connect import DatabaseConnectie               # Databaseklasse importeren

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # aanpassing: titel en vensterinstellingen
        self.setWindowTitle("Lake Side Mania - GUI")
        self.setGeometry(100, 100, 1024, 768)

        # aanpassing: maak databaseverbinding als privé-attribuut
        self._database = DatabaseConnectie()
        self._database.open_verbinding()

        # aanpassing: gebruik een QStackedWidget om tussen schermen te wisselen
        self._stack = QStackedWidget()
        self.setCentralWidget(self._stack)

        # aanpassing: schermen als privé-attributen (encapsulatie toegepast)
        self._startscherm = Startscherm(self)
        self._homepagina = Homepagina(self)
        self._scherm1 = Scherm1(self)
        self._scherm2 = Scherm2(self)
        self._scherm3 = Scherm3(self)

        # aanpassing: voeg schermen toe aan de stack
        self._stack.addWidget(self._startscherm)
        self._stack.addWidget(self._homepagina)
        self._stack.addWidget(self._scherm1)
        self._stack.addWidget(self._scherm2)
        self._stack.addWidget(self._scherm3)

        # aanpassing: standaard startscherm tonen bij het opstarten
        self._stack.setCurrentWidget(self._startscherm)

    # aanpassing: methode om van scherm te wisselen
    def toon_pagina(self, widget: QWidget):
        """Toont het opgegeven scherm in de GUI."""
        self._stack.setCurrentWidget(widget)

    # aanpassing: geef toegang tot database op gecontroleerde manier
    def get_database(self):
        """Geeft toegang tot de databaseverbinding (gebruikt in andere schermen)."""
        return self._database

    # aanpassing: sluit database netjes af bij het sluiten van de app
    def closeEvent(self, event):
        """Wordt uitgevoerd bij het afsluiten van de applicatie."""
        self._database.sluit_verbinding()
        event.accept()
