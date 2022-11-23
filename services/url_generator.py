from string import ascii_uppercase
from random import choice

from sqlalchemy.orm import Session


numbers = {}
for i in range(1, 10):
    numbers[i] = str(i)

for k, v in enumerate(ascii_uppercase):
    numbers[k+10] = v


def generate_unique_url_id(url_id):
    return ''.join(number_to_base(url_id))


def number_to_base(n, b=36):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(numbers[int(n % b)])
        n //= b
    return digits[::-1]
