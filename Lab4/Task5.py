import random
from random import sample
import string
def get_random_password(n=8) -> str:
    num = string.ascii_letters + string.digits
    password = ''.join(random.sample(num, n))
    return password


print(get_random_password())

