import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Mistry123!",
        database="LSM_treintje"
    )

    cursor = conn.cursor()

    cursor.execute("SELECT locatie_id, naam, wachttijd FROM Locatie")

    print("Beschikbare locaties in de database:\n")
    for (locatie_id, naam, wachttijd) in cursor.fetchall():
        print(f"{locatie_id}: {naam} (wachttijd: {wachttijd} minuten)")

except mysql.connector.Error as err:
    print(f"Fout bij verbinden met database: {err}")

finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
