# Opmerkingen in deze code zijn door mij geschreven ter verduidelijking van de werking. 
# Na het kiezen van een tijdslot kan de gebruiker zijn reis bevestigen.

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QListWidget
from PyQt6.QtCore import Qt

class Scherm2(QWidget):
    def __init__(self, main_window):
        super().__init__()

        # Verwijzing naar het hoofdvenster om later te kunnen wisselen van scherm
        self._main_window = main_window

        # Layout voor dit scherm
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Titel bovenaan
        titel = QLabel("Selecteer een beschikbaar tijdslot")
        titel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        titel.setStyleSheet("font-size: 18px; font-weight: bold; margin-bottom: 10px;")

        # Lijst met beschikbare tijden
        self._lijst_tijden = QListWidget()
        self._lijst_tijden.addItems([
            "12:00 - 12:45",
            "12:45 - 13:30",
            "13:30 - 14:15",
            "14:15 - 15:00",
            "15:00 - 15:45",
            "15:45 - 16:30",
            "16:30 - 17:15"
        ])

        # Knop om tijdslot te bevestigen
        self._btn_bevestig = QPushButton("Bevestig mijn reis!")
        self._btn_bevestig.clicked.connect(self._bevestig_reis)

        # Alles toevoegen aan de layout
        layout.addWidget(titel)
        layout.addWidget(self._lijst_tijden)
        layout.addWidget(self._btn_bevestig)

        # Layout koppelen aan het scherm
        self.setLayout(layout)

    def _bevestig_reis(self):
        """Functie om de gekozen tijd op te halen en naar het bevestigingsscherm te gaan."""
        # Ophalen van geselecteerde tijd
        geselecteerde_items = self._lijst_tijden.selectedItems()

        # Controle of er iets is gekozen
        if geselecteerde_items:
            tijd = geselecteerde_items[0].text()  # haalt de tekst van het geselecteerde item op
            print(f"Tijdslot bevestigd: {tijd}")

            # Tijd doorgeven aan scherm3 voordat het scherm wordt geopend
            self._main_window._scherm3.stel_tijd_in(tijd)

            # Ga door naar bevestigingsscherm (scherm3)
            self._main_window.toon_pagina(self._main_window._scherm3)
        else:
            print("Geen tijdslot geselecteerd!")

