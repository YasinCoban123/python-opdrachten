def is_palindrome(s):
    leeg_str = ""
    for char in s:
        if char.isalnum():  
            leeg_str += char.lower()

    for i in range(len(leeg_str) // 2):
        if leeg_str[i] != leeg_str[-(i + 1)]:
            return False
    return True

input_string = input("Enter a string: ")

if is_palindrome(input_string):
    print(f'"{input_string}" is a palindrome.')
else:
    print(f'"{input_string}" is not a palindrome.')
