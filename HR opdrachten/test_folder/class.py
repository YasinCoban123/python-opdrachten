# Definieer een klasse voor een Student
class Student:
    def __init__(self, naam, leeftijd, studie, cijfer_gemiddelde):
        self.naam = naam
        self.leeftijd = leeftijd
        self.studie = studie
        self.cijfer_gemiddelde = cijfer_gemiddelde

    def introduceer(self):
        return f"Hallo, ik ben {self.naam}, ik ben {self.leeftijd} jaar oud en studeer {self.studie}."

# Maak een object (instantie) van de klasse Student
student1 = Student("Sophie", 21, "Informatica", 8.3)

# Roep de introduceer-methode aan
print(student1.introduceer())  # Output: Hallo, ik ben Sophie, ik ben 21 jaar oud en studeer Informatica.

# Een class in Python is een sjabloon
# voor het maken van objecten. 
# Een klasse definieert de eigenschappen (attributen) 
# en gedragingen (methoden) die bij dat object horen.

# In het voorbeeld: De class Student
# heeft een speciale methode genaamd __init__, de constructor.
# Deze methode wordt automatisch aangeroepen
# wanneer je een nieuw object maakt,
# en stelt de waarden van de eigenschappen
# (naam, leeftijd, studie, cijfer_gemiddelde) in.

# self verwijst naar de huidige instantie van de klasse.
# Hiermee kun je binnen de klasse toegang krijgen
# tot de attributen en methoden.

# De introduceer-methode geeft een korte introductie
# terug over de student.