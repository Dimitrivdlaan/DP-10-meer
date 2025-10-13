# Opmerkingen in deze code zijn door mij geschreven ter verduidelijking van de werking.

"""
Dit scherm toont de attracties en hun wachttijden,
en laat de gebruiker een attractie kiezen om te reserveren.
"""

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QTableWidget, QTableWidgetItem
from PyQt6.QtCore import Qt


class Scherm1(QWidget):
    """Scherm waarin de attracties en hun wachttijden worden weergegeven."""

    def __init__(self, hoofd_venster):
        """Initialiseert het scherm en laadt de attractiedata."""
        super().__init__()

        # Verwijzing naar het hoofdvenster zodat we later van scherm kunnen wisselen
        self._hoofd_venster = hoofd_venster

        # Layout voor het hele scherm aanmaken
        _layout = QVBoxLayout()
        _layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Titel bovenaan het scherm
        _titel = QLabel("Attracties en wachttijden")
        _titel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        _titel.setStyleSheet("font-size: 22px; font-weight: bold; margin-bottom: 10px;")

        # Tabel aanmaken waarin de attracties en wachttijden worden getoond
        self._tabel = QTableWidget()
        self._tabel.setColumnCount(3)  # kolommen: knop, attractienaam, wachttijd
        self._tabel.setHorizontalHeaderLabels(["#", "Attractie", "Wachttijd (minuten)"])
        self._tabel.setStyleSheet("font-size: 16px;")

        # Knop om terug te keren naar de homepagina
        self._knop_terug = QPushButton("Terug naar homepagina")
        self._knop_terug.clicked.connect(self._terug_naar_home)

        # Alle onderdelen toevoegen aan de layout
        _layout.addWidget(_titel)
        _layout.addWidget(self._tabel)
        _layout.addWidget(self._knop_terug)

        # De layout koppelen aan dit scherm
        self.setLayout(_layout)

        # Functie aanroepen om de tabel te vullen met data uit de database
        self._vul_tabel_met_data()

    def _vul_tabel_met_data(self):
        """Haalt de attracties en wachttijden op uit de database en vult de tabel."""
        try:
            # Ophalen van data via de databaseconnectie uit het hoofdvenster
            locaties = self._hoofd_venster.get_database().get_locaties()

            # Aantal rijen in de tabel instellen op basis van het aantal resultaten
            self._tabel.setRowCount(len(locaties))

            # Elke rij vullen met een knop en de bijbehorende data
            for i, (naam, wachttijd) in enumerate(locaties):
                # Maak een knop met de naam van de attractie
                knop = QPushButton(str(naam))

                # Als je op de knop drukt, wordt de attractie doorgegeven aan de reserveringsfunctie
                knop.clicked.connect(lambda _, n=naam: self._reserveer(n))

                # Voeg de knop toe in de eerste kolom
                self._tabel.setCellWidget(i, 0, knop)

                # Vul de attractienaam en wachttijd in de andere kolommen
                self._tabel.setItem(i, 1, QTableWidgetItem(str(naam)))
                self._tabel.setItem(i, 2, QTableWidgetItem(str(wachttijd)))

        except Exception as foutmelding:
            # Als er iets fout gaat bij het ophalen of tonen van data
            print(f"Fout bij laden van wachttijden: {foutmelding}")

    def _reserveer(self, attractie_naam):
        """Wordt uitgevoerd als de gebruiker op een attractie klikt om te reserveren."""
        print(f"Attractie gekozen: {attractie_naam}")

        # De gekozen attractie opslaan in het hoofdvenster zodat andere schermen deze kunnen gebruiken
        self._hoofd_venster.set_geselecteerde_attractie(attractie_naam)

        # Naar het volgende scherm gaan waar de gebruiker een tijdslot kan kiezen
        self._hoofd_venster.toon_pagina(self._hoofd_venster._scherm2)

    def _terug_naar_home(self):
        """Keert terug naar de homepagina."""
        self._hoofd_venster.toon_pagina(self._hoofd_venster._homepagina)
