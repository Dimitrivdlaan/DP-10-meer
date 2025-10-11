# Opmerkingen in deze code zijn door mij geschreven ter verduidelijking van de werking. 
# Hier krijgt de gebruiker een bevestiging en kan hij terug naar het hoofdmenu of de app afsluiten.

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt6.QtCore import Qt

class Scherm4(QWidget):
    def __init__(self, main_window):
        super().__init__()

        # Verwijzing naar het hoofdvenster om te kunnen wisselen tussen schermen
        self._main_window = main_window

        #Layout aanmaken
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Titel bovenaan
        titel = QLabel("Bedankt voor je reservering!")
        titel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        titel.setStyleSheet("font-size: 20px; font-weight: bold; margin-bottom: 10px;")

        # Bevestigingstekst onder de titel
        self._label_info = QLabel("Je reservering is succesvol afgerond.\nWe wensen je veel plezier in het park.")
        self._label_info.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._label_info.setStyleSheet("font-size: 14px; margin-bottom: 20px;")

        # Knop om terug te keren naar het hoofdmenu
        self._btn_home = QPushButton("Terug naar homepagina")
        self._btn_home.clicked.connect(self._terug_home)

        # Knop om de applicatie af te sluiten
        self._btn_sluiten = QPushButton("App afsluiten")
        self._btn_sluiten.clicked.connect(self._app_sluiten)

        # Onderdelen toevoegen aan de layout
        layout.addWidget(titel)
        layout.addWidget(self._label_info)
        layout.addWidget(self._btn_home)
        layout.addWidget(self._btn_sluiten)

        # Layout instellen
        self.setLayout(layout)

    def _terug_home(self):
        """Keert terug naar de homepagina."""
        self._main_window.toon_pagina(self._main_window._homepagina)

    def _app_sluiten(self):
        """Sluit de applicatie netjes af."""
        self._main_window.close()