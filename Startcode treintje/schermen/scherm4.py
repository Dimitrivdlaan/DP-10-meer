# Opmerkingen in deze code zijn door mij geschreven ter verduidelijking van de werking.

"""
Hier krijgt de gebruiker een bevestiging en kan hij terug naar het hoofdmenu of de app afsluiten.
"""

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt6.QtCore import Qt


class Scherm4(QWidget):
    """Scherm waarin de gebruiker een bevestiging ontvangt en kan afsluiten of terugkeren naar de homepagina."""

    def __init__(self, hoofd_venster):
        """Initialiseert het scherm en maakt de bevestigingsinterface aan."""
        super().__init__()

        # Verwijzing naar het hoofdvenster om te kunnen wisselen tussen schermen
        self._hoofd_venster = hoofd_venster

        # Layout aanmaken
        _layout = QVBoxLayout()
        _layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Titel bovenaan
        _titel = QLabel("Bedankt voor je reservering!")
        _titel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        _titel.setStyleSheet("font-size: 20px; font-weight: bold; margin-bottom: 10px;")

        # Bevestigingstekst onder de titel
        self._label_info = QLabel("Je reservering is succesvol afgerond.\nWe wensen je veel plezier in het park.")
        self._label_info.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._label_info.setStyleSheet("font-size: 14px; margin-bottom: 20px;")

        # Knop om terug te keren naar de homepagina
        self._knop_home = QPushButton("Terug naar homepagina")
        self._knop_home.clicked.connect(self._terug_home)

        # Knop om de applicatie af te sluiten
        self._knop_sluiten = QPushButton("App afsluiten")
        self._knop_sluiten.clicked.connect(self._app_sluiten)

        # Onderdelen toevoegen aan de layout
        _layout.addWidget(_titel)
        _layout.addWidget(self._label_info)
        _layout.addWidget(self._knop_home)
        _layout.addWidget(self._knop_sluiten)

        # Layout instellen
        self.setLayout(_layout)

    def _terug_home(self):
        """Keert terug naar de homepagina."""
        self._hoofd_venster.toon_pagina(self._hoofd_venster._homepagina)

    def _app_sluiten(self):
        """Sluit de applicatie netjes af."""
        self._hoofd_venster.close()

