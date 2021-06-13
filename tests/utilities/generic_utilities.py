import random
import string


def generate_a_random_password():
    session_id_length = 10
    random_session_id = ''.join(random.choices(string.ascii_letters + string.digits, k=session_id_length))
    return random_session_id
