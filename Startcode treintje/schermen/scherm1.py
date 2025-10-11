# Opmerkingen in deze code zijn door mij geschreven ter verduidelijking van de werking.
# Dit scherm toont de attracties en hun wachttijden, en laat de gebruiker een attractie kiezen om te reserveren.

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QTableWidget, QTableWidgetItem
from PyQt6.QtCore import Qt

class Scherm1(QWidget):
    def __init__(self, main_window):
        super().__init__()

        # Verwijzing naar het hoofdvenster zodat we later van scherm kunnen wisselen
        self._main_window = main_window

        # Layout voor het hele scherm aanmaken
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Titel bovenaan het scherm
        titel = QLabel("Attracties en wachttijden")
        titel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        titel.setStyleSheet("font-size: 22px; font-weight: bold; margin-bottom: 10px;")

        # Tabel aanmaken waarin de attracties en wachttijden worden getoond
        self._tabel = QTableWidget()
        self._tabel.setColumnCount(3)  # kolommen: knop, attractienaam, wachttijd
        self._tabel.setHorizontalHeaderLabels(["#", "Attractie", "Wachttijd (minuten)"])
        self._tabel.setStyleSheet("font-size: 16px;")

        # Knop om terug te keren naar de homepagina
        self._btn_terug = QPushButton("Terug naar homepagina")
        self._btn_terug.clicked.connect(self._terug_naar_home)

        # Alle onderdelen toevoegen aan de layout
        layout.addWidget(titel)
        layout.addWidget(self._tabel)
        layout.addWidget(self._btn_terug)

        # De layout koppelen aan dit scherm
        self.setLayout(layout)

        # Functie aanroepen om de tabel te vullen met data uit de database
        self._vul_tabel_met_data()

    def _vul_tabel_met_data(self):
        """Haalt de attracties en wachttijden op uit de database en vult de tabel."""
        try:
            # Ophalen van data via de databaseconnectie uit het main_window
            locaties = self._main_window.get_database().get_locaties()

            # Aantal rijen in de tabel instellen op basis van het aantal resultaten
            self._tabel.setRowCount(len(locaties))

            # Elke rij vullen met een knop en de bijbehorende data
            for i, (naam, wachttijd) in enumerate(locaties):
                # Maak een knop met de naam van de attractie
                btn = QPushButton(str(naam))
                # Als je op de knop drukt, wordt de attractie doorgegeven aan de reserveringsfunctie
                btn.clicked.connect(lambda _, n=naam: self._reserveer(n))
                # Voeg de knop toe in de eerste kolom
                self._tabel.setCellWidget(i, 0, btn)

                # Vul de attractienaam en wachttijd in de andere kolommen
                self._tabel.setItem(i, 1, QTableWidgetItem(str(naam)))
                self._tabel.setItem(i, 2, QTableWidgetItem(str(wachttijd)))

        except Exception as e:
            # Als er iets fout gaat bij het ophalen of tonen van data
            print(f"Fout bij laden van wachttijden: {e}")

    def _reserveer(self, attractie_naam):
        """Wordt uitgevoerd als de gebruiker op een attractie klikt om te reserveren."""
        print(f"Attractie gekozen: {attractie_naam}")

        # De gekozen attractie opslaan in het main window zodat andere schermen deze kunnen gebruiken
        self._main_window.set_geselecteerde_attractie(attractie_naam)

        # Naar het volgende scherm gaan waar de gebruiker een tijdslot kan kiezen
        self._main_window.toon_pagina(self._main_window._scherm2)

    def _terug_naar_home(self):
        """Keert terug naar de homepagina."""
        self._main_window.toon_pagina(self._main_window._homepagina)
