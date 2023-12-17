import random


class RandomService:
    @staticmethod
    def get_random(min_, max_):
        return random.randrange(min_, max_)
