# Opmerkingen in deze code zijn door mij geschreven ter verduidelijking van de werking.

"""
Dit is het startscherm van de applicatie.
De gebruiker ziet hier een welkomstbericht en verschillende knoppen (zoals in het wireframe),
waarvan de laatste knop 'Lakeside Mania' doorverwijst naar de homepagina.
"""

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt6.QtCore import Qt


class Startscherm(QWidget):
    """Startscherm van de applicatie met een welkomstbericht en navigatieknoppen."""

    def __init__(self, hoofd_venster):
        """Initialiseert het startscherm en maakt de knoppen aan."""
        super().__init__()

        # Verwijzing naar het hoofdvenster zodat we later van scherm kunnen wisselen
        self._hoofd_venster = hoofd_venster

        # Hoofd-layout aanmaken en centreren op het scherm
        _layout = QVBoxLayout()
        _layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Titel bovenaan het scherm
        _titel = QLabel("Welkom bij de Lakeside Mania app")
        _titel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        _titel.setStyleSheet("font-size: 22px; font-weight: bold; margin-bottom: 20px;")
        _layout.addWidget(_titel)

        # Lijst met knoppen zoals in het ontwerp (wireframe)
        _knoppen = ["Knop 1", "Knop 2", "Knop 3", "Knop 4", "Knop 5", "Lakeside Mania"]

        # Elke knop aanmaken en toevoegen aan de layout
        for tekst in _knoppen:
            knop = QPushButton(tekst)  # knop aanmaken met tekst
            knop.setFixedHeight(40)  # vaste hoogte instellen
            knop.setStyleSheet("font-size: 16px; margin: 5px;")  # stijl toepassen
            _layout.addWidget(knop)  # knop toevoegen aan de layout

        # De laatste knop ("Lakeside Mania") verwijst naar de homepagina
        _layout.itemAt(_layout.count() - 1).widget().clicked.connect(
            lambda: self._hoofd_venster.toon_pagina(self._hoofd_venster._homepagina)
        )

        # De samengestelde layout koppelen aan dit scherm
        self.setLayout(_layout)
