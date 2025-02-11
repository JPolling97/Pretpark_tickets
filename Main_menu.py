import sys
from Klant_menu import klant_menu
from Admin_menu import admin_menu

active = True
prijzen = {"jong kind": 0 , "kind": 5, "volwassene": 10, "senior": 8, "parkeren": 7.50, "btw": 0.09}

while active:
    antwoord = input("""Hallo medewerker, welk systeem wil u gebruiken?
    Admin systeem:       toets '1'
    Kassa systeem:       toets '2'
    Programma afsluiten: toets '3'
""")

    if antwoord == "1":
        admin_menu(prijzen)
        print(" ")
        print("Dit zijn de nieuwe prijzen per categorie:")
        print(prijzen)
        print(" ")
    elif antwoord == "2":
        klant_menu(prijzen)
    elif antwoord == "3":
        sys.exit()