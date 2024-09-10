# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.


# name = "Yasin"
# age = 18
# a = '10 December '
# b = '2023'
# c = a + b
#a += b zelde als a = a + b

# print(c)
# print("hallo wereld")
# input("Goeie morgen, wat is je naam")
# input("Mijn naam is Yasin, Ik ben 18 jaar oud")
# input("Mijn naam is " + name + ", Ik ben " + str(age) + " jaar oud")


# waarheid = False

# if waarheid:
#     print("De voorwaarde is waar.")
# else:
#     print("De voorwaarde is onwaar.")

# getallen = [1, 2, 3, 4, 5]

# for nummer in getallen:
#     print(nummer)


# automerken = ["Toyota", "Ford", "Honda", "BMW", "Tesla"]
# gezocht_merk = "Honda"

# if gezocht_merk in automerken:
#     print(f"{gezocht_merk} is beschikbaar in de lijst van automerken.")
# else:
#     print(f"{gezocht_merk} is niet beschikbaar in de lijst van automerken.")


def galgje():
    woord = input("Speler 1, voer een woord in: ").lower()
    geraden_letters = set()
    fouten = 0
    max_fouten = 9
    
    while fouten < max_fouten:
        gok = input("Speler 2, raad een letter: ").lower()

        if gok in geraden_letters:
            print("Je hebt deze letter al geraden. Probeer opnieuw.")
            continue

        geraden_letters.add(gok)

        if gok in woord:
            print("Goed geraden!")
        else:
            fouten += 1
            print(f"Fout! Je hebt {fouten} van de {max_fouten} fouten gemaakt.")

        weergave = ''.join(letter if letter in geraden_letters else '_' for letter in woord)
        print("Woord: " + weergave)

        if set(woord) == geraden_letters:
            print("Gefeliciteerd! Je hebt het woord geraden.")
            break

    if fouten >= max_fouten:
        print("Helaas, je hebt het maximaal aantal fouten bereikt. Het woord was:", woord)

galgje()
