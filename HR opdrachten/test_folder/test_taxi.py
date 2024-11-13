def calculate_fare(afstand):
    rit = 4.00
    tarief_per_140_meters = 0.25
    afstand_in_meters = afstand * 1000
    full = afstand_in_meters // 140
    tarief_voor_afstand = full * tarief_per_140_meters
    resterend_afstand = afstand_in_meters % 140
    
    if resterend_afstand > 0:
        tarief_voor_afstand += tarief_per_140_meters 

    totaal_rit = rit + tarief_voor_afstand
    
    return round(totaal_rit, 2)

# Assert tests
assert calculate_fare(0) == 4.00, "Test met afstand 0 km"
assert calculate_fare(0.14) == 4.25, "Test met afstand 0.14 km"
assert calculate_fare(1) == 5.75, "Test met afstand 1 km"
assert calculate_fare(1.5) == 6.00, "Test met afstand 1.5 km"
assert calculate_fare(0.28) == 4.50, "Test met afstand 0.28 km"
assert calculate_fare(2) == 7.50, "Test met afstand 2 km"
assert calculate_fare(5) == 15.00, "Test met afstand 5 km"

if __name__ == "__main__":
    afstand = float(input("Distance traveled (in kilometers): "))
    totaal_rit = calculate_fare(afstand)
    print(f"Total fare: {totaal_rit} EUR")
