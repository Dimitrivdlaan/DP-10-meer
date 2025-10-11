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

        # Dubbelklik op een tijdslot werkt ook als bevestiging
        self._lijst_tijden.itemDoubleClicked.connect(self._bevestig_reis)

        # Knop om tijdslot te bevestigen
        self._btn_bevestig = QPushButton("Bevestig mijn reis!")
        self._btn_bevestig.clicked.connect(self._bevestig_reis)

        # Alles toevoegen aan de layout
        layout.addWidget(titel)
        layout.addWidget(self._lijst_tijden)
        layout.addWidget(self._btn_bevestig)

        # Layout koppelen aan het scherm
        self.setLayout(layout)

    def _bevestig_reis(self, item=None):
        """Functie om de gekozen tijd op te halen en naar het bevestigingsscherm te gaan."""
        # Ophalen van geselecteerde tijd
        if item:  # als het via dubbelklik is
            tijd = item.text()
        else:
            geselecteerde_items = self._lijst_tijden.selectedItems()
            if not geselecteerde_items:
                print("Geen tijdslot geselecteerd!")
                return
            tijd = geselecteerde_items[0].text()

        print(f"Tijdslot bevestigd: {tijd}")

        # In echte app zou dit in de database worden opgeslagen
        # self._main_window._database.voeg_reservering_toe('Treintje', tijd)

        # Ga door naar bevestigingsscherm (scherm3)
        self._main_window.toon_pagina(self._main_window._scherm3)

