📌 Beskrivning

Det här projektet är en enkel Python-applikation som hanterar banktransaktioner och dokument. Applikationen är designad för att demonstrera grundläggande programmeringsprinciper, hantering av data och tester med hjälp av pytest.

📂 Projektstruktur

📦 bank_project
 ┣ 📜 main.py          # Huvudprogrammet
 ┣ 📜 utils.py         # Hjälpfunktioner för kontohantering
 ┣ 📜 api.py           # API-integration för valutakonvertering
 ┣ 📜 db_handler.py    # Hantering av kontodata
 ┣ 📜 requirements.txt # Lista över nödvändiga bibliotek
 ┣ 📜 .gitignore       # Ignorera filer som .venv och CSV-filer
 ┣ 📦 tests/           # Enhetstester
 ┃ ┣ 📜 test_bank.py   # Testfall för bankfunktioner
 ┃ ┗ 📜 test_api.py    # Testfall för API-funktioner
 ┗ 📦 data/            # Datahantering
   ┗ 📜 accounts.csv   # Lagring av konton

🛠️ Installation

Följ dessa steg för att installera och köra projektet:

1️⃣ Klona projektet

git clone https://github.com/ditt-anvandarnamn/bank_project.git
cd bank_project

2️⃣ Skapa och aktivera en virtuell miljö

📌 Rekommenderas för att hantera beroenden utan att påverka andra Python-projekt.

# Skapa en virtuell miljö
python -m venv venv

# Aktivera den:
# För Windows
venv\Scripts\activate

# För Mac/Linux
source venv/bin/activate

3️⃣ Installera beroenden

pip install -r requirements.txt

🚀 Användning

Starta programmet genom att köra:

python main.py

När programmet körs visas en meny:

Meny:
1. Skapa konto
2. Lista alla konton
3. Insättning
4. Uttag
5. Sök efter ett konto
6. Valutakonvertering
7. Ta bort ett konto
8. Avsluta

Användare kan navigera genom menyn genom att ange motsvarande nummer.

🎯 Funktioner

Skapa konto
Lista konton
Insättning
Uttag
Sök efter konton
Valutakonvertering

🛠️ Teknologier och bibliotek
Projektet använder följande teknologier och Python-bibliotek:

Python 3.9+
Pandas – För att hantera CSV-filer
hashlib – För att säkra lösenord med SHA-256
requests – För att hantera valutakonvertering (om API används)
pytest – För enhetstestning

📋 Kriterier för: Projekt kurs avancerad Python

A (Säker programmering): Lösenord hashas med SHA-256 i utils.py.
B (Avancerad datahantering): Använder Pandas för att hantera kontodata i db_handler.py.
C (API-integration): Hämtar valutakurser från ett API i api.py.
G (Filhantering): Lagring och laddning av kontodata i db_handler.py.
F (Enhetstestning): Använder pytest för att testa funktionerna.
E (Automatisering): Filhantering och API-integrering automatiserar bankfunktionerna.

📝 Att göra / Möjliga förbättringar

- Hasha lösenord med salt och ha fler lösenord i programmet för att kunna t.ex. göra insättningar och uttag.
- Spara data i en riktig och säkrare databas med användning av SQLLite
- Webbapplikation med Django eller Flask.

🤝 Bidrag

Om du vill bidra till projektet, gör en fork av repositoryt och skicka en pull request!
📩 Kontakt: github sabrinarybak / mail sabrina.rybak@outlook.com