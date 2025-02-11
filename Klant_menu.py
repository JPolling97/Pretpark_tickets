def klant_menu(prijzen):
    bon = []
    totaal = 0
    active = True

    while active:
        aantal = int(input("Welkom bij het pretpark, hoeveel tickets wilt u bestellen? "))
        for i in range(aantal): #voor elk kaartje wordt gevraagd om leeftijd, vervolgens worden de leeftijd en bijbehorende prijs toegevoegd aan de list 'bon'
            leeftijd = int(input("Wat is uw leeftijd? "))
            if leeftijd < 4:
                print(f"Een kaartje voor jonge kinderen (0-3 jaar) kost €{prijzen["jong kind"]}.")
                print(" ")
                totaal += prijzen["jong kind"]
                bon.append(f"entree jong kind_________ €{prijzen["jong kind"]}")
            elif leeftijd > 3 and leeftijd < 19:
                print(f"Een kaartje voor kinderen (4-18 jaar) kost €{prijzen["kind"]}.")
                print(" ")
                totaal += prijzen["kind"]
                bon.append(f"entree kind______________ €{prijzen["kind"]}")
            elif leeftijd > 18 and leeftijd < 65:
                print(f"Een kaartje voor volwassenen (19-65 jaar) kost €{prijzen["volwassene"]}.")
                print(" ")
                totaal += prijzen["volwassene"]
                bon.append(f"entree volwassene________ €{prijzen["volwassene"]}")
            elif leeftijd > 64:
                print(f"Een kaartje voor senioren (65+ jaar) kost €{prijzen["senior"]}.")
                print(" ")
                totaal += prijzen["senior"]
                bon.append(f"entree senior____________ €{prijzen["senior"]}")
        print(f"Uw totaalbedrag is €{totaal} excl. BTW.")

        #hier wordt gevraagd of de klant een parkeerticket wil toevoegen. Bij ja wordt deze met prijs toegevoegd aan de list 'bon'
        parkeren = input("Wilt u ook een parkeerticket kopen voor €7,50? j/n")
        if parkeren == "j":
            totaal += prijzen["parkeren"]
            bon.append(f"parkeerticket____________ €{prijzen["parkeren"]}")
            print(" ")
            print(f"Uw totaalbedrag is €{totaal} excl BTW.")
        elif parkeren == "n":
            print(" ")
            print(f"Uw totaalbedrag is €{totaal} excl BTW.")

        #BTW berekening
        btw1 = totaal * prijzen["btw"]
        btw = round(btw1, 2)
        totaal_incl = round(totaal + btw1, 2)
        totaal1 = round(totaal, 2)

        #als de klant een bon wil wordt de list 'bon'geprint, gevolgd door de uitkomsten van de BTW berekeningen
        antwoord = input("Wilt u een kassabon? j/n")
        if antwoord == "j":
            for i in bon:
                print(i)
            print(f"totaal___________________ €{totaal1} excl. BTW")
            print(f"BTW______________________ €{btw}")
            print("  ")
            print(f"totaal___________________ €{totaal_incl} incl. BTW")
            print(" ")
            print("Bedankt voor uw bestelling en veel plezier in ons park!")
            print(" ")
        elif antwoord == "n":
            print("Bedankt voor uw bestelling en veel plezier in ons park!")
            print(" ")

        #hier kan de werknemer kiezen of deze in het klantmenu wil blijven of terug wil gaan naar het hoofdmenu
        doorgaan = input("Wilt u nog een bestelling plaatsen? j/n")
        if doorgaan == "j":
            continue
        elif doorgaan == "n":
            active = False