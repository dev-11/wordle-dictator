import config as c
from .word_service import WordService


class WordleDictatorService:
    def __init__(self, word_service: WordService):
        self.word_service = word_service

    def update_word_of_the_day(self):
        self.word_service.update_daily_word()

    def get_word_of_the_day(self):
        if not self.word_service.has_daily_word():
            self.update_word_of_the_day()

        return self.word_service.get_daily_word()
