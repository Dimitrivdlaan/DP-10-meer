# Opmerkingen in deze code zijn door mij geschreven ter verduidelijking van de werking.

"""
Na het kiezen van een tijdslot kan de gebruiker zijn reis bevestigen.
"""

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QListWidget
from PyQt6.QtCore import Qt


class Scherm2(QWidget):
    """Scherm waar de gebruiker een tijdslot kan kiezen en zijn reis kan bevestigen."""

    def __init__(self, hoofd_venster):
        """Initialiseert het scherm en maakt de interface aan."""
        super().__init__()

        # Verwijzing naar het hoofdvenster om later te kunnen wisselen van scherm
        self._hoofd_venster = hoofd_venster

        # Layout voor dit scherm
        _layout = QVBoxLayout()
        _layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Titel bovenaan
        _titel = QLabel("Selecteer een beschikbaar tijdslot")
        _titel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        _titel.setStyleSheet("font-size: 18px; font-weight: bold; margin-bottom: 10px;")

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
        self._knop_bevestig = QPushButton("Bevestig mijn reis")
        self._knop_bevestig.setStyleSheet("background-color: lightgreen; height: 40px;")
        self._knop_bevestig.clicked.connect(self._bevestig_reis)

        # Alles toevoegen aan de layout
        _layout.addWidget(_titel)
        _layout.addWidget(self._lijst_tijden)
        _layout.addWidget(self._knop_bevestig)

        # Layout koppelen aan het scherm
        self.setLayout(_layout)

    def _bevestig_reis(self):
        """Haalt de gekozen tijd op, koppelt deze aan de attractie en gaat naar het bevestigingsscherm."""
        geselecteerde_items = self._lijst_tijden.selectedItems()

        if geselecteerde_items:
            tijd = geselecteerde_items[0].text()

            # Haal de geselecteerde attractie op via de getterfunctie van het hoofdvenster
            attractie = self._hoofd_venster.get_geselecteerde_attractie() or "Onbekende attractie"

            print(f"Tijdslot bevestigd: {tijd} voor attractie: {attractie}")

            # Tijd en attractie doorgeven aan scherm 3
            self._hoofd_venster._scherm3.stel_reservering_in(attractie, tijd)
            self._hoofd_venster.toon_pagina(self._hoofd_venster._scherm3)
        else:
            print("Geen tijdslot geselecteerd!")
