'''
Een lambda-functie is een korte manier om een kleine functie te schrijven in Python, 
zonder de functie een naam te geven. 
Ze zijn handig als je een eenvoudige functie maar één keer nodig hebt.
'''

# Lambda functie om twee getallen op te tellen
optellen = lambda x, y: x + y

print(optellen(3, 4))  # Output: 7

# Hieronder is de functie versie ervan dat hetzelfde doet
def optellen(x, y):
    return x + y

# Andere voorbeelden

# map() voorbeeld: verdubbel elk getal in een lijst.
getallen = [1, 2, 3]
verdubbeld = map(lambda x: x * 2, getallen)
print(list(verdubbeld))  # Output: [2, 4, 6]

# filter() voorbeeld: houd alleen even getallen.
getallen = [1, 2, 3, 4]
even = filter(lambda x: x % 2 == 0, getallen)
print(list(even))  # Output: [2, 4]
