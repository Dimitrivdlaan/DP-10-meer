# Opmerkingen in deze code zijn door mij geschreven ter verduidelijking van de werking. 
# Dit is het startpunt van de applicatie, hier wordt de hoofdwindow geopend en de stijl geladen.

from PyQt6.QtWidgets import QApplication
from schermen.main_window import MainWindow  # import aangepast voor juiste pad

def main():
    app = QApplication([])

    # stijl van het bestand style.qss laden
    load_stylesheet(app)

    # hoofdvenster starten
    window = MainWindow()
    window.show()

    # app uitvoeren
    app.exec()

def load_stylesheet(app):
    """Laadt de QSS-stylesheet zodat de GUI mooi wordt weergegeven"""
    try:
        with open("style.qss", "r") as f:
            app.setStyleSheet(f.read())
    except FileNotFoundError:
        print("style.qss niet gevonden — standaardstijl wordt gebruikt.")

if __name__ == "__main__":
    main()
