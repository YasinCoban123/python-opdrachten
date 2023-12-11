# Vraag de gebruiker om hun leeftijd
leeftijd = float(input("Voer je leeftijd in: "))

# Controleer of de gebruiker al mag beginnen met rijlessen
minimum_leeftijd = 16.5

if leeftijd >= minimum_leeftijd:
    print("Je mag beginnen met rijlessen!")
else:
    print("Je moet nog wachten om met rijlessen te beginnen.")
