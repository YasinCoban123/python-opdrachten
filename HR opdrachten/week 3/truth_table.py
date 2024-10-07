truth_waardes = [True, False]

print("AND")
for a in truth_waardes:
    for b in truth_waardes:
        result = a and b  
        print(f"{a} + {b} = {result}")

print()

print("OR")
for a in truth_waardes:
    for b in truth_waardes:
        result = a or b  
        print(f"{a} + {b} = {result}")
