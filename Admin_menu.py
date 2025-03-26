import json

def admin_menu():

    active = True

    while active:
        with open("prijzen.json", "r") as f:
            prijslijst = json.load(f)
        print("Huidige prijslijst:")
        for i in prijslijst:
            print(i, prijslijst[i])
        print("")

        antwoord = input("Van welke categorie wilt u de prijs aanpassen? ")
        if antwoord == "1":
            prijslijst["1: jong kind    "] = float(input("Vul de nieuwe prijs in: "))
        elif antwoord == "2":
            prijslijst["2: kind         "] = float(input("Vul de nieuwe prijs in: "))
        elif antwoord == "3":
            prijslijst["3: volwassene   "] = float(input("Vul de nieuwe prijs in: "))
        elif antwoord == "4":
            prijslijst["4: senior       "] = float(input("Vul de nieuwe prijs in: "))
        elif antwoord == "5":
            prijslijst["5: parkeren     "] = float(input("Vul de nieuwe prijs in: "))
        elif antwoord == "6":
            prijslijst["6: btw          "] = float(input("Vul de nieuwe prijs in: "))
        elif antwoord == "7":
            prijslijst["7: groepskorting"] = float(input("Vul de nieuwe prijs in: "))
        else:
            print("Error, kies een bestaande categorie")
        with open("prijzen.json", "w") as f:
            json.dump(prijslijst, f, indent=4)



        antwoord1 = input("Wilt u nog een prijs aanpassen? j/n ")
        if antwoord1 == "j":
            continue
        elif antwoord1 == "n":
            active = False
