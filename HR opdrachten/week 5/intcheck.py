def is_integer(unchecked: str) -> bool:
    unchecked = unchecked.strip()

    if len(unchecked) == 0:
        return False

    if unchecked[0] in ('+', '-'):

        return unchecked[1:].isdigit() and len(unchecked[1:]) > 0

    return unchecked.isdigit()

def remove_non_integer(unchecked: str) -> int:
    result = ''.join([ch for ch in unchecked if ch.isdigit() or ch in ('+', '-')])
    
    return int(result)

def main():
    user_input = input("Enter a string: ")

    if is_integer(user_input):
        print("Valid integer")
    else:
        print("Invalid integer")

    cleaned_integer = remove_non_integer(user_input)
    print(f"Cleaned integer: {cleaned_integer}")

if __name__ == "__main__":
    main()