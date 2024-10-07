binary_string = input("Voer een binair nummer in: ")

decimaal_nummer = 0

macht = 0

for digit in binary_string[::-1]:
    if digit == '1':
        decimaal_nummer += 2 ** macht 
    macht += 1 

print(f"Het decimale equivalent van binaire {binary_string} is {decimaal_nummer}")
