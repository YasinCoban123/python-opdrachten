# Vraag de score van speler 1
score_speler1 = int(input("Voer de score van Lebron in: "))

# Vraag de score van speler 2
score_speler2 = int(input("Voer de score van Murat in: "))

# Vergelijk de scores en bepaal wie er heeft gewonnen of dat er gelijkspel is
if score_speler1 > score_speler2:
    print("Lebron heeft gewonnen!")
elif score_speler2 > score_speler1:
    print("Murat heeft gewonnen!")
else:
    print("Het is een gelijkspel!")
