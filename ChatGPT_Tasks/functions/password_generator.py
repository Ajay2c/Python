import random
import string

def generate_password(length):
    """Generate a random password of given length"""
    password = ''
    chars = string.ascii_lowercase + string.digits
    for i in range(length):
        password += random.choice(chars)
    return password

# Generate a random password of length 8
password = generate_password(8)
print(password)
