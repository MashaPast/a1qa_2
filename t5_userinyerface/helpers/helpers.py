import random
import string


def generate_random_text(n=20):
    random_str = ''.join([random.choice(string.ascii_letters) for i in range(n)])
    return random_str