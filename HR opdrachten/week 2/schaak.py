def schaak_vierkant_kleur(position):

    column_letter = position[0].upper()  
    row_number = int(position[1])        
    
    column_number = ord(column_letter) - ord('A') + 1
    
    total = column_number + row_number
    
    if total % 2 == 0:
        return "White"
    else:
        return "Black"


print(schaak_vierkant_kleur("D5")) 
print(schaak_vierkant_kleur("A1")) 