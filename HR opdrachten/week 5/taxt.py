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

if __name__ == "__main__":
    afstand = float(input("Distance traveled (in kilometers): "))

    totaal_rit = calculate_fare(afstand)

    print(f"Total fare: {totaal_rit} EUR")
