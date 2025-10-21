
import random
import string

def generate_password(length, include_uppercase=True, include_lowercase=True, include_digits=True, include_symbols=True):
    characters = ''
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_digits:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    if not characters:
        print("Error: No character types selected for the password.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to AUSTSafepass!")

    try:
        num_passwords = int(input("Enter the number of passwords to generate: "))
        if num_passwords <= 0:
            raise ValueError("Number of passwords should be greater than zero.")
    except ValueError as e:
        print(f"Error: {e}")
        return

    length = int(input("Enter the desired password length: "))
    include_uppercase = input("Include uppercase letters? (yes/no): ").lower() == "yes"
    include_lowercase = input("Include lowercase letters? (yes/no): ").lower() == "yes"
    include_digits = input("Include digits? (yes/no): ").lower() == "yes"
    include_symbols = input("Include symbols? (yes/no): ").lower() == "yes"

    print("\nGenerating passwords...\n")

    for i in range(num_passwords):
        password = generate_password(length, include_uppercase, include_lowercase, include_digits, include_symbols)
        if password:
            print(f"Password {i+1}: {password}")

if __name__ == "__main__":
    main()