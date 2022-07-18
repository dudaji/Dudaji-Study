from abc import ABC, abstractmethod


class Observable(ABC):
    def __init__(self):
        self.__observers: list[NotificationObserver] = []

    def register(self, observer):
        self.__observers.append(observer)

    def remove(self, observer):
        if observer in self.__observers:
            self.__observers.remove(observer)

    def notify(self):
        for observer in self.__observers:
            observer.update(self)

    @abstractmethod
    def get_value(self):
        pass

    @abstractmethod
    def update_value(self, value):
        pass


class ObserverManager(Observable):
    def __init__(self):
        super().__init__()
        self.value = None

    def get_value(self):
        return self.value

    def update_value(self, value):
        self.value = value
        self.notify()


class Observer(ABC):
    @abstractmethod
    def update(self, observable: Observable):
        pass


class NotificationObserver:
    def __init__(self, value):
        self.value = value

    def update(self, observable: Observable):
        self.value = observable.get_value()
