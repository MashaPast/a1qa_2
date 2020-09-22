import random
import string
from typing import Dict


class APIutils:
    @staticmethod
    def check_list_sorted_ascending(body):
        list_of_ids = []
        for el in body:
            list_of_ids.append(el['id'])
        if list_of_ids == sorted(list_of_ids):
            return True
        else:
            return False

    @staticmethod
    def generate_random_str(n=5):
        random_str = ''.join([random.choice(string.ascii_letters) for i in range(n)])
        return random_str

    @staticmethod
    def get_user(list_of_users, id) -> Dict:
        for user in list_of_users:
            if user['id'] == id:
                return user
