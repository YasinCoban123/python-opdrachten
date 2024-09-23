def mens_naar_honden_jaren(mens_jaren):
    if mens_jaren < 0:
        return "Only positive numbers are allowed"
    
    if mens_jaren <= 2:
        honden_jaren = mens_jaren * 10.5
    else:
        honden_jaren = 2 * 10.5 + (mens_jaren - 2) * 4
    
    return int(honden_jaren)

# Test cases
print(mens_naar_honden_jaren(1))
print(mens_naar_honden_jaren(2))  
print(mens_naar_honden_jaren(4))   
print(mens_naar_honden_jaren(5))   
print(mens_naar_honden_jaren(-1)) 
