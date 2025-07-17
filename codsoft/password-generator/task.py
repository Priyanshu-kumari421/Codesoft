import random
import string

def generate_password(length):
    if length < 4:
        return "Password too short! Use at least 4 characters."
    
    # Characters: uppercase, lowercase, digits, punctuation
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# --- User Input ---
try:
    user_length = int(input("Enter the desired password length: "))
    result = generate_password(user_length)
    print("Generated Password:", result)
except ValueError:
    print("Please enter a valid number.")