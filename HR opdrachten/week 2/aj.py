def classify_triangle(sides_input):
    sides = sides_input.replace(" ", "").split(",")

    a = int(sides[0].split("=")[1])
    b = int(sides[1].split("=")[1])
    c = int(sides[2].split("=")[1])

    if a == b == c:
        return "Equilateral triangle"
    elif a == b or b == c or a == c:
        return "Isosceles triangle"
    else:
        return "Scalene triangle"

sides_input = input("Sides: ")
result = classify_triangle(sides_input)
print(result)
