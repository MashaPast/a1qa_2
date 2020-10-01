import random
import string


class Utils:

    @staticmethod
    def generate_random_str(n=5):
        random_str = ''.join([random.choice(string.ascii_letters) for i in range(n)])
        return random_str

