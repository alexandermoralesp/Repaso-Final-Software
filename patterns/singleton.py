import random


class SingletonClass:
    _output = ""

    @staticmethod
    def get(self):
        if self._output != "":
            return self._output
        self._output = random.randint(1, 10)
