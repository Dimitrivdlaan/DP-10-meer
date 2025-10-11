# Opmerkingen in deze code zijn door mij geschreven ter verduidelijking van de werking. 
# Hier haal ik gegevens op (zoals locaties en wachttijden) en kan ik ook reserveringen toevoegen.

import mysql.connector

class DatabaseConnectie:
    def __init__(self):
        # Database-inloggegevens als privé variabelen
        self._host = "localhost"
        self._user = "root"
        self._password = "Mistry123!"
        self._database = "LSM_treintje"

        # Variabelen voor de verbinding en cursor
        self._conn = None
        self._cursor = None

    def open_verbinding(self):
        """Maakt verbinding met de database."""
        try:
            # Verbind met de database via mysql.connector
            self._conn = mysql.connector.connect(
                host=self._host,
                user=self._user,
                password=self._password,
                database=self._database
            )
            self._cursor = self._conn.cursor()
            print("Verbonden met database.")
        except mysql.connector.Error as err:
            print(f"Fout bij verbinden met database: {err}")

    def toon_locaties(self):
        """Toont alle locaties met hun wachttijden."""
        try:
            # Query om locaties op te halen uit de tabel
            self._cursor.execute("SELECT locatie_id, naam, wachttijd FROM Locatie")

            print("\nBeschikbare locaties in de database:\n")
            for (locatie_id, naam, wachttijd) in self._cursor.fetchall():
                print(f"{locatie_id}: {naam} (wachttijd: {wachttijd} minuten)")
        except mysql.connector.Error as err:
            print(f"Fout bij ophalen van data: {err}")
    
    def get_locaties(self):
        """Alias voor toon_locaties(), voor compatibiliteit met oude code."""
        self.toon_locaties()

def voeg_reservering_toe(self, attractie, tijdslot):
    """Voegt een reservering toe voor een attractie en tijdslot."""
    try:
        # Insert-query om een nieuwe reservering op te slaan
        query = "INSERT INTO Reservering (attractie, tijdslot) VALUES (%s, %s)"
        self._cursor.execute(query, (attractie, tijdslot))
        self._conn.commit()
        print(f"Reservering toegevoegd: {attractie} om {tijdslot}")
    except mysql.connector.Error as err:
        print(f"Fout bij toevoegen reservering: {err}")
