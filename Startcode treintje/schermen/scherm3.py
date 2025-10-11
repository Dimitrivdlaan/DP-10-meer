# Opmerkingen in deze code zijn door mij geschreven ter verduidelijking van de werking. 
# De gebruiker ziet hier zijn bevestiging en kan eventueel terug naar de homepagina.

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
import qrcode
import io

class Scherm3(QWidget):
    def __init__(self, main_window):
        super().__init__()

        # Verwijzing naar het hoofdvenster om schermen te kunnen wisselen
        self._main_window = main_window
        self._gekozen_tijd = None  # Tijdslot wordt later ingevuld

        # Layout aanmaken voor dit scherm
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Titel bovenaan
        self._titel = QLabel("Je gekozen tijdslot wordt hieronder getoond.")
        self._titel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._titel.setStyleSheet("font-size: 20px; font-weight: bold; margin-bottom: 10px;")

        # Label om de gekozen tijd te tonen
        self._label_tijd = QLabel("")
        self._label_tijd.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._label_tijd.setStyleSheet("font-size: 16px; margin-bottom: 15px;")

        # Label voor QR-code melding
        self._label_qr = QLabel("")
        self._label_qr.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Label voor de QR-code afbeelding
        self._qr_afbeelding = QLabel()
        self._qr_afbeelding.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Knop om QR-code te genereren
        self._btn_genereer = QPushButton("Genereer mijn QR-code")
        self._btn_genereer.clicked.connect(self._genereer_qr)

        # Knop om terug te keren naar de homepagina
        self._btn_terug = QPushButton("Terug naar homepagina")
        self._btn_terug.clicked.connect(self._terug_home)

        # Onderdelen toevoegen aan layout
        layout.addWidget(self._titel)
        layout.addWidget(self._label_tijd)
        layout.addWidget(self._label_qr)
        layout.addWidget(self._qr_afbeelding)
        layout.addWidget(self._btn_genereer)
        layout.addWidget(self._btn_terug)

        # Layout koppelen aan het scherm
        self.setLayout(layout)

    def stel_tijd_in(self, tijd):
        """Wordt aangeroepen vanuit scherm2 met de gekozen tijd."""
        self._gekozen_tijd = tijd
        self._titel.setText("Je bevestigde tijd is:")
        self._label_tijd.setText(f"{tijd}")
        self._label_qr.setText("")  # Geen melding tot QR-code wordt gemaakt
        self._qr_afbeelding.clear()

    def _genereer_qr(self):
        """Maakt een QR-code aan en toont deze in het scherm."""
        try:
            # Tekst voor de QR-code, bevat gekozen tijdslot
            data = f"Lake Side Mania - Instapbewijs\nTijdslot: {self._gekozen_tijd}"

            # QR-code aanmaken en tonen in het venster
            qr = qrcode.QRCode(version=1, box_size=8, border=2)
            qr.add_data(data)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")

            # QR-code converteren naar afbeelding
            buffer = io.BytesIO()
            img.save(buffer, format="PNG")
            buffer.seek(0)
            pixmap = QPixmap()
            pixmap.loadFromData(buffer.getvalue())
            self._qr_afbeelding.setPixmap(pixmap.scaled(200, 200, Qt.AspectRatioMode.KeepAspectRatio))

            # Tekst bijwerken
            self._label_qr.setText("Je instapbewijs staat klaar. De QR-code wordt hieronder getoond.")
        except Exception as e:
            self._label_qr.setText(f"Er ging iets mis bij het maken van de QR-code: {e}")

    def _terug_home(self):
        """Keert terug naar de homepagina."""
        self._main_window.toon_pagina(self._main_window._homepagina)

