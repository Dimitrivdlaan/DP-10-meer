# DP-10-meer
DP10 – User Story 5: Reserveringen Beheren

Project: Startcode Treintje
Opleiding: HBO-ICT – Windesheim
Auteur: Bismark Owusu-Ansah & team

📘 Inleiding

Dit onderdeel is ontwikkeld voor DP10 – Realisatie GUI en implementeert User Story 5:

“Als bezoeker wil ik via de GUI mijn reserveringen kunnen bekijken, bevestigen of annuleren, zodat ik mijn treinritten kan beheren.”

De module integreert rechtstreeks met de bestaande PyQt GUI (Startcode Treintje) en maakt gebruik van een MySQL-database (geleverd via dp10_start_db_bc2b.sql).

⚙️ Functies

✅ Reserveringen opzoeken: invoer van een QR-ID om alle reserveringen van die gebruiker te tonen
✅ Bevestigen: toevoegen van een nieuwe reservering aan de database
✅ Annuleren: verwijderen van een bestaande reservering
✅ Treinenlijst: toont actuele treinen met vertrek- en aankomstlocaties
✅ Database-interactie: via DAO/Service-laag (MySQL connector)
✅ Feedback: bevestiging en foutmeldingen via dialoogvensters

Technische details

Architectuur:

Model: dataclasses voor Trein, Locatie, Reservering

DAO: SQL-queries (SELECT, INSERT, DELETE)

Service: logica en validatie

Controller: gekoppeld aan PyQt-UI

UI: reserveringen_scherm.py – scherm in Startcode-stijl

Belangrijk:

Idempotente acties → dubbele reservering wordt voorkomen

Foutafhandeling met QMessageBox

Losgekoppelde logica → makkelijk te testen

🧪 Testen
Test	Actie	Verwacht resultaat
TC-05-1	QR 101 zoeken	Alleen reserveringen van 101 zichtbaar
TC-05-2	Trein bevestigen	Nieuwe reservering toegevoegd
TC-05-3	Reservering annuleren	Reservering verwijderd
TC-05-4	Verkeerde QR-ID	Foutmelding “Voer een geldige QR ID in”
TC-05-5	MySQL uitgeschakeld	Foutmelding “Geen verbinding met database”


