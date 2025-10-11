# Opmerkingen in deze code zijn door mij geschreven ter verduidelijking van de werking.
# Dit scherm vormt het hoofdmenu van de applicatie. De gebruiker kan vanaf hier:
# - naar het overzicht van attracties en wachttijden gaan,
# - zijn QR-code bekijken (indien al gegenereerd),
# - of de applicatie afsluiten.

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox
from PyQt6.QtCore import Qt

class Homepagina(QWidget):
    def __init__(self, main_window):
        super().__init__()

        # Verwijzing naar het hoofdvenster, nodig om tussen schermen te kunnen wisselen
        self._main_window = main_window

        # Variabele om bij te houden of er al een QR-code is gegenereerd
        self._qr_gegenereerd = False

        # Hoofd-layout voor de hele pagina
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Titel bovenaan het scherm
        titel = QLabel("Welkom bij Lake Side Mania")
        titel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        titel.setStyleSheet("font-size: 24px; font-weight: bold;")

        # Knop om naar het scherm met attracties en wachttijden te gaan
        self._btn_wachttijden = QPushButton("Attracties / wachttijden")
        self._btn_wachttijden.clicked.connect(self._open_wachttijden)

        # Knop om het scherm met de QR-code te openen
        self._btn_qrcode = QPushButton("Mijn instapbewijs (QR-code)")
        self._btn_qrcode.clicked.connect(self._open_qrcode)

        # Knop om de applicatie af te sluiten
        self._btn_afsluiten = QPushButton("Sluit de app af")
        self._btn_afsluiten.clicked.connect(self._app_sluiten)

        # Onderdelen toevoegen aan de layout (in volgorde van boven naar beneden)
        layout.addWidget(titel)
        layout.addWidget(self._btn_wachttijden)
        layout.addWidget(self._btn_qrcode)
        layout.addWidget(self._btn_afsluiten)

        # De layout koppelen aan dit scherm
        self.setLayout(layout)

    def _open_wachttijden(self):
        """Opent het scherm waar de attracties en hun wachttijden worden weergegeven."""
        self._main_window.toon_pagina(self._main_window._scherm1)

    def _open_qrcode(self):
        """Opent het scherm waar de QR-code wordt getoond, als die al is aangemaakt."""
        scherm3 = self._main_window._scherm3

        # Controleren of er al een QR-code is aangemaakt
        if not scherm3._qr_afbeelding.pixmap():
            # Als er nog geen QR-code is, toon dan een melding voor de gebruiker
            QMessageBox.information(self, "Geen QR-code", "Er is nog geen QR-code gegenereerd.")
        else:
            # Anders, ga naar het QR-scherm
            self._main_window.toon_pagina(scherm3)

    def _app_sluiten(self):
        """Sluit de applicatie netjes af."""
        self._main_window.close()

