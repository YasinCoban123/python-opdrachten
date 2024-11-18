class Converter:
    # Conversiefactoren van meters naar elke eenheid
    CONVERSIONS = {
        'inches': 0.0254,        # 1 inch = 0.0254 meter
        'feet': 0.3048,          # 1 foot = 0.3048 meter
        'yards': 0.9144,         # 1 yard = 0.9144 meter
        'miles': 1609.344,       # 1 mile = 1609.344 meter
        'kilometers': 1000,      # 1 kilometer = 1000 meter
        'meters': 1,             # 1 meter = 1 meter
        'centimeters': 0.01,     # 1 centimeter = 0.01 meter
        'millimeters': 0.001     # 1 millimeter = 0.001 meter
    }

    def __init__(self, length, unit):
        """
        Initialiseer het Converter-object met een lengte en bijbehorende eenheid.
        Converteer de ingevoerde lengte naar meters als basis eenheid.
        """
        if unit not in self.CONVERSIONS:
            raise ValueError(f"Niet-ondersteunde eenheid: {unit}")
        # Converteer naar meters met behulp van de juiste factor
        self.length_in_meters = length * self.CONVERSIONS[unit]

    def _convert_from_meters(self, target_unit):
        """
        Converteer de lengte van meters naar de gewenste eenheid.
        """
        if target_unit not in self.CONVERSIONS:
            raise ValueError(f"Niet-ondersteunde eenheid: {target_unit}")
        # Bereken de waarde in de gewilde eenheid
        return self.length_in_meters / self.CONVERSIONS[target_unit]

    # Methodes voor elke eenheid
    def inches(self):
        return self._convert_from_meters('inches')

    def feet(self):
        return self._convert_from_meters('feet')

    def yards(self):
        return self._convert_from_meters('yards')

    def miles(self):
        return self._convert_from_meters('miles')

    def kilometers(self):
        return self._convert_from_meters('kilometers')

    def meters(self):
        return self._convert_from_meters('meters')

    def centimeters(self):
        return self._convert_from_meters('centimeters')

    def millimeters(self):
        return self._convert_from_meters('millimeters')


# Voorbeeldgebruik:
c = Converter(9, 'inches')  # Maak een Converter object met 9 inches
print(c.feet())             # Output: 0.75 (9 inches naar feet)
print(c.meters())           # Output: 0.2286 (9 inches naar meters)
print(c.centimeters())      # Output: 22.86 (9 inches naar centimeters)
print(c.yards())            # Output: 0.25 (9 inches naar yards)