# Definieer een functie om twee getallen met elkaar te vermenigvuldigen
def vermenigvuldigen(a, b):
    return a * b

# Vraag input voor de twee getallen
getal1 = float(input("Voer het eerste getal in om te vermenigvuldigen: "))
getal2 = float(input("Voer het tweede getal in vermenigvuldigen: "))

# Roep de vermenigvuldigen functie aan en print het resultaat
resultaat = vermenigvuldigen(getal1, getal2)
print("Het resultaat is:", resultaat)
