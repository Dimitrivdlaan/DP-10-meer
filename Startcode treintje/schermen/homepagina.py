# Opmerkingen in deze code zijn door mij geschreven ter verduidelijking van de werking. 
# Hier kan de gebruiker door naar de wachttijden, reservering of zijn QR-code bekijken.

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt6.QtCore import Qt

class Homepagina(QWidget):
    def __init__(self, main_window):
        super().__init__()

        # Verwijzing naar main window zodat ik andere schermen kan openen
        self._main_window = main_window

        # Layout aanmaken voor de pagina
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Titel bovenaan het scherm
        titel = QLabel("Welkom bij Lake Side Mania")
        titel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        titel.setStyleSheet("font-size: 24px; font-weight: bold;")

        # Knop om wachttijden te bekijken
        self._btn_wachttijden = QPushButton("Attracties / wachttijden")
        self._btn_wachttijden.clicked.connect(self._open_wachttijden)

        # Knop voor instapbewijs (QR-code)
        self._btn_qrcode = QPushButton("Mijn instapbewijs (QR-code)")
        self._btn_qrcode.clicked.connect(self._open_qrcode)

        # Knop om de app af te sluiten
        self._btn_afsluiten = QPushButton("Sluit de app af")
        self._btn_afsluiten.clicked.connect(self._app_sluiten)

        # Alles toevoegen aan de layout
        layout.addWidget(titel)
        layout.addWidget(self._btn_wachttijden)
        layout.addWidget(self._btn_qrcode)
        layout.addWidget(self._btn_afsluiten)

        # Layout koppelen aan het scherm
        self.setLayout(layout)

    def _open_wachttijden(self):
        """Opent het scherm met attracties en wachttijden."""
        # Wissel naar het juiste scherm via main window
        self._main_window.toon_pagina(self._main_window._scherm1)

    def _open_qrcode(self):
        """Opent het scherm waar de QR-code wordt getoond."""
        self._main_window.toon_pagina(self._main_window._scherm3)

    def _app_sluiten(self):
        """Sluit de app netjes af."""
        self._main_window.close()

        
