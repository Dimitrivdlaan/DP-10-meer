# Opmerkingen in deze code zijn door mij geschreven ter verduidelijking van de werking.
# Dit is het startscherm van de applicatie. 
# De gebruiker ziet hier een welkomstbericht en verschillende knoppen (zoals in het wireframe), waarvan de laatste knop "Lakeside Mania" doorverwijst naar de homepagina.

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt6.QtCore import Qt

class Startscherm(QWidget):
    def __init__(self, main_window):
        super().__init__()

        # Verwijzing naar het hoofdvenster zodat we later van scherm kunnen wisselen
        self.main_window = main_window

        # Hoofd-layout aanmaken en centreren op het scherm
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Titel bovenaan het scherm
        titel = QLabel("Welkom bij de Lakeside Mania app")
        titel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        titel.setStyleSheet("font-size: 22px; font-weight: bold; margin-bottom: 20px;")
        layout.addWidget(titel)

        # Lijst met knoppen zoals in het ontwerp (wireframe)
        knoppen = ["Knop 1", "Knop 2", "Knop 3", "Knop 4", "Knop 5", "Lakeside Mania"]

        # Elke knop wordt aangemaakt en toegevoegd aan de layout
        for tekst in knoppen:
            knop = QPushButton(tekst)              # knop aanmaken met tekst
            knop.setFixedHeight(40)                # vaste hoogte instellen
            knop.setStyleSheet("font-size: 16px; margin: 5px;")  # stijl toepassen
            layout.addWidget(knop)                 # knop toevoegen aan de layout

        # De laatste knop ("Lakeside Mania") verwijst naar de homepagina
        layout.itemAt(layout.count() - 1).widget().clicked.connect(
            lambda: self.main_window.toon_pagina(self.main_window._homepagina)
        )

        # De samengestelde layout koppelen aan dit scherm
        self.setLayout(layout)
