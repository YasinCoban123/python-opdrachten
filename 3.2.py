# Vraag de gebruiker om een getal
getal = int(input("Voer een getal in: "))

# Bereken de faculteit van het getal
faculteit = 1

for i in range(1, getal + 1):
    faculteit *= i

# Print de faculteit
print("De faculteit van", getal, "is", faculteit)