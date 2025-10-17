from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QComboBox, QScrollArea, QHBoxLayout
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

        self.scroll_area = QScrollArea()
        self.container = QWidget()
        self.layout_plan = QVBoxLayout(self.container)
        self.scroll_area.setWidget(self.container)
        self.scroll_area.setWidgetResizable(True)
        layout.addWidget(QLabel("Huidig Reisplan:"))
        layout.addWidget(self.scroll_area)
        self.load_travel_plan()

        add_button = QPushButton("Toevoegen aan Reisplan")
        add_button.setObjectName("action-button")
        add_button.clicked.connect(self.add_to_travel_plan)
        layout.addWidget(add_button)

        nav_layout = QHBoxLayout()
        btn_terug_naar_scherm4 = QPushButton("Terug naar Scherm 4")
        btn_terug_naar_scherm4.setObjectName("nav-button")
        btn_terug_naar_scherm4.clicked.connect(lambda: self.main_window.toon_pagina(self.main_window.scherm4))
        nav_layout.addWidget(btn_terug_naar_scherm4)

        btn_naar_start = QPushButton("Naar Start")
        btn_naar_start.setObjectName("nav-button")
        btn_naar_start.clicked.connect(lambda: self.main_window.toon_pagina(self.main_window.startscherm))
        nav_layout.addWidget(btn_naar_start)

        layout.addLayout(nav_layout)
        self.setLayout(layout)

    def load_locations(self):
        self.mycursor.execute("SELECT locatie_id, naam, wachttijd FROM locatie")
        locations = self.mycursor.fetchall()
        self.location_combo.clear()
        self.location_data = {loc_id: (name, wachttijd) for loc_id, name, wachttijd in locations}
        for loc_id, name, wachttijd in locations:
            self.location_combo.addItem(f"{name} ({wachttijd})", loc_id)

    def load_travel_plan(self):
        # Clear existing widgets
        while self.layout_plan.count():
            child = self.layout_plan.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        
        self.mycursor.execute("SELECT locatie_id FROM reisplan WHERE qr_id = %s", (self.qr_id,))
        plan = self.mycursor.fetchall()
        for (loc_id,) in plan:
            name, wachttijd = self.location_data.get(loc_id, (f"Locatie {loc_id}", ""))
            self.add_attraction_widget(loc_id, name, wachttijd)

    def add_attraction_widget(self, loc_id, name, wachttijd):
        widget = QWidget()
        h_layout = QHBoxLayout(widget)
        label = QLabel(f"{name} ({wachttijd})")
        h_layout.addWidget(label)
        remove_button = QPushButton("Verwijderen")
        remove_button.setObjectName("remove-button")
        remove_button.clicked.connect(lambda: self.remove_from_travel_plan(loc_id, widget))
        h_layout.addWidget(remove_button)
        self.layout_plan.addWidget(widget)

    def remove_from_travel_plan(self, loc_id, widget):
        self.mycursor.execute("DELETE FROM reisplan WHERE qr_id = %s AND locatie_id = %s", (self.qr_id, loc_id))
        self.mydb.commit()
        widget.deleteLater()
        self.layout_plan.removeWidget(widget)

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
                name, wachttijd = self.location_data[loc_id]
                self.add_attraction_widget(loc_id, name, wachttijd)