from abc import ABC, abstractmethod


class LanguageAbstract(ABC):
    @abstractmethod
    def do_algorithm(self, data):
        pass


class EnglishConcrete(LanguageAbstract):
    def do_algorithm(self, data):
        return data*"Hello world"


class SpanishConcrete(LanguageAbstract):
    def do_algorithm(self, data):
        return data*"Hola mundo"


class FrenchConcrete(LanguageAbstract):
    def do_algorithm(self, data):
        return data*"Bonjour le monde"


class Context:
    def __init__(self, strategy: LanguageAbstract):
        self._strategy = strategy

    @property
    def strategy(self):
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: LanguageAbstract):
        self._strategy = strategy

    def do_some_business_logic(self):
        print("Context realize the strategy")
        result = self._strategy.do_algorithm(1)
        print(",".join(result))
