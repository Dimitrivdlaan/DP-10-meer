from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt6.QtGui import QPixmap
import qrcode
import mysql.connector
from io import BytesIO
from PIL import Image
import base64

class Scherm5(QWidget):
    def __init__(self, main_window, qr_id):
        super().__init__()
        self.main_window = main_window
        self.qr_id = qr_id
        layout = QVBoxLayout()

        layout.addWidget(QLabel("Uw QR-code voor vandaag:"))

        self.qr_label = QLabel()
        layout.addWidget(self.qr_label)
        self.generate_qr_code()

        btn_terug = QPushButton("Terug naar Reisplan")
        btn_terug.setObjectName("nav-button")
        btn_terug.clicked.connect(lambda: self.main_window.toon_pagina(self.main_window.scherm1))
        layout.addWidget(btn_terug)

        self.setLayout(layout)

    def generate_qr_code(self):
        # Haal reisplan data op
        mydb = mysql.connector.connect(host="localhost", user="user", password="password", database="LSM_treintje")
        mycursor = mydb.cursor()
        
        mycursor.execute("SELECT l.naam FROM reisplan rp JOIN locatie l ON rp.locatie_id = l.locatie_id WHERE rp.qr_id = %s", (self.qr_id,))
        plan = mycursor.fetchall()
        
        # Maak QR data: qr_id, datum, lijst van locaties
        from datetime import date
        today = date.today().isoformat()
        locations = [name for (name,) in plan]
        qr_data = f"QR:{self.qr_id}|DATE:{today}|LOCATIONS:{','.join(locations)}"
        
        # Update database met data en datum
        mycursor.execute("UPDATE qrcode SET data = %s, datum = %s WHERE qr_id = %s", (qr_data, today, self.qr_id))
        mydb.commit()
        
        # Genereer QR code
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(qr_data)
        qr.make(fit=True)
        img = qr.make_image(fill='black', back_color='white')
        
        # Converteer naar QPixmap voor PyQt6
        buffer = BytesIO()
        img.save(buffer, format="PNG")
        buffer.seek(0)
        
        pixmap = QPixmap()
        pixmap.loadFromData(buffer.read())
        self.qr_label.setPixmap(pixmap)