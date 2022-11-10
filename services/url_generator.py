from string import ascii_letters, digits
from random import choice

from sqlalchemy.orm import Session

from database import crud


def generate_unique_url_id():
    return ''.join([choice(ascii_letters + digits) for i in range(6)])


def get_unique_url_id(db: Session):
    short_id = generate_unique_url_id()
    # Check if short_id is not in db
    while crud.get_url_with_id(db, short_id):
        short_id = generate_unique_url_id()
    return short_id
