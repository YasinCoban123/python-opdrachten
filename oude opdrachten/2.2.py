hobbylijst = []

for _ in range(3):
    hobby = input("Voer een hobby in: ")
    hobbylijst.append(hobby)

print("Hobby's:")
for hobby in hobbylijst:
    print(hobby)