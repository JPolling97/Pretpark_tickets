import os
from pathlib import Path

def boekhouding():

    active = True

    while active:
        antwoord  = input("""Wat wil u weten?"
                          Aantal bonnen van -datum-:           toets 1
                          Aantal bonnen in totaal:             toets 2
                          Open de map met bonnen van -datum-:  toets 3
                          Open bon met boncode:                toets 4
                          Terug naar het hoofdmenu:            toets 5 """)
        if antwoord == "1":
            datum = input("Vul de datum in waarvan u het aantal bonnen wil weten: (DD-MM-JJJJ) ")
            map = f"Bonnen {datum}"
            folder_path = f'Bonnen/{map}'
            if os.path.isdir(folder_path):
                file_count = len([f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))])
                print(f"Er zijn {file_count} bonnen gemaakt op {datum}.")
            else:
                print(f"Error. Map 'Bonnen {datum}' bestaat niet.")
        elif antwoord == "2":
            directory = Path("Bonnen")
            file_count = len([f for f in directory.rglob('*') if f.is_file()])
            print(f"Er zijn in totaal {file_count} bonnen bekend in het systeem.")
        elif antwoord == "3":
            datum = input("Van welke datum wil u de bonnen inzien? Vul in als DD-MM-JJJJ. ")
            folder_path = fr"C:\Github_Workspace\Practice-project\pretpark_tickets\Bonnen\Bonnen {datum}"
            if os.path.exists(folder_path):
                os.startfile(folder_path)
            else:
                print(f"Error. Map 'Bonnen {datum}' bestaat niet.")
        elif antwoord == "4":
            datum = input("Van welke datum is de bon die u wil openen? Vul in als 'DD-MM-JJJJ. ")
            folder_path = fr"C:\Github_Workspace\Practice-project\pretpark_tickets\Bonnen\Bonnen {datum}"
            files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
            print(" ")
            print(f"Gevonden bonnen in Bonnen {datum}")
            for i in files:
                print(i)
            print("")
            code = input("Welke bon wil u openen? Vul in als '00-00-00' ")
            file_name = f"Bon {code}.txt"
            file_path = fr"C:\Github_Workspace\Practice-project\pretpark_tickets\Bonnen\Bonnen {datum}\{file_name}"
            if os.path.exists(file_path):
                os.system(f'notepad "{file_path}"')
            else:
                print(f"Error. {file_name} bestaat niet.")

        elif antwoord == "5":
            active = False
        else:
            print("Error. Selecteer functie 1-5")

