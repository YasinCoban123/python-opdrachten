grootte = 10

print("   ", end="")  
for i in range(1, grootte + 1):
    print(f"{i:3}", end=" ")  # Print de bovenste nummers (nummers 1 tot 10)
print()  # Ga naar de volgende regel

# Loop door elke rij
for i in range(1, grootte + 1):
    print(f"{i:2} ", end="") 
    
    for j in range(1, grootte + 1):
        print(f"{i * j:3}", end=" ")  
    print()  # Ga naar de volgende rij
