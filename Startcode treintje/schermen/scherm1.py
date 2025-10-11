# Opmerkingen in deze code zijn door mij geschreven ter verduidelijking van de werking. 
# De data komt uit de database en wordt netjes in een tabel weergegeven.

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QTableWidget, QTableWidgetItem
from PyQt6.QtCore import Qt

class Scherm1(QWidget):
    def __init__(self, main_window):
        super().__init__()

        # Verwijzing naar het hoofdvenster om later te kunnen navigeren
        self._main_window = main_window

        # Hoofdlayout voor dit scherm
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Titel bovenaan het scherm
        titel = QLabel("Attracties en wachttijden")
        titel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        titel.setStyleSheet("font-size: 22px; font-weight: bold; margin-bottom: 10px;")

        # Tabel om de wachttijden te tonen
        self._tabel = QTableWidget()
        self._tabel.setColumnCount(2)
        self._tabel.setHorizontalHeaderLabels(["Attractie", "Wachttijd (minuten)"])
        self._tabel.setStyleSheet("font-size: 16px;")

        # Knoppen onderaan
        self._btn_reserveren = QPushButton("Maak een reservering")
        self._btn_reserveren.clicked.connect(self._open_reserveren)

        self._btn_terug = QPushButton("Terug naar homepagina")
        self._btn_terug.clicked.connect(self._terug_naar_home)

        # Alles toevoegen aan layout
        layout.addWidget(titel)
        layout.addWidget(self._tabel)
        layout.addWidget(self._btn_reserveren)
        layout.addWidget(self._btn_terug)

        # Layout koppelen aan scherm
        self.setLayout(layout)

        # Vullen van de tabel met data uit de database
        self._vul_tabel_met_data()

    def _vul_tabel_met_data(self):
        """Haalt data uit de database en vult de tabel."""
        try:
            # Haalt de databaseconnectie op vanuit main_window
            locaties = self._main_window._database.get_locaties()

            # Aantal rijen instellen op basis van het aantal resultaten
            self._tabel.setRowCount(len(locaties))

            # Elke rij vullen met naam en wachttijd
            for i, (naam, wachttijd) in enumerate(locaties):
                self._tabel.setItem(i, 0, QTableWidgetItem(str(naam)))
                self._tabel.setItem(i, 1, QTableWidgetItem(str(wachttijd)))

        except Exception as e:
            print(f"Fout bij laden van wachttijden: {e}")

    def _open_reserveren(self):
        """Opent het scherm waar gebruiker een reservering kan maken."""
        self._main_window.toon_pagina(self._main_window._scherm2)

    def _terug_naar_home(self):
        """Gaat terug naar de homepagina."""
        self._main_window.toon_pagina(self._main_window._homepagina)