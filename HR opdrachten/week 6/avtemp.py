temperatures = (
    ('1995', '3', [
        '47.3', '40.0', '38.3', '36.3', '37.4', '40.3', '41.1', '40.5', '41.6', '43.2',
        '46.2', '45.8', '44.9', '39.4', '40.5', '42.0', '46.5', '46.2', '43.3', '41.7',
        '40.7', '39.6', '44.2', '47.8', '45.9', '47.3', '39.8', '35.2', '38.5', '40.5', '47.0'
    ]),
    ('2010', '3', [
        '39.2', '36.7', '35.5', '35.2', '35.8', '33.8', '30.7', '33.2', '32.3', '33.3',
        '37.3', '39.9', '40.8', '42.9', '42.7', '42.6', '44.8', '50.3', '52.2', '55.2',
        '47.2', '45.0', '48.6', '55.0', '57.4', '50.9', '48.6', '46.2', '49.6', '50.1', '43.6'
    ]),
    ('2020', '3', [
        '43.2', '41.1', '40.0', '43.6', '42.6', '44.0', '44.0', '47.9', '46.6', '50.5',
        '51.5', '47.7', '44.7', '44.0', '48.9', '45.3', '46.6', '49.7', '47.2', '44.8',
        '41.8', '40.9', '41.0', '42.7', '43.4', '44.0', '46.4', '45.5', '40.7', '39.5', '40.6'
    ])
)

def main():
    # tempdata voor elk jaar ophalen
    temps_1995 = temperatures[0][2]
    temps_2010 = temperatures[1][2]
    temps_2020 = temperatures[2][2]

    # unieke dagen met gelijke temperaturen in maart 1995 en maart 2010
    gelijk_1995_2010 = set(temps_1995) & set(temps_2010)

    # unieke dagen met gelijke temperaturen in maart 1995 en maart 2020
    gelijk_1995_2020 = set(temps_1995) & set(temps_2020)

    # jaar met de hoogste temperatuur in maart
    max_1995 = max(temps_1995)
    max_2010 = max(temps_2010)
    max_2020 = max(temps_2020)

    # hoogste temperatuur vergelijken tussen de drie jaren
    hoogste_temp = max(float(max_1995), float(max_2010), float(max_2020))

    # bepaal welk jaar de hoogste temperatuur heeft
    if hoogste_temp == float(max_1995):
        hoogste_jaar = '1995'
    elif hoogste_temp == float(max_2010):
        hoogste_jaar = '2010'
    else:
        hoogste_jaar = '2020'

    # warmste maart (gemmideld temparatuur)
    gem_1995 = sum(map(float, temps_1995)) / len(temps_1995)
    gem_2010 = sum(map(float, temps_2010)) / len(temps_2010)
    gem_2020 = sum(map(float, temps_2020)) / len(temps_2020)

    # jaar bepalen die warmste maart heeft (gemmideld temparatuur)
    warmste_jaar = '1995' if gem_1995 > gem_2010 and gem_1995 > gem_2020 else '2010' if gem_2010 > gem_2020 else '2020'

    # antwoorden printen
    print(len(gelijk_1995_2010))  # aantal dagen met gelijke temperaturen in 1995 en 2010
    print(len(gelijk_1995_2020))  # aantal dagen met gelijke temperaturen in 1995 en 2020
    print(hoogste_jaar)          # jaar met de hoogste temperatuur
    print(warmste_jaar)          # jaar met het warmste maart

if __name__ == "__main__":
    main()