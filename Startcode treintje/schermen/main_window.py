# Opmerkingen in deze code zijn door mij geschreven ter verduidelijking van de werking.

"""
Dit bestand definieert de klasse HoofdVenster.
Deze klasse beheert de navigatie en databaseverbinding van de applicatie Lake Side Mania.
"""

from PyQt6.QtWidgets import QMainWindow, QStackedWidget, QWidget
from schermen.startscherm import Startscherm
from schermen.homepagina import HomePagina
from schermen.scherm1 import Scherm1
from schermen.scherm2 import Scherm2
from schermen.scherm3 import Scherm3
from schermen.scherm4 import Scherm4
from db_connect import DatabaseConnectie


class HoofdVenster(QMainWindow):
    """Hoofdvenster van de Lake Side Mania GUI-toepassing."""

    def __init__(self):
        """Initialiseert het hoofdvenster, de schermen en de databaseverbinding."""
        super().__init__()

        # Titel en vensterinstellingen
        self.setWindowTitle("Lake Side Mania - GUI")
        self.setGeometry(100, 100, 1024, 768)

        # Maak databaseverbinding aan (protected attribuut)
        self._database = DatabaseConnectie()
        self._database.open_verbinding()

        # Variabele om de geselecteerde attractie tijdelijk op te slaan
        self._geselecteerde_attractie = None

        # Gebruik een QStackedWidget om tussen schermen te wisselen
        self._stack = QStackedWidget()
        self.setCentralWidget(self._stack)

        # Initialiseer en encapsuleer de schermen
        self._startscherm = Startscherm(self)
        self._homepagina = HomePagina(self)
        self._scherm1 = Scherm1(self)
        self._scherm2 = Scherm2(self)
        self._scherm3 = Scherm3(self)
        self._scherm4 = Scherm4(self)

        # Voeg schermen toe aan de stack
        self._stack.addWidget(self._startscherm)
        self._stack.addWidget(self._homepagina)
        self._stack.addWidget(self._scherm1)
        self._stack.addWidget(self._scherm2)
        self._stack.addWidget(self._scherm3)
        self._stack.addWidget(self._scherm4)

        # Toon het startscherm bij het opstarten
        self._stack.setCurrentWidget(self._startscherm)

    def toon_pagina(self, widget: QWidget):
        """Toont het opgegeven scherm in het hoofdvenster."""
        self._stack.setCurrentWidget(widget)

    def get_database(self):
        """Geeft gecontroleerde toegang tot de databaseverbinding."""
        return self._database

    def get_scherm1(self):
        """Geeft gecontroleerde toegang tot scherm 1 vanuit andere schermen."""
        return self._scherm1

    def set_geselecteerde_attractie(self, attractie_naam: str):
        """Slaat de naam van de geselecteerde attractie tijdelijk op."""
        self._geselecteerde_attractie = attractie_naam
        print(f"Geselecteerde attractie ingesteld op: {attractie_naam}")

    def get_geselecteerde_attractie(self):
        """Geeft de momenteel geselecteerde attractie terug."""
        return self._geselecteerde_attractie

    def closeEvent(self, event):
        """Wordt uitgevoerd bij het afsluiten van de applicatie."""
        self._database.sluit_verbinding()
        event.accept()
