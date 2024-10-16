def is_valid_password(password):
    # set van vereiste symbolen (alleen deze zijn toegestaan)
    vereiste_symbolen = {'*', '@', '!', '?'}

    # sets om tekens te sorteren
    digits = set('0123456789')
    lowercase = set('abcdefghijklmnopqrstuvwxyz')
    uppercase = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    # wachtwoord naar set converteren
    wachtwoord_set = set(password)
    
    # lengte controleren van wachtwoord
    if len(password) < 8 or len(password) > 20:
        return False
    
    # controleren op ongeldige symbolen, alleen de symbolen van required_symbols zijn toegestaan.
    if not wachtwoord_set <= digits | lowercase | uppercase | vereiste_symbolen:
        return False
    
    # controleer of de wachtwoord aan de vereisen toe doet.
    if (wachtwoord_set & digits) and (wachtwoord_set & lowercase) and (wachtwoord_set & uppercase) and (wachtwoord_set & vereiste_symbolen):
        return True
    else:
        return False

def main():
    attempts = 3  # max aantal pogingen
    
    while attempts > 0:
        password = input("Password: ").strip()
        
        if is_valid_password(password):
            print("Password is valid")
            break
        else:
            print("Password is invalid")
            attempts -= 1
    
    if attempts == 0:
        print("Maximum attempts reached. Access denied.")

# programma runnen
if __name__ == "__main__":
    main()
