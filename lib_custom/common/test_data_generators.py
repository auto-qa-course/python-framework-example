import random
import string


class TestDataGenerators:

    @staticmethod
    def generate_random_id():
        return random.randrange(100, 200, 2).to_s

    @staticmethod
    def generate_random_str(string_length):
        return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(string_length))
