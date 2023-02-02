from abc import ABC
from enum import Enum, auto


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
    def prepare(self, amount):
        pass


class TeaFactory(HotDrinkFactory):
    def prepare(self, amount):
        print(f'Boil water, warm up the pot, pour {amount}ml')
        return Tea()


class CoffeeFactory(HotDrinkFactory):
    def prepare(self, amount):
        print(f'Grind some beans, boil water, pour {amount}ml')
        return Coffee()


# def make_drink(drink_type: str):
#     match drink_type:
#         case 'tea':
#             return TeaFactory().prepare(200)
#         case 'coffee':
#             return CoffeeFactory().prepare(50)
#         case _:
#             return None


class HotDrinkMachine:
    class AvailableDrink(Enum):
        COFFEE = auto()
        TEA = auto()

    factories = []
    initialized = False

    def __init__(self):
        if not self.initialized:
            self.initialized = True
            for d in self.AvailableDrink:
                name = d.tag.capitalize()
                factory_name = d.tag.capitalize() + 'Factory'
                factory_instance = eval(factory_name)()
                self.factories.append((name, factory_instance))

    def make_drink(self):
        print('Available drinks: ')
        for f in self.factories:
            print(f[0])

        idx = int(input(f'Please pick drink (0-{len(self.factories) - 1}):\n'))
        amount = int(input('Specify amount of drink:\n'))
        return self.factories[idx][1].prepare(amount)


if __name__ == '__main__':
    # entry = input('What drink would you like?\n')
    # drink = make_drink(entry)
    # drink.consume()
    hdm = HotDrinkMachine()
    hdm.make_drink()
