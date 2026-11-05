"""
Decodelabs - Project 3: Random Password Generator
Goal: Ask the user for a password length and generate a random,
      complex password using letters, numbers (and optional symbols).
Key skills: Importing modules (random, string) & string manipulation.
"""

import random
import string


def generate_password(length, use_symbols=True):
    """Build a random password of the given length."""
    letters = string.ascii_letters      # a-z and A-Z
    digits = string.digits              # 0-9
    symbols = string.punctuation if use_symbols else ""

    # Guarantee at least one letter and one digit (and one symbol if used)
    password_chars = [random.choice(letters), random.choice(digits)]
    if use_symbols:
        password_chars.append(random.choice(symbols))

    # Fill the remaining length with random characters from the full pool
    all_chars = letters + digits + symbols
    while len(password_chars) < length:
        password_chars.append(random.choice(all_chars))

    # Shuffle so the guaranteed characters aren't always at the start
    random.shuffle(password_chars)

    # Join the list of characters into a single string
    return "".join(password_chars)


def get_length():
    """Keep asking until the user enters a valid length."""
    while True:
        value = input("Enter password length (e.g., 8): ").strip()
        if not value.isdigit():
            print("Please enter a whole number.")
            continue
        length = int(value)
        if length < 4:
            print("Password must be at least 4 characters for good security.")
            continue
        return length


def main():
    print("=" * 35)
    print("   RANDOM PASSWORD GENERATOR")
    print("=" * 35)

    length = get_length()
    choice = input("Include symbols like @#$%? (y/n): ").strip().lower()
    use_symbols = choice != "n"

    password = generate_password(length, use_symbols)
    print(f"\nYour generated password: {password}")

    # Simple string-based strength hint
    if length >= 12 and use_symbols:
        print("Strength: Strong")
    elif length >= 8:
        print("Strength: Medium")
    else:
        print("Strength: Weak - try a longer password.")


if __name__ == "__main__":
    main()
