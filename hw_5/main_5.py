#ЗАДАЧА 1
#ВАРИАНТ 1

class Vehicle:

    def __init__(self, speed, year):
        self._speed = speed
        self._year = year

    def move(self):
        print("transport moving...")


class PersonalTransport(Vehicle):

    def __init__(self, speed, year, master):
        super().__init__(speed, year)
        self._master = master


class PublicTransport(Vehicle):

    def __init__(self, speed, year, capacity):
        super().__init__(speed, year)
        self._capacity = capacity

class Autobus(PublicTransport):

    def __init__(self, speed, year, capacity, conductor):
        super().__init__(speed, year, capacity)
        self._conductor = conductor

class Scooter(PersonalTransport):

    def __init__(self, speed, year, master, battery):
        super().__init__(speed, year, master)
        self._battery = battery

class Tram(PublicTransport):

    def __init__(self, speed, year, capacity, number):
        super().__init__(speed, year, capacity)
        self._number = number

class Car(PersonalTransport):

    def __init__(self, speed, year, master, model):
        super().__init__(speed, year, master)
        self._model = model

#ВАРИАНТ 2

class Figure:

    def __init__(self, size):
        self._size = size

    def find_side(self):
        print("в поиске стороны фигуры...")

class TwoDimensional(Figure): pass

class ThreeDimensional(Figure): pass

class Orb(ThreeDimensional):

    def __init__(self, size, radius):
        super().__init__(size)
        self._radius = radius

class Cube(ThreeDimensional):

    def __init__(self, size, edge):
        super().__init__(size)
        self._edge = edge

class Circle(TwoDimensional):

    def __init__(self, size, radius):
        super().__init__(size)
        self._radius = radius

class Triangle(TwoDimensional):

    def __init__(self, size, a, b, c):
        super().__init__(size)
        self._a = a
        self._b = b
        self._c = c

class Rectangle(TwoDimensional):

    def __init__(self, size, width, height):
        super().__init__(size)
        self._width = width
        self._height = height

#ВАРИАНТ 3(ПО ЖЕЛАНИЮ)

class Program: pass

class OperationSystem: pass # честно не знаю что это вообще

class CLI: pass # честно не знаю что это вообще

class AppMobile(Program): pass

class GraphicEditor(Program): pass

class Antivirus(Program): pass

class GamingPlatform(Program): pass

class AppWeb(Program): pass

class CloudService(Program): pass

class ConsoleGame(Program): pass

#ЗАДАЧА 2
#ВАРИАНТ 1

class FarmAnimal:

    def __init__(self, skill_breath):
        self._skill_breath = skill_breath

    def breath(self):
        print("animal to breath...")

class Cow(FarmAnimal):

    def __init__(self, skill_breath, size):
        super().__init__(skill_breath)
        self._size = size

    def move(self):
        print("cow is moving")

class Chicken(FarmAnimal):

    def __init__(self, skill_breath, size):
        super().__init__(skill_breath)
        self._size = size

    def move(self):
        print("chicken is moving...")

class Sheep(FarmAnimal):
    def __init__(self, skill_breath, size):
        super().__init__(skill_breath)
        self._size = size

    def move(self):
        print("sheep is moving...")

class Pig(FarmAnimal):
    def __init__(self, skill_breath, size):
        super().__init__(skill_breath)
        self._size = size

    def move(self):
        print("pig is moving...")


#ВАРИАНТ 2

class Account:

    def __init__(self, number, balance):
        self._number = number
        self._balance = balance

    def money_account(self):
        if self._balance > 0:
            print("На вашем счету есть несколько денежных средств")
        else:
            print("Пополните счёт")

class CreditAccount(Account):

    def __init__(self, number, balance, credit):
        super().__init__(number, balance)
        self._credit = credit

    def credit_limit(self):
        if self._credit == 0:
            print("Кредитный лимит карты был исчерпан")
        else:
            print("На вашей кредитной карте ещё есть средства")

class DebitAccount(Account):

    def __init__(self, number, balance):
        super().__init__(number, balance)

    def make_deposit(self):
        self._balance += 150
        print("Вы успешно добавили на баланс 150 рублей")



#ВАРИАНТ 3

class Human:

    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

class FlightAttendant(Human):
    
    def __init__(self, name, age):
        super().__init__(name)
        self._age = age

    def help_passengers(self):
        print("Помогаю пассажирам...")

class Passenger(Human):

    def __init__(self, name, age, luggage, hand_luggage):
        super().__init__(name)
        self._age = age
        self._luggage = luggage
        self._hand_luggage = hand_luggage

    def search_place(self):
        print("Ищу свое место в самолёте...")

class Pilot(Human):

    def __init__(self, name, age, experience):
        super().__init__(name)
        self._age = age
        self._exp = experience

    def fly(self):
        print("Господа и дамы, мы взлетаем..!")