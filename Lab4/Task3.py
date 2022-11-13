import random


def get_unique_list_numbers() -> list[int]:
    num_random = list(range(-10,11))
    random.shuffle(num_random)
    return num_random[:15]


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
