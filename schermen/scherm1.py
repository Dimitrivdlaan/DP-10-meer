from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QPushButton, QMessageBox
from PyQt6.QtCore import Qt
from mysql.connector import connect, Error


class Scherm1(QWidget):
    def __init__(self, mw=None, db_config=None):
        super().__init__()
        self.db_config = db_config or {"host":"localhost","user":"user","password":"password","database":"LSM_treintje"}
        l = QVBoxLayout(self)
        self.table = QTableWidget(0, 4)
        self.table.setHorizontalHeaderLabels(["locatie_id","naam","beschrijving","wachttijd"])
        l.addWidget(self.table)
        btn = QPushButton("Ververs")
        btn.clicked.connect(self.load_data)
        l.addWidget(btn)
        self.load_data()

    def load_data(self):
        try:
            c = connect(**self.db_config)
            cur = c.cursor()
            cur.execute("SELECT locatie_id,naam,beschrijving,wachttijd FROM locatie")
            rows = cur.fetchall()
            self.table.setRowCount(0)
            for r, row in enumerate(rows):
                self.table.insertRow(r)
                for col, val in enumerate(row):
                    it = QTableWidgetItem(str(val) if val is not None else "")
                    if col == 0:
                        it.setFlags(it.flags() & ~Qt.ItemFlag.ItemIsEditable)
                    self.table.setItem(r, col, it)
            cur.close(); c.close()
        except Error as e:
            QMessageBox.critical(self, "DB fout", str(e))