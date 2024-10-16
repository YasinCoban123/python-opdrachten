import random

def generate_random_password() -> str:
    password_length = random.randint(7, 10)
    password = ''.join(chr(random.randint(33, 126)) for _ in range(password_length))

    return password

def main():
    print(generate_random_password(), end='')

if __name__ == "__main__":
    main()
