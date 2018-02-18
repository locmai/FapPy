import random
import string
from accounts.models import UserKey


def get_key():
    keys = [elem.key for elem in UserKey.objects.all()]
    generate_key(keys)


def generate_key(keys):
    key = ''.join(random.choices(string.ascii_uppercase + string.digits, k=150))
    if key in keys:
        return generate_key(keys)
    return key