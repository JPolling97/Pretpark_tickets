import sys
import json
from Klant_menu import klant_menu
from Admin_menu import admin_menu
from Boekhouding import boekhouding

active = True
#prijzen = {"1: jong kind    ": 0.00 , "2: kind         ": 5.00, "3: volwassene   ": 10.00, "4: senior       ": 8.00, "5: parkeren     ": 7.50, "6: btw          ": 0.09, "7: groepskorting": 5.00}
#with open("prijzen.json", "w") as f:
    #json.dump(prijzen, f)

while active:
    antwoord = input("""Hallo medewerker, welk systeem wil u gebruiken?
    Admin systeem:       toets '1'
    Kassa systeem:       toets '2'
    Boekhoud systeem:    toets '3'
    Programma afsluiten: toets '4'
""")

    if antwoord == "1":
        admin_menu()
    elif antwoord == "2":
        klant_menu()
    elif antwoord == "3":
        boekhouding()
    elif antwoord == "4":
        sys.exit()

