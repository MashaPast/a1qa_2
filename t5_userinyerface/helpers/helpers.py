import random
import string
import base64
from t5_userinyerface import CONFIG_DATA


def generate_random_str(n=5):
    random_str = ''.join([random.choice(string.ascii_letters) for i in range(n)])
    return random_str


def generate_random_pass(n=15):
    letter_from_email = generate_random_str()[0]
    random_number = random.randint(0, 10)
    rus = 'ы'
    random_str = ''.join([random.choice(string.ascii_uppercase + string.ascii_letters) for i in range(n)])
    random_pass = random_str + letter_from_email + str(random_number) + rus
    return random_pass


def encode_image_with_base64():
    with open(CONFIG_DATA["IMAGE_PATH"], "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
        return encoded_string
