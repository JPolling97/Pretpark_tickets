from Genereer_ticket import selectie, parkeer_ticket_pdf
from Kassabon import kassabon
import os
import json


def klant_menu():
    with open("prijzen.json", "r") as f:
        prijslijst = json.load(f)
    bon = []
    bon_prijzen = []
    totaal = 0
    active = True

    while active:
        aantal = int(input("Welkom bij het pretpark, hoeveel tickets wilt u bestellen? "))
        # Create a new folder (if it doesn't exist)
        mapnaam = input("Naam: ")

        for i in range(aantal): #voor elk kaartje wordt gevraagd om leeftijd, vervolgens worden de leeftijd en bijbehorende prijs toegevoegd aan de list 'bon'
            leeftijd = int(input("Wat is uw leeftijd? "))
            if leeftijd < 4:
                prijs  = "%1.2f" % prijslijst["1: jong kind    "]
                print(f"Een kaartje voor jonge kinderen (0-3 jaar) kost €{prijs}.")
                totaal += prijslijst["1: jong kind    "]
                bon.append(f"Entree jong kind_________ €")
                bon_prijzen.append(prijs)
                selectie(leeftijd, mapnaam)
            elif leeftijd > 3 and leeftijd < 19:
                prijs = "%1.2f" % prijslijst["2: kind         "]
                print(f"Een kaartje voor kinderen (4-18 jaar) kost €{prijs}.")
                totaal += prijslijst["2: kind         "]
                bon.append(f"Entree kind______________ €")
                bon_prijzen.append(prijs)
                selectie(leeftijd, mapnaam)
            elif leeftijd > 18 and leeftijd < 65:
                prijs = "%1.2f" % prijslijst["3: volwassene   "]
                print(f"Een kaartje voor volwassenen (19-65 jaar) kost €{prijs}.")
                totaal += prijslijst["3: volwassene   "]
                bon.append(f"Entree volwassene_______ €")
                bon_prijzen.append(prijs)
                selectie(leeftijd, mapnaam)
            elif leeftijd > 64:
                prijs = "%1.2f" % prijslijst["4: senior       "]
                print(f"Een kaartje voor senioren (65+ jaar) kost €{prijs}.")
                totaal += prijslijst["4: senior       "]
                bon.append(f"Entree senior____________ €")
                bon_prijzen.append(prijs)
                selectie(leeftijd, mapnaam)
            print(" ")
            print(f"Uw totaal is €{"%1.2f" % totaal}")
            print(" ")

        if aantal > 4:
            prijs = "%1.2f" % prijslijst["7: groepskorting"]
            print(f"Bij bestelling van 5 of meer tickets krijgt u €{prijs} korting.")
            totaal -= prijslijst["7: groepskorting"]
            bon.append(f"Groepskorting___________ -€")
            bon_prijzen.append(prijs)

        #hier wordt gevraagd of de klant een parkeerticket wil toevoegen. Bij ja wordt deze met prijs toegevoegd aan de list 'bon'
        prijs = "%1.2f" % prijslijst["5: parkeren     "]
        parkeren = input(f"Wilt u ook een parkeerticket kopen voor €{prijs} j/n")
        if parkeren == "j":
            prijs = "%1.2f" % prijslijst["5: parkeren     "]
            totaal += prijslijst["5: parkeren     "]
            bon.append(f"Parkeerticket____________ €")
            bon_prijzen.append(prijs)
            parkeer_ticket_pdf(mapnaam)
            print(" ")
            print(f"Uw totaalbedrag is €{"%1.2f" % totaal} excl BTW.")
        elif parkeren == "n":
            print(" ")
            print(f"Uw totaalbedrag is €{"%1.2f" % totaal} excl BTW.")
        print(" ")

        #als de klant een bon wil wordt de list 'bon'geprint, gevolgd door de uitkomsten van de BTW berekeningen
        antwoord = input("Wilt u een kassabon? j/n")
        print(" ")
        if antwoord == "j":
            kassabon(bon, totaal, prijslijst, bon_prijzen, mapnaam)
        elif antwoord == "n":
            print("Bedankt voor uw bestelling en veel plezier in ons park!")
            print(" ")

        #hier kan de werknemer kiezen of deze in het klantmenu wil blijven of terug wil gaan naar het hoofdmenu
        doorgaan = input("Wilt u nog een bestelling plaatsen? j/n")
        if doorgaan == "j":
            continue
        elif doorgaan == "n":
            active = False
