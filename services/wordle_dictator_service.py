import config as c


class WordleDictatorService:
    def __init__(self, storage_service, random_service):
        self._storage_service = storage_service
        self._random_service = random_service

    def get_word_of_the_day(self):
        words = self._storage_service.get(c.words_file).split("\n")
        index = self._random_service.get_random(0, len(words)-1)
        return words[index]
