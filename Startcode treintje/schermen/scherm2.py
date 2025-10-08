from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QComboBox, QMessageBox, QHBoxLayout
from PyQt6.QtCore import Qt

class Scherm2(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

        # hoofd layout
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # titel bovenaan
        titel = QLabel("Reservering maken")
        titel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        titel.setStyleSheet("font-size: 20px; font-weight: bold; margin-bottom: 20px;")
        layout.addWidget(titel)

        # tekst boven dropdowns
        uitleg = QLabel("Kies een attractie en een tijd:")
        uitleg.setAlignment(Qt.AlignmentFlag.AlignCenter)
        uitleg.setStyleSheet("font-size: 14px; margin-bottom: 10px;")
        layout.addWidget(uitleg)

        # horizontale layout voor de 2 dropdowns
        keuze_layout = QHBoxLayout()

        # dropdown voor attracties
        self.combo_attractie = QComboBox()
        self.combo_attractie.setFixedWidth(200)
        self.combo_attractie.setStyleSheet("font-size: 14px;")
        keuze_layout.addWidget(self.combo_attractie)

        # dropdown voor tijden
        self.combo_tijd = QComboBox()
        self.combo_tijd.setFixedWidth(200)
        self.combo_tijd.setStyleSheet("font-size: 14px;")
        keuze_layout.addWidget(self.combo_tijd)

        layout.addLayout(keuze_layout)

        # data inladen in de dropdowns
        self.vul_attracties_in()
        self.vul_tijden_in()

        # knop om te bevestigen
        btn_bevestig = QPushButton("Bevestig mijn reis")
        btn_bevestig.setFixedHeight(40)
        btn_bevestig.setStyleSheet("font-size: 16px; margin-top: 20px;")
        btn_bevestig.clicked.connect(self.bevestig_reservering)
        layout.addWidget(btn_bevestig)

        # knop om terug te gaan naar het vorige scherm
        btn_terug = QPushButton("← Terug")
        btn_terug.setFixedHeight(35)
        btn_terug.setStyleSheet("font-size: 14px; margin-top: 10px;")
        btn_terug.clicked.connect(lambda: self.main_window.toon_pagina(self.main_window.scherm1))
        layout.addWidget(btn_terug)

        # layout instellen
        self.setLayout(layout)

    def vul_attracties_in(self):
        """Haalt attracties op uit de database en vult de combobox"""
        locaties = self.main_window.get_locaties()
        if not locaties:
            self.combo_attractie.addItem("Geen attracties gevonden")
        else:
            for naam, _ in locaties:
                self.combo_attractie.addItem(naam)

    def vul_tijden_in(self):
        """Vult de tijden in de combobox (voorlopig vaste tijden)"""
        tijden = ["10:00", "10:30", "11:00", "11:30", "12:00", "12:30", "13:00", "13:30", "14:00", "14:30", "15:00"]
        for t in tijden:
            self.combo_tijd.addItem(t)

    def bevestig_reservering(self):
        """Wordt uitgevoerd als gebruiker op 'Bevestig mijn reis' drukt"""
        attractie = self.combo_attractie.currentText()
        tijd = self.combo_tijd.currentText()

        if attractie == "Geen attracties gevonden":
            QMessageBox.warning(self, "Let op", "Er zijn geen attracties om te reserveren.")
            return

        # laat een melding zien met de gekozen attractie en tijd
        QMessageBox.information(self, "Reservering bevestigd",
            f"Je hebt '{attractie}' gekozen voor {tijd}.\n"
            "Je QR-code wordt nu aangemaakt...")

        # ga naar het volgende scherm (QR-code scherm)
        self.main_window.toon_pagina(self.main_window.scherm3)