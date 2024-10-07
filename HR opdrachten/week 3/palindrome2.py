def is_palindrome(s):
    leeg_str = ""
    for char in s:
        if char.isalnum():  
            leeg_str += char.lower()

    for i in range(len(leeg_str) // 2):
        if leeg_str[i] != leeg_str[-(i + 1)]:
            return False
    return True

input_sentence = input("Enter a sentence: ")

if is_palindrome(input_sentence):
    print(f'"{input_sentence}" is a palindrome.')
else:
    print(f'"{input_sentence}" is not a palindrome.')
