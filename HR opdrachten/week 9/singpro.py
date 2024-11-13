class Product:
    def __init__(self, name, amount, price):
        self.name = name  # Naam van het product
        self.amount = amount  # Aantal items op voorraad
        self.price = price  # Standaardprijs per product

    def get_price(self, quantity):
        """Bereken de totale kosten, inclusief eventuele korting op basis van de hoeveelheid."""
        if quantity < 10:
            total_price = self.price * quantity  # Geen korting voor minder dan 10 items
        elif 10 <= quantity < 100:
            total_price = self.price * quantity * 0.90  # 10% korting voor 10 tot 99 items
        else:
            total_price = self.price * quantity * 0.80  # 20% korting voor 100 items of meer

        return total_price

    def make_purchase(self, quantity):
        """Verlaag de voorraad op basis van het aantal gekochte items."""
        if quantity <= self.amount:
            self.amount -= quantity
            print(f"Aankoop succesvol! {quantity} {self.name}(s) gekocht.")
            print(f"Overige voorraad: {self.amount}")
        else:
            print(f"Niet genoeg voorraad. Beschikbare voorraad: {self.amount}")

# Voorbeeld van het maken van een product en het gebruiken van de klasse
if __name__ == "__main__":
    # Maak een productobject aan
    product = Product("Laptop", 50, 1000)

    # Bereken de prijs voor een klant die 15 items wil kopen (met korting)
    print(f"Totaalprijs voor 15 items: {product.get_price(15)}")

    # Maak een aankoop van 20 items
    product.make_purchase(20)

    # Bereken de prijs voor een klant die 120 items wil kopen (met een grotere korting)
    print(f"Totaalprijs voor 120 items: {product.get_price(120)}")

    # Maak een aankoop van 30 items
    product.make_purchase(30)

    # Controleer de resterende voorraad
    print(f"Resterende voorraad na aankopen: {product.amount}")




