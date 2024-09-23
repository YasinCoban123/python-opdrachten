'''
feestdagen = {
    (1, 1): "Nieuwjaarsdag",
    (4, 27): "Koningsdag",
    (5, 5): "Bevrijdingsdag",
    (12, 5): "Sinterklaas",
    (12, 25): "Kerst",
    (12, 26): "Kerstdag"
}

def check_feestdagen(maand, dag):
    if (maand, dag) in feestdagen:
        print(feestdagen[(maand, dag)])
    else:
        print("Geen feestdag gevonden op de opgegeven datum.")

try:
    # Vraag om maand en dag in één invoer
    invoer = input("Voer de datum in ): ").strip()
    maand, dag = map(int, invoer.split())
    
    check_feestdagen(maand, dag)
except ValueError:
    print("Ongeldige invoer. Zorg ervoor dat je maand en dag correct invoert.")
    '''

feestdagen = {
    (1, 1): "Nieuwjaarsdag",
    (4, 27): "Koningsdag",
    (5, 5): "Bevrijdingsdag",
    (12, 5): "Sinterklaas",
    (12, 25): "Eerste Kerstdag",
    (12, 26): "Tweede Kerstdag"
}

def find_feestdagen():
    date_input = input("Date: ")

    try:
        date_parts = date_input.split(",")
        month = int(date_parts[0].split(":")[1].strip())
        day = int(date_parts[1].split(":")[1].strip())

        if (month, day) in feestdagen:
            print(feestdagen[(month, day)])
        else:
            print("No holiday found on given input")
    except (IndexError, ValueError):
        print("Invalid input format. Please provide input as 'Month: <month>, Day: <day>'")

find_feestdagen()

