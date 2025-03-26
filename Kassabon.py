import time
from datetime import date
from datetime import datetime
import os

def kassabon(bon, totaal, prijslijst, bon_prijzen, mapnaam):
    # BTW berekening
    btw = totaal * prijslijst["6: btw          "]
    totaal_incl = totaal + btw

    #instellen datum en tijd
    now = datetime.now()
    tijd = now.strftime("%H-%M-%S")
    today1 = date.today()
    today = today1.strftime("%d-%m-%Y")

    #namen bon en mapje
    bon_titel = f"Bon {tijd}.txt"
    folder_name = f"Bonnen/Bonnen {today}"
    paths = []
    os.makedirs(folder_name, exist_ok=True)
    paths.append(os.path.join(folder_name, bon_titel))
    paths.append(os.path.join(mapnaam, bon_titel))

    for i in paths:
        with open(i, "w") as f:
            f.write(tijd)
            f.write("\n")
            f.write("  ")
            f.write("\n")
            for i in range(len(bon)):
                f.write(bon[i])
                f.write(bon_prijzen[i])
                f.write("\n")
            f.write("  ")
            f.write("\n")
            f.write(f"Totaal__________________ €{"%1.2f" % totaal} excl. BTW")
            f.write("\n")
            f.write(f"BTW______________________ €{"%1.2f" % btw}")
            f.write("\n")
            f.write("  ")
            f.write("\n")
            f.write(f"Totaal__________________ €{"%1.2f" % totaal_incl} incl. BTW")
            f.write("\n")
            f.write(" ")
            f.write("\n")
            f.write("Bedankt voor uw bestelling en veel plezier in ons park!")
