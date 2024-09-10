# Stemproces
stemmen_dominique = 0
stemmen_zacharia = 0

# Welkomstbericht
print("Welkom bij de verkiezingen!")

while True:
    print("\nKies een kandidaat om op te stemmen:")
    print("1. Dominique")
    print("2. Zacharia")
    print("0. Stoppen of uitslag opvragen")

    keuze = input("Voer het nummer van de kandidaat in: ")

    if keuze == "0":
        break
    elif keuze == "UITSLAG":
        print("Uitslag van de verkiezingen:")
        print("Dominique:", stemmen_dominique, "stemmen")
        print("Zacharia:", stemmen_zacharia, "stemmen")
        continue

    try:
        keuze = int(keuze)
        if keuze == 1:
            stemmen_dominique += 1
            print("U heeft gestemd op Dominique!")
        elif keuze == 2:
            stemmen_zacharia += 1
            print("U heeft gestemd op Zacharia!")
        else:
            print("Ongeldige keuze! Probeer opnieuw.")
    except ValueError:
        print("Ongeldige keuze! Probeer opnieuw.")

print("Het stemproces is beëindigd.")

# Bepaal de winnaar
if stemmen_dominique > stemmen_zacharia:
    winnaar = "Dominique"
elif stemmen_dominique < stemmen_zacharia:
    winnaar = "Zacharia"
else:
    winnaar = "Gelijkspel"

print("De winnaar van de verkiezingen is:", winnaar)

print("Bedankt voor uw deelname aan de verkiezingen!")
