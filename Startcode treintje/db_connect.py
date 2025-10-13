# Opmerkingen in deze code zijn door mij geschreven ter verduidelijking van de werking.

"""
Deze module beheert de verbinding met de MySQL-database.
Hier worden gegevens opgehaald (zoals locaties en wachttijden) en reserveringen toegevoegd.
"""

import mysql.connector


class DatabaseConnectie:
    """Beheert de verbinding en interactie met de MySQL-database van Lake Side Mania."""

    def __init__(self):
        """Initialiseert de databaseverbinding met inloggegevens en instellingen."""
        # Database-inloggegevens als privé variabelen
        self._host = "localhost"
        self._gebruiker = "root"
        self._wachtwoord = "Mistry123!"
        self._database_naam = "LSM_treintje"

        # Variabelen voor de verbinding en cursor
        self._verbinding = None
        self._cursor = None

    def open_verbinding(self):
        """Maakt verbinding met de database."""
        try:
            self._verbinding = mysql.connector.connect(
                host=self._host,
                user=self._gebruiker,
                password=self._wachtwoord,
                database=self._database_naam
            )
            self._cursor = self._verbinding.cursor()
            print("Verbonden met database.")
        except mysql.connector.Error as foutmelding:
            print(f"Fout bij verbinden met database: {foutmelding}")

    def toon_locaties(self):
        """Toont alle locaties met hun wachttijden in de console."""
        try:
            self._cursor.execute("SELECT locatie_id, naam, wachttijd FROM Locatie")

            print("\nBeschikbare locaties in de database:\n")
            for locatie_id, naam, wachttijd in self._cursor.fetchall():
                print(f"{locatie_id}: {naam} (wachttijd: {wachttijd} minuten)")
        except mysql.connector.Error as foutmelding:
            print(f"Fout bij ophalen van data: {foutmelding}")

    def get_locaties(self):
        """Haalt namen en wachttijden van attracties op als lijst van tuples."""
        try:
            self._cursor.execute("SELECT naam, wachttijd FROM Locatie")
            return self._cursor.fetchall()
        except mysql.connector.Error as foutmelding:
            print(f"Fout bij laden van wachttijden: {foutmelding}")
            return []

    def voeg_reservering_toe(self, attractie, tijdslot):
        """Voegt een reservering toe voor een attractie en tijdslot."""
        try:
            query = "INSERT INTO Reservering (attractie, tijdslot) VALUES (%s, %s)"
            self._cursor.execute(query, (attractie, tijdslot))
            self._verbinding.commit()
            print(f"Reservering toegevoegd: {attractie} om {tijdslot}")
        except mysql.connector.Error as foutmelding:
            print(f"Fout bij toevoegen van reservering: {foutmelding}")

    # Extra belangrijke queries (voor feedback docent)

    def verwijder_reservering(self, reservering_id):
        """Verwijdert een bestaande reservering op basis van het ID."""
        try:
            query = "DELETE FROM Reservering WHERE reservering_id = %s"
            self._cursor.execute(query, (reservering_id,))
            self._verbinding.commit()
            print(f"Reservering met ID {reservering_id} verwijderd.")
        except mysql.connector.Error as foutmelding:
            print(f"Fout bij verwijderen van reservering: {foutmelding}")

    def update_wachttijd(self, attractie, nieuwe_wachttijd):
        """Wijzigt de wachttijd van een specifieke attractie."""
        try:
            query = "UPDATE Locatie SET wachttijd = %s WHERE naam = %s"
            self._cursor.execute(query, (nieuwe_wachttijd, attractie))
            self._verbinding.commit()
            print(f"Wachttijd voor '{attractie}' aangepast naar {nieuwe_wachttijd} minuten.")
        except mysql.connector.Error as foutmelding:
            print(f"Fout bij bijwerken van wachttijd: {foutmelding}")

    def zoek_reserveringen(self):
        """Geeft een lijst met alle reserveringen (attractie + tijdslot)."""
        try:
            self._cursor.execute("SELECT attractie, tijdslot FROM Reservering")
            return self._cursor.fetchall()
        except mysql.connector.Error as foutmelding:
            print(f"Fout bij ophalen van reserveringen: {foutmelding}")
            return []

    def sluit_verbinding(self):
        """Sluit de databaseverbinding netjes af."""
        if self._verbinding and self._verbinding.is_connected():
            self._cursor.close()
            self._verbinding.close()
            print("Verbinding met database gesloten.")
