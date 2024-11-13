''' de variabele __name__ Is iets 
In Python is __name__ een speciale ingebouwde variabele die 
aangeeft of een script direct wordt uitgevoerd 
of dat het als module wordt geïmporteerd in een ander script.

Als je een script direct uitvoert, krijgt __name__ de waarde "__main__". 
Dit betekent dat het script als het hoofdprogramma draait.
Als het script echter wordt geïmporteerd in een ander script, 
dan krijgt __name__ de waarde van de naam van het bestand (zonder .py).
'''

def greet():
    print("Hello from the function!")

if __name__ == "__main__":
    print("This script is being run directly")
    greet()
else:
    print("This script is being imported as a module")



