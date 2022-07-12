from abc import ABC, abstractmethod
import random


class Observer:
    def update(self):
        return "Helllo"


class Subject(ABC):
    @abstractmethod
    def attach(selfself, observer: Observer):
        pass

    @abstractmethod
    def detach(selfself, observer: Observer):
        pass

    @abstractmethod
    def notify(self):
        pass


class ConcreteSubject(Subject):
    _state: int = 0
    _observers = []

    def attach(self, observer: Observer):
        self._observers.append(observer)

    def detach(self, observer: Observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update()

    def some_business_logic(self):
        self._state = random.randint(1, 10)
        self.notify()
