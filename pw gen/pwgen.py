import random
import string

def generate_password(length=12):
    """Generates a random secure password."""
    if length < 8:
        raise ValueError("Password length must be at least 8 characters.")
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(characters, k=length))
    return password
