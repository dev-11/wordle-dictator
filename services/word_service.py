from datetime import datetime as dt
import config as c


class WordService:
    def __init__(self, storage_service, random_service):
        self._storage_service = storage_service
        self.random_service = random_service

    def has_daily_word(self):
        return self._storage_service.has(c.word_of_the_day_file)

    def get_daily_word(self):
        return self._storage_service.get(c.word_of_the_day_file)

    def update_daily_word(self):
        words = self._storage_service.get_lines(c.words_file)
        random_index = self.random_service.get_random(0, len(words)-1)
        self._storage_service.save_or_update(c.word_of_the_day_file, words[random_index], dt.now())

    def get_all_words(self):
        return self._storage_service.get_lines(c.words_file)
