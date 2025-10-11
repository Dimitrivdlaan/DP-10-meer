from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt6.QtCore import Qt

class Startscherm(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

        # hoofd layout
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # titel bovenaan
        titel = QLabel("Welkom bij de Lakeside Mania app")
        titel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        titel.setStyleSheet("font-size: 22px; font-weight: bold; margin-bottom: 20px;")
        layout.addWidget(titel)

        # lijst met knoppen (zoals op wireframe)
        knoppen = ["Knop 1", "Knop 2", "Knop 3", "Knop 4", "Knop 5", "Lakeside Mania"]

        # knoppen toevoegen aan layout
        for tekst in knoppen:
            knop = QPushButton(tekst)
            knop.setFixedHeight(40)
            knop.setStyleSheet("font-size: 16px; margin: 5px;")
            layout.addWidget(knop)

        # laatste knop (Lakeside Mania) gaat naar de volgende pagina
        layout.itemAt(layout.count() - 1).widget().clicked.connect(
    lambda: self.main_window.toon_pagina(self.main_window.get_scherm1())
        )

        # layout instellen voor het scherm
        self.setLayout(layout)
