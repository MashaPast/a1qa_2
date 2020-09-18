import random
import string


def check_list_sorted_ascending(body):
    list_of_ids = []
    for el in body:
        list_of_ids.append(el['id'])
    if list_of_ids == sorted(list_of_ids):
        return True
    else:
        return False


def generate_random_str(n=5):
    random_str = ''.join([random.choice(string.ascii_letters) for i in range(n)])
    return random_str


def get_user_with_id_5(list_of_users):
    for user in list_of_users:
        if user['id'] == 5:
            return user