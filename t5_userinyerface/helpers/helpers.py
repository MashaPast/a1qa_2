import random
import string


def generate_random_email(n=5):
    random_str = ''.join([random.choice(string.ascii_letters) for i in range(n)])
    return random_str


def generate_random_pass(n=15):
    letter_from_email = generate_random_email()[0]
    random_number = random.randint(0, 10)
    rus = 'ы'
    random_str = ''.join([random.choice(string.ascii_uppercase + string.ascii_letters) for i in range(n)])
    random_pass = random_str + letter_from_email + str(random_number) + rus
    return random_pass


