# functie om unieke charachters te tellen met dictionary
def unique_chars_dict(input_string):
    char_count = {}
    
    # elk character als key toevoegen in dictionary
    for char in input_string:
        char_count[char] = True
    
    return len(char_count)

# functie om unieke charachters te tellen met set
def unique_chars_set(input_string):
    # string naar set verplaatsen, waarbij dan alleen unieke characters blijft
    return len(set(input_string))

if __name__ == "__main__":
    input_string = input("Enter a string: ")
    
    # resultaat printen met dic of set
    print(f"Unique characters (using dictionary): {unique_chars_dict(input_string)}")
    print(f"Unique characters (using set): {unique_chars_set(input_string)}")