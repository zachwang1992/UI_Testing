import random
import string


def generate_a_random_password():
    password_length = 10
    random_password = ''.join(random.choices(string.ascii_letters + string.digits, k=password_length))
    return random_password
