

def check_list_sorted_ascending(body):
    list_of_ids = []
    for el in body:
        list_of_ids.append(el['id'])
    if list_of_ids == sorted(list_of_ids):
        return True
    else:
        return False
