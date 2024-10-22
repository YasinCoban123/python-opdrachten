contacts = []


def add_contact(name, phone_numbers, email):
    contact = {
        'name': name,
        'phone_numbers': phone_numbers,
        'email': email
    }
    contacts.append(contact)


def search_contacts(keyword):
    return list(filter(lambda c: keyword.lower() in c['email'].lower(), contacts))


def delete_contact(name):
    contact_found = False  # Vlag om bij te houden of we het contact vinden

    for contact in contacts:
        if contact['name'].lower() == name.lower():
            contacts.remove(contact)  # Verwijder het contact
            contact_found = True  # Contact is gevonden en verwijderd
            break

    # Feedback voor de gebruiker:
    if contact_found:
        print(f"Contact '{name}' deleted successfully.")
    else:
        print(f"Contact '{name}' not found.")


def update_contact(name, phone_numbers, email):
    # Validatie: controleer of de telefoonnummers en e-mail niet leeg zijn
    if not phone_numbers or not email:
        print("Phone numbers and email cannot be empty.")
        return  # Stop de functie zonder te updaten

    for contact in contacts:
        if contact['name'].lower() == name.lower():
            contact['phone_numbers'] = phone_numbers  # Updaten van de telefoonnummers (correcte variabele)
            contact['email'] = email  # Updaten van het e-mailadres
            print(f"Contact '{name}' updated successfully.")  # Succesmelding
            break
    else:
        print(f"Contact '{name}' not found.")  # Als de naam niet bestaat


def main():
    # Vooraf gedefinieerde contacten toevoegen
    add_contact("John Doe", ["1234567890", "9876543210"], "john@example.com")
    add_contact("Jane Smith", ["5555555555"], "jane@example.com")
    add_contact("Bob Johnson", ["1111111111", "2222222222", "3333333333"], "bob@example.com")

    # Zoeken naar een contact
    search_term = input("Enter a name to search: ")
    search_results = search_contacts(search_term)

    if search_results:
        print("Search Results:")
        for contact in search_results:
            print(f"Name: {contact['name']}")
            print("Phone Numbers:", ', '.join(contact['phone_numbers']))
            print(f"Email: {contact['email']}")
    else:
        print("No matching contacts found.")

    # Verwijderen van een contact
    contact_name = input("Enter the name of the contact to delete: ")
    delete_contact(contact_name)

    # Bijwerken van een contact
    update_name = input("Enter the name of the contact to update: ")
    update_phone_numbers = input("Enter the new phone numbers (separated by commas): ").split(",")
    update_email = input("Enter the new email address: ")
    update_contact(update_name, update_phone_numbers, update_email)


# Het hoofdprogramma starten
main()
