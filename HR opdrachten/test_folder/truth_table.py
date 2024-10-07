# Functie om een truth table voor AND, OR en NOT te genereren
def truth_table():
    print("A\tB\tA AND B\tA OR B\tNOT A")
    print("-" * 30)
    
    # Alle mogelijke combinaties van A en B
    for A in [True, False]:
        for B in [True, False]:
            # AND, OR en NOT operaties uitvoeren
            and_result = A and B
            or_result = A or B
            not_a = not A
            
            # Resultaten printen
            print(f"{A}\t{B}\t{and_result}\t{or_result}\t{not_a}")

# Truth table genereren
truth_table()




# Een simpelere variant ervan
# Alle mogelijke waarden voor A en B
A_values = [True, False]
B_values = [True, False]

# Koptekst van de truth table
print("A     B     A AND B     A OR B")

# Lussen door alle mogelijke combinaties van A en B
for A in A_values:
    for B in B_values:
        print(f"{A}  {B}  {A and B}       {A or B}")
