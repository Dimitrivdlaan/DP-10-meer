from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QListWidget, QComboBox
import mysql.connector

class Scherm1(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.qr_id = 1 # omdat ik geen qr code aanmak
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Dit is scherm 1 - Reisplan"))

        self.mydb = mysql.connector.connect(host="localhost", user="user", password="password", database="LSM_treintje") # database connectie
        self.mycursor = self.mydb.cursor()

        self.location_combo = QComboBox()
        self.load_locations()
        layout.addWidget(QLabel("Selecteer een locatie om toe te voegen:"))
        layout.addWidget(self.location_combo)

        self.travel_plan_list = QListWidget()
        layout.addWidget(QLabel("Huidig Reisplan:"))
        layout.addWidget(self.travel_plan_list)
        self.load_travel_plan()

        add_button = QPushButton("Toevoegen aan Reisplan")
        add_button.clicked.connect(self.add_to_travel_plan)
        layout.addWidget(add_button)
        self.setLayout(layout)

    def load_locations(self):
        self.mycursor.execute("SELECT locatie_id, naam FROM locatie")
        locations = self.mycursor.fetchall()
        self.location_combo.clear()
        self.location_data = {loc_id: name for loc_id, name in locations}
        for loc_id, name in locations:
            self.location_combo.addItem(name, loc_id)

    def load_travel_plan(self):
        self.mycursor.execute("SELECT locatie_id FROM reisplan WHERE qr_id = %s", (self.qr_id,))
        plan = self.mycursor.fetchall()
        self.travel_plan_list.clear()
        for (loc_id,) in plan:
            name = self.location_data.get(loc_id, f"Locatie {loc_id}")
            self.travel_plan_list.addItem(name)

    def add_to_travel_plan(self):
        selected_index = self.location_combo.currentIndex()
        if selected_index >= 0:
            loc_id = self.location_combo.itemData(selected_index)
            name = self.location_combo.currentText()
            self.mycursor.execute("SELECT qr_id FROM qrcode WHERE qr_id = %s", (self.qr_id,))
            if not self.mycursor.fetchone():
                self.mycursor.execute("INSERT INTO qrcode (qr_id) VALUES (%s)", (self.qr_id,))
                self.mydb.commit()
            self.mycursor.execute("SELECT * FROM reisplan WHERE qr_id = %s AND locatie_id = %s", (self.qr_id, loc_id))
            if not self.mycursor.fetchone():
                self.mycursor.execute("INSERT INTO reisplan (qr_id, locatie_id) VALUES (%s, %s)", (self.qr_id, loc_id))
                self.mydb.commit()
                self.travel_plan_list.addItem(name)