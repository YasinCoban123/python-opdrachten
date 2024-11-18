class PasswordManager:
    def __init__(self):
        # Initialiseer de lijst old_passwords
        self.old_passwords = []

    def get_password(self):
        # Retuen het huidige wachtwoord (laatste in de lijst),
        # of None als de lijst leeg is
        return self.old_passwords[-1] if self.old_passwords else None

    def set_password(self, new_password):
        # Controleer of het nieuwe wachtwoord anders is dan alle oude wachtwoorden
        if new_password not in self.old_passwords:
            self.old_passwords.append(new_password)  # Voeg het nieuwe wachtwoord toe aan de lijst
            print("Wachtwoord succesvol bijgewerkt.")
        else:
            print("Wachtwoord niet bijgewerkt. Het nieuwe wachtwoord komt overeen met een eerder wachtwoord.")

    def is_correct(self, password):
        # Controleer of het gegeven wachtwoord overeenkomt met het huidige wachtwoord
        return password == self.get_password()


# Voorbeeldgebruik:
pm = PasswordManager()
pm.set_password("wachtwoord123")  # Stel het eerste wachtwoord in
pm.set_password("wachtwoord123")  # Probeer hetzelfde wachtwoord opnieuw in te stellen
print(pm.get_password())          # Output: wachtwoord123
print(pm.is_correct("wachtwoord123"))  # Output: True
print(pm.is_correct("verkeerd"))      # Output: False
pm.set_password("nieuwwachtwoord456") # Stel een nieuw wachtwoord in
print(pm.get_password())              # Output: nieuwwachtwoord456