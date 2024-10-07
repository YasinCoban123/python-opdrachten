import random

def arithmetic_operation(arithmetic_type):
    correct = 0
    incorrect = 0
    mistakes = [] 

    for _ in range(10):
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)

        if arithmetic_type == "summation":
            correct_result = num1 + num2
            user_answer = int(input(f"{num1} + {num2} = "))
        elif arithmetic_type == "subtraction":
            correct_result = num1 - num2
            user_answer = int(input(f"{num1} - {num2} = "))
        elif arithmetic_type == "multiplication":
            correct_result = num1 * num2
            user_answer = int(input(f"{num1} * {num2} = "))
        else:
            print("Invalid arithmetic type! Please choose summation, subtraction, or multiplication.")
            return

        if user_answer == correct_result:
            correct += 1
        else:
            incorrect += 1
            mistakes.append(f"{num1} {'+' if arithmetic_type == 'summation' else '-' if arithmetic_type == 'subtraction' else '*'} {num2} = {correct_result}, but you answered {user_answer}")

    print(f"\nYou had {correct} correct and {incorrect} incorrect answers in \"{arithmetic_type}\".")
    
    if mistakes:
        print("\nHere are the incorrect answers:")
        for mistake in mistakes:
            print(mistake)

if __name__ == "__main__":
    arithmetic_type = input("Arithmetic operation (summation, subtraction, multiplication): ").lower()
    arithmetic_operation(arithmetic_type)