# Aritmetische operators

# Optelling
a = 10
b = 5
print(a + b)  # 15

# Aftrekking
print(a - b)  # 5

# Vermenigvuldiging
print(a * b)  # 50

# Deling
print(a / b)  # 2.0

# Modulus (rest van de deling)
print(a % b)  # 0

# Machtsverheffing
print(a ** 2)  # 100

# Gehele deling (floor division)
print(a // 3)  # 3




# Vergelijkingsoperators

# Gelijk aan
print(a == b)  # False

# Niet gelijk aan
print(a != b)  # True

# Groter dan
print(a > b)  # True

# Kleiner dan
print(a < b)  # False

# Groter dan of gelijk aan
print(a >= b)  # True

# Kleiner dan of gelijk aan
print(a <= b)  # False




# Logische operators

# AND operator: beide condities moeten waar zijn
print(a > 5 and b < 10)  # True

# OR operator: een van de condities moet waar zijn
print(a > 15 or b < 10)  # True

# NOT operator: keert de waarde om
print(not(a > 15))  # True




# Toewijzingsoperators

# Eenvoudige toewijzing
c = 10  # c krijgt de waarde 10

# Samengestelde toewijzingen
c += 2  # Dit is hetzelfde als: c = c + 2
print(c)  # 12

c *= 3  # Dit is hetzelfde als: c = c * 3
print(c)  # 36

c -= 4  # Dit is hetzelfde als: c = c - 4
print(c)  # 32

c /= 8  # Dit is hetzelfde als: c = c / 8
print(c)  # 4.0




# Bitwise operators

x = 6  # binaire waarde: 110
y = 3  # binaire waarde: 011

# AND
print(x & y)  # 2 (binair: 010)

# OR
print(x | y)  # 7 (binair: 111)

# XOR
print(x ^ y)  # 5 (binair: 101)

# NOT (omkering van bits)
print(~x)  # -7 (omgekeerde bits van 110)

# Links schuiven (shift)
print(x << 1)  # 12 (binair: 1100)

# Rechts schuiven (shift)
print(x >> 1)  # 3 (binair: 011)




# Identiteitsoperators

d = [1, 2, 3]
e = d
f = [1, 2, 3]

# Is (zelfde object in het geheugen)
print(d is e)  # True

# Is not (verschillende objecten in het geheugen)
print(d is not f)  # True




# Lidmaatschapsoperators

lijst = [1, 2, 3, 4]

# In
print(3 in lijst)  # True

# Niet in
print(5 not in lijst)  # True
