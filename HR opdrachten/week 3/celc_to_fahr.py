def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def temparature():
    print("°C  °F")
    
    for celsius in range(0, 101, 10):
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius:2}  {fahrenheit:.0f}")

temparature()
