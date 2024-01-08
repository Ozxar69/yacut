import random
import string

from .models import URLMap
from .constants import LENGTH


def get_unique_short_id():
    while True:
        characters = string.ascii_letters + string.digits
        short_id = "".join(random.choice(characters) for _ in range(LENGTH))
        if not URLMap.query.filter_by(short=short_id).first():
            return short_id
