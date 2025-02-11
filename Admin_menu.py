def admin_menu(prijzen):

    active = True

    while active:
        print(prijzen)
        antwoord = input("Van welke categorie wilt u de prijs aanpassen? ")
        if antwoord in prijzen:
            prijzen[antwoord] = float(input("Vul de nieuwe prijs in: "))
            print(f"prijslijst: {prijzen}")
            print(" ")
            antwoord1 = input("Wilt u nog een prijs aanpassen? j/n")
            if antwoord1 == "j":
                continue
            elif antwoord == "n":
                active = False
            return prijzen
        else:
            print("Error, kies een bestaande categorie")