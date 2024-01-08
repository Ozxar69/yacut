import random
import string

from .models import URLMap


def get_unique_short_id():
    while True:
        length = random.randint(8, 16)
        characters = string.ascii_letters + string.digits
        short_id = ''.join(random.choice(characters) for _ in range(length))
        if not URLMap.query.filter_by(short=short_id).first():
            return short_id
