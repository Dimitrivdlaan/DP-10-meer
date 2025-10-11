# Opmerkingen in deze code zijn door mij geschreven ter verduidelijking van de werking. 
# De gebruiker ziet hier zijn bevestiging en kan eventueel terug naar de homepagina.

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt6.QtCore import Qt
import qrcode

class Scherm3(QWidget):
    def __init__(self, main_window):
        super().__init__()

        # Verwijzing naar het hoofdvenster om schermen te kunnen wisselen
        self._main_window = main_window

        # Layout aanmaken voor dit scherm
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Titel bovenaan
        titel = QLabel("Je instapbewijs is aangemaakt!")
        titel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        titel.setStyleSheet("font-size: 20px; font-weight: bold; margin-bottom: 10px;")

        # Label om QR-code tekst of melding te tonen
        self._label_qr = QLabel("QR-code wordt hieronder getoond.")
        self._label_qr.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Knop om QR-code te genereren
        self._btn_genereer = QPushButton("Genereer mijn QR-code")
        self._btn_genereer.clicked.connect(self._genereer_qr)

        # Knop om terug te keren naar de homepagina
        self._btn_terug = QPushButton("Terug naar homepagina")
        self._btn_terug.clicked.connect(self._terug_home)

        # Onderdelen toevoegen aan layout
        layout.addWidget(titel)
        layout.addWidget(self._label_qr)
        layout.addWidget(self._btn_genereer)
        layout.addWidget(self._btn_terug)

        # Layout koppelen aan het scherm
        self.setLayout(layout)

    def _genereer_qr(self):
        """Maakt een QR-code aan voor de bevestiging."""
        try:
            # Tekst voor de QR-code, dit kan later worden uitgebreid met echte data
            data = "Bevestiging: Lake Side Mania - Tijdslot bevestigd"

            # QR-code aanmaken (bron: geeksforgeeks.org, aangepast naar eigen gebruik)
            qr = qrcode.make(data)

            # QR-code opslaan als afbeelding
            qr.save("qrcode_bevestiging.png")
            print("QR-code gegenereerd en opgeslagen als 'qrcode_bevestiging.png'.")

            # Tekst in het scherm bijwerken
            self._label_qr.setText("QR-code succesvol gegenereerd. Kijk in je projectmap voor het bestand.")
        except Exception as e:
            self._label_qr.setText(f"Er ging iets mis bij het maken van de QR-code: {e}")

    def _terug_home(self):
        """Keert terug naar de homepagina."""
        self._main_window.toon_pagina(self._main_window._homepagina)

