# Opmerkingen in deze code zijn door mij geschreven ter verduidelijking van de werking.

"""
Dit scherm vormt het hoofdmenu van de applicatie.
De gebruiker kan vanaf hier:
- naar het overzicht van attracties en wachttijden gaan,
- zijn QR-code bekijken (indien al gegenereerd),
- of de applicatie afsluiten.
"""

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox
from PyQt6.QtCore import Qt


class HoofdPagina(QWidget):
    """Hoofdmenu van de applicatie."""

    def __init__(self, hoofd_venster):
        """Initialiseert het hoofdmenu en maakt de knoppen en layout aan."""
        super().__init__()

        # Verwijzing naar het hoofdvenster, nodig om tussen schermen te kunnen wisselen
        self._hoofd_venster = hoofd_venster

        # Variabele om bij te houden of er al een QR-code is gegenereerd
        self._qr_gegenereerd = False

        # Hoofd-layout voor de hele pagina
        _hoofd_layout = QVBoxLayout()
        _hoofd_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Titel bovenaan het scherm
        _label_titel = QLabel("Welkom bij Lake Side Mania")
        _label_titel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        _label_titel.setStyleSheet("font-size: 24px; font-weight: bold;")

        # Knop om naar het scherm met attracties en wachttijden te gaan
        self._knop_wachttijden = QPushButton("Attracties / wachttijden")
        self._knop_wachttijden.clicked.connect(self._open_wachttijden)

        # Knop om het scherm met de QR-code te openen
        self._knop_qrcode = QPushButton("Mijn instapbewijs (QR-code)")
        self._knop_qrcode.clicked.connect(self._open_qrcode)

        # Knop om de applicatie af te sluiten
        self._knop_afsluiten = QPushButton("Sluit de app af")
        self._knop_afsluiten.clicked.connect(self._app_sluiten)

        # Onderdelen toevoegen aan de layout (in volgorde van boven naar beneden)
        _hoofd_layout.addWidget(_label_titel)
        _hoofd_layout.addWidget(self._knop_wachttijden)
        _hoofd_layout.addWidget(self._knop_qrcode)
        _hoofd_layout.addWidget(self._knop_afsluiten)

        # De layout koppelen aan dit scherm
        self.setLayout(_hoofd_layout)

    def _open_wachttijden(self):
        """Opent het scherm waar de attracties en hun wachttijden worden weergegeven."""
        self._hoofd_venster.toon_pagina(self._hoofd_venster._scherm_wachttijden)

    def _open_qrcode(self):
        """Opent het scherm waar de QR-code wordt getoond, als die al is aangemaakt."""
        _scherm_qrcode = self._hoofd_venster._scherm_qrcode

        # Controleren of er al een QR-code is aangemaakt
        if not _scherm_qrcode._qr_afbeelding.pixmap():
            QMessageBox.information(self, "Geen QR-code", "Er is nog geen QR-code gegenereerd.")
        else:
            self._hoofd_venster.toon_pagina(_scherm_qrcode)

    def _app_sluiten(self):
        """Sluit de applicatie netjes af."""
        self._hoofd_venster.close()
