from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
import qrcode 
import io

class Scherm3(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

        # layout voor dit scherm
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # titel bovenaan
        titel = QLabel("Je persoonlijke QR-code")
        titel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        titel.setStyleSheet("font-size: 20px; font-weight: bold; margin-bottom: 20px;")
        layout.addWidget(titel)

        # QR-code genereren met de qrcode library
        # bron: geeksforgeeks.org - Generate QR Code using qrcode in Python
        # (heb ik gebruikt als voorbeeld om te leren hoe je QR-code aanmaakt)
        data = "RESERVERING | Lakeside Mania | 20 minuten geldig"
        qr_img = qrcode.make(data)

        # QR-code omzetten naar afbeelding die PyQt kan tonen
        buffer = io.BytesIO()
        qr_img.save(buffer, format="PNG")
        qr_bytes = buffer.getvalue()

        pixmap = QPixmap()
        pixmap.loadFromData(qr_bytes)
        label_qr = QLabel()
        label_qr.setPixmap(pixmap)
        label_qr.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label_qr)

        # knop om terug te gaan naar startpagina
        btn_terug = QPushButton("Terug naar startpagina")
        btn_terug.setFixedHeight(40)
        btn_terug.setStyleSheet("font-size: 16px; margin-top: 20px;")
        btn_terug.clicked.connect(lambda: self.main_window.toon_pagina(self.main_window.startscherm))
        layout.addWidget(btn_terug)

        # layout instellen
        self.setLayout(layout)
