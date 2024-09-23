def is_palindrome(user_string):
    cleaned_string = ""
    for char in user_string:
        if char.isalnum():
            cleaned_string += char.lower()

    return cleaned_string == cleaned_string[::-1]

# Read input from the user
user_input = input("Enter a string: ")

# Check if the string is a palindrome
if is_palindrome(user_input):
    print(f'"{user_input}" is a palindrome')
else:
    print(f'"{user_input}" is not a palindrome')
