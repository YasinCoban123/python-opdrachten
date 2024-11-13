''' 
**kwargs en *args worden gebruikt om functies flexibeler 
te maken door een variabel aantal argumenten 
aan een functie door te geven
'''



'''
*args
Staat voor "arguments" en wordt gebruikt om een willekeurig 
aantal positional arguments door te geven aan een functie.
In de functie worden deze argumenten als een tuple opgeslagen.
Voorbeeld:
'''

def optellen(*args):
    return sum(args)

print(optellen(1, 2, 3))  # Output: 6
print(optellen(5, 10, 15, 20))  # Output: 50


'''
**kwargs:
Staat voor "keyword arguments" en wordt gebruikt om een willekeurig 
aantal named (keyword) arguments door te geven aan een functie.
In de functie worden deze argumenten als een dictionary opgeslagen.
'''

def print_gegevens(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_gegevens(naam="Sophie", leeftijd=25, stad="Amsterdam")

