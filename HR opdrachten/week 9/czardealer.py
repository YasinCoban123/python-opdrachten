# Stap 1 en Stap 2: Definieer de klassen Car en Customer

class Customer:
    def __init__(self, name):
        self.name = name

    def print(self):
        print(f"Naam: {self.name}")


class Car:
    def __init__(self, brand, model, color, price):
        self.brand = brand
        self.model = model
        self.color = color
        self.price = price
        self.sold = False
        self.sold_to = None  # Dit zal een Customer object bevatten wanneer de auto is verkocht

    def sell(self, customer):
        self.sold = True
        self.sold_to = customer

    def print(self):
        print(f"Merk: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Kleur: {self.color}")
        print(f"Prijs: {self.price}")
        if self.sold:
            print(f"Verkocht aan: {self.sold_to.name}")
        else:
            print("Nog niet verkocht")


# Stap 3: Definieer de klasse Motorcycle

class Motorcycle:
    def __init__(self, brand, model, color, price):
        self.brand = brand
        self.model = model
        self.color = color
        self.price = price
        self.sold = False
        self.sold_to = None  # Dit zal een Customer object bevatten wanneer de motor is verkocht

    def sell(self, customer):
        self.sold = True
        self.sold_to = customer

    def print(self):
        print(f"Merk: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Kleur: {self.color}")
        print(f"Prijs: {self.price}")
        if self.sold:
            print(f"Verkocht aan: {self.sold_to.name}")
        else:
            print("Nog niet verkocht")


# Voorbeeldgebruik binnen het main blok
if __name__ == "__main__":
    # Maak een Car object
    car1 = Car("BMW", "X5", "Zwart", 34899)
    car1.print()  # Print de details vóór de verkoop

    # Maak een Customer en verkoop de auto aan hen
    customer1 = Customer("John Doe")
    car1.sell(customer1)  # Verkoop de auto
    car1.print()  # Print de details na de verkoop

    print()  # Scheiding

    # Maak een Motorcycle object
    motorcycle1 = Motorcycle("Harley-Davidson", "Iron 883", "Matte Zwart", 9500)
    motorcycle1.print()  # Print de details vóór de verkoop
 
    # Maak een andere Customer en verkoop de motor aan hen
    customer2 = Customer("Jane Smith")
    motorcycle1.sell(customer2)  # Verkoop de motor
    motorcycle1.print()  # Print de details na de verkoop
