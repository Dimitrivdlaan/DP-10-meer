import mysql.connector

class DatabaseConnection:
    def __init__(self): 
        self._host = host
        self._user = user
        self._password = password
        self._database = database
        self._conn = None
        self._cursor = None

    def open_verbinding(self):
        try:
            self._conn = mysql.connector.connect(
                host=self._host,
                user=self._user,
                password=self._password,
                database=self._database
            )
            self._cursor = self._conn.cursor()
            print("Verbinding met database succesvol.")

        except mysql.connector.Error as err:
            print(f"Fout bij verbinden met database: {err}")

    def toon_locaties(self):
        try:  
            self._cursor.execute("SELECT locatie_id, naam, wachttijd FROM Locatie")
            print("Beschikbare locaties in de database:\n")
            for (locatie_id, naam, wachttijd) in self._cursor.fetchall():
                print(f"{locatie_id}: {naam} (wachttijd: {wachttijd} minuten)")

        except mysql.connector.Error as err:
            print(f"Fout bij ophalen van locaties: {err}")

    def voeg_reservering_toe(self,attractie, tijdslot):
        try:
            query = "INSERT INTO Reservering (attractie, tijdslot) VALUES (%s, %s)"
            self._cursor.execute(query, (attractie, tijdslot))
            self._conn.commit()
            print(f"Reservering succesvol toegevoegd: {attractie} om {tijdslot}.")
        except mysql.connector.Error as err:
            print(f"Fout bij toevoegen van reservering: {err}")

    def sluit_verbinding(self):
        if self._conn and self._conn.is_connected():
             self._cursor.close()
             self._conn.close()
             print("Verbinding met database gesloten.")
