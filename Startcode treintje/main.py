# Opmerkingen in deze code zijn door mij geschreven ter verduidelijking van de werking.

"""
Dit is het startpunt van de applicatie.
Hier wordt het hoofdvenster geopend en de opmaakstijl (QSS-bestand) geladen.
"""

from PyQt6.QtWidgets import QApplication
from schermen.main_window import HoofdVenster  # import aangepast voor juiste pad


def main():
    """Start de applicatie en opent het hoofdvenster."""
    app = QApplication([])

    # Stijl van het bestand style.qss laden
    laad_opmaakstijl(app)

    # Hoofdvenster starten
    venster = HoofdVenster()
    venster.show()

    # Applicatie uitvoeren
    app.exec()


def laad_opmaakstijl(app):
    """Laadt de QSS-stylesheet zodat de GUI mooi wordt weergegeven."""
    try:
        with open("style.qss", "r") as bestand:
            app.setStyleSheet(bestand.read())
    except FileNotFoundError:
        print("style.qss niet gevonden — standaardstijl wordt gebruikt.")


if __name__ == "__main__":
    main()
