from abc import ABC


class HotDrink(ABC):
    def consume(self):
        pass


class Tea(HotDrink):
    def consume(self):
        print('This tea is tasty')


class Coffee(HotDrink):
    def consume(self):
        print('This coffee is tasty')


class HotDrinkFactory(ABC):
    def prepare(self):
        pass


class TeaFactory(HotDrinkFactory):
    def 
