from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QTableWidget, QTableWidgetItem
from PyQt6.QtCore import Qt

class Scherm1(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

        # hoofd layout van dit scherm
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # titel bovenaan
        titel = QLabel("Attracties / wachttijden")
        titel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        titel.setStyleSheet("font-size: 20px; font-weight: bold; margin-bottom: 15px;")
        layout.addWidget(titel)

        # tabel aanmaken voor de attracties
        self.tabel = QTableWidget()
        self.tabel.setColumnCount(2)
        self.tabel.setHorizontalHeaderLabels(["Attractie", "Wachttijd (minuten)"])
        self.tabel.horizontalHeader().setStretchLastSection(True)
        self.tabel.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)  # niks aanpassen in tabel
        layout.addWidget(self.tabel)

        # data uit de database ophalen
        self.toon_locaties()

        # knop om een reservering te maken
        btn_reserveer = QPushButton("Maak een reservering")
        btn_reserveer.setFixedHeight(40)
        btn_reserveer.setStyleSheet("font-size: 16px; margin-top: 10px;")
        btn_reserveer.clicked.connect(lambda: self.main_window.toon_pagina(self.main_window.scherm2))
        layout.addWidget(btn_reserveer)

        # knop om de app af te sluiten
        btn_sluit = QPushButton("Sluit de app af")
        btn_sluit.setFixedHeight(40)
        btn_sluit.setStyleSheet("font-size: 16px; margin-top: 5px;")
        btn_sluit.clicked.connect(lambda: self.main_window.close())
        layout.addWidget(btn_sluit)

        # layout instellen
        self.setLayout(layout)

    def toon_locaties(self):
        """Haalt de attracties en wachttijden op uit de database en vult de tabel"""
        locaties = self.main_window.get_locaties()

        if not locaties:
            # als er niks in de database zit
            self.tabel.setRowCount(1)
            self.tabel.setItem(0, 0, QTableWidgetItem("Geen attracties gevonden"))
            self.tabel.setItem(0, 1, QTableWidgetItem("-"))
        else:
            # vul tabel met de database data
            self.tabel.setRowCount(len(locaties))
            for i, (naam, wachttijd) in enumerate(locaties):
                self.tabel.setItem(i, 0, QTableWidgetItem(str(naam)))
                self.tabel.setItem(i, 1, QTableWidgetItem(str(wachttijd)))
