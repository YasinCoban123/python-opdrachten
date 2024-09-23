import re

def geldige_kenteken(kenteken):
    patronen = [
        r'^[A-Z]{2}-\d{2}-\d{2}$',  # XX-99-99
        r'^\d{2}-\d{2}-[A-Z]{2}$',  # 99-99-XX
        r'^\d{2}-[A-Z]{2}-\d{2}$',  # 99-XX-99
        r'^[A-Z]{2}-\d{2}-[A-Z]{2}$',  # XX-99-XX
        r'^[A-Z]{2}-[A-Z]{2}-\d{2}$',  # XX-XX-99
        r'^\d{2}-[A-Z]{2}-[A-Z]{2}$',  # 99-XX-XX
        r'^\d{2}-[A-Z]{3}-\d$',  # 99-XXX-9
        r'^\d-[A-Z]{3}-\d{2}$',  # 9-XXX-99
        r'^[A-Z]{2}-\d{3}-[A-Z]$',  # XX-999-X
        r'^[A-Z]-\d{3}-[A-Z]{2}$',  # X-999-XX
        r'^[A-Z]{3}-\d{2}-[A-Z]$',  # XXX-99-X
        r'^\d-[A-Z]{2}-\d{3}$'  # 9-XX-999
    ]
    
    for patroon in patronen:
        if re.match(patroon, kenteken):
            return "Valid"
    
    return "Invalid"

# Test cases
print(geldige_kenteken("A-149-HH")) 
print(geldige_kenteken("149-A-HH"))  
