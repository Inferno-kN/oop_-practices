#Задача 1

class Patient:
    def __init__(self, fio: str, age: int, zabolev: str):
        self.fio = fio
        self.age = age
        self.zabolev = zabolev

    def zapis(self, date: str, time: str):
        print(f"{self.fio}, Вы записаны на приём в дату {date} и время {time}")

    def info(self):
        print(f"ФИО: {self.fio}, Возраст: {self.age}, Текущее заболевание: {self.zabolev}")

#Задача 2

class TouristSpot:
    def __init__(self, place: str, country: str, dostopr: str):
        self.place = place
        self.country = country
        self.dostopr = dostopr

    def visit_place(self, name: str):
        print(f"{name}, Вы посетили нас!")

    def info(self):
        print(f"Место: {self.place}, Страна: {self.country}, Достопримечательность: {self.dostopr}")

#Задача 3

class ModelWindow:

    width_screen = 1960 #ширина экрана, а это горизонталь gorizont
    height_screen = 1080 #высота экрана, то есть вертикаль vertikal

    def __init__(self, title: str, koord: int, vertikal: int, gorizont: int, color: str, visible: bool, frame: bool):
        self.title = title
        self.koord = koord
        self.vertikal = vertikal
        self.gorizont = gorizont
        self.color = color
        self.visible = visible
        self.frame = frame

    def movement_vertikal(self) -> bool:
        if 0 <= self.vertikal <= ModelWindow.height_screen:
            print(f"Окно по вертикали {self.vertikal} двигается или находится в состоянии покоя на высоте {ModelWindow.height_screen} экрана")
            return True
        else:
            print(f"Окно по вертикали {self.vertikal} не может превышать высоту {ModelWindow.height_screen} экрана")
            return False

    def movement_gorizont(self) -> bool:
        if 0 <= self.gorizont <= ModelWindow.width_screen:
            print(f"Окно по горизонтали {self.gorizont} двигается или находится в состоянии покоя на ширине {ModelWindow.width_screen} экрана")
            return True
        else:
            print(f"Окно по горизонтали {self.gorizont} не может превышать ширину {ModelWindow.width_screen} экрана")
            return False


    def height_change(self, height: int):
        if 0 <= height <= ModelWindow.height_screen:
            print(f"Высота изменилась на {height} сантиметров")
        else:
            print(f"Отрицательная высота или высота, превышающая высоту экрана невозможна!")

    def width_change(self, width: int):
        if 0 <= width <= ModelWindow.width_screen:
            print(f"Ширина изменилась на {width} сантиметров")
        else:
            print(f"Отрицательная ширина или ширина, превышающая ширину экрана невозможна!")


    def update_color(self, new_color: str) -> bool:
        if self.color != new_color:
            print(f"Цвет {self.color} остался без изменений")
            return False
        else:
            print(f"Цвет {self.color} был изменён на {new_color}")
            return True

    def update_frame(self, new_frame: str) -> bool:
        if self.frame != new_frame:
            print(f"Рамка {self.frame} осталось такой же")
            return False
        else:
            print(f"Рамка {self.frame} была изменена на рамку {new_frame}")

    def __str__(self):
        return f"Заголовок окна: {self.title}, Координаты левого верхнего угла: {self.koord},\nРазмер по горизонтали, Размер по вертикали:{self.gorizont}, {self.vertikal}, Цвет окна: {self.color}, Cостояние видимое/невидимое: {self.visible}, состояние с рамкой/без рамки: {self.frame}"

#Задача 4

class ArrayUtils:

    @staticmethod
    def sum(arr):
        return sum(arr)

    @staticmethod
    def multi_arr(arr):
        multi = 1
        for i in arr:
            multi *= i
        print(multi)

    @staticmethod
    def inverse_arr(arr):
        return arr[::-1]

    @staticmethod
    def max1(arr):
        max1 = arr[0]
        if max1 < arr[1]:
            max1 = arr[1]
        return max1

    @staticmethod
    def min1(arr):
        min1 = arr[1]
        if min1 < arr[0]:
            min1 = arr[0]
        return min1

#Задача 5

class Vector:
    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other): #это скалярное произведение, а вот векторное произведение не пойму как сделать
        return Vector(self.x * other.x, self.y * other.y, self.z * other.z)

    def lenn(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def __str__(self):
        return f"{self.x}, {self.y}, {self.z}"

#Задача 6

class Fraction:
    def __init__(self, numerator: int, denominator: int): # numerator - числитель, denominator - знаменатель
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, other):
        if self.denominator != 0:
            new_numerator = self.numerator + other.numerator
            new_denominator = self.denominator + other.denominator
            return new_numerator, new_denominator
        else:
            raise ValueError("Знаменатель не может быть равен нулю")


    def __sub__(self, other):
        if self.denominator != 0:
            new_numerator = self.numerator - other.numerator
            new_denominator = self.denominator - other.denominator
            return new_numerator, new_denominator
        else:
            raise ValueError("Знаменатель не может быть равен нулю")


    def __mul__(self, other):
        if self.denominator != 0:
            new_numerator = self.numerator * other.numerator
            new_denominator = self.denominator * other.denominator
            return new_numerator, new_denominator
        else:
            raise ValueError("Знаменатель не может быть равен нулю")

    def __str__(self):
        if self.denominator == 1:
            return self.numerator
        else:
            return self.numerator / self.denominator


#Задача 7
import math

class GeometryUtils:

    @staticmethod #1
    def calculating_circle(radius: float) -> float:
        S = math.pi * radius**2 # рассчитываем площадь круга
        return S

    @staticmethod #2
    def perimeter_circle(radius: float) -> float:
        P = 2 * math.pi * radius
        return P

    @staticmethod #3
    def rectangle_area(length: float, width: float) -> float:
        S = length * width #площадь прямоугольника
        return S

    @staticmethod #4
    def perimeter_area(length: float, width: float) -> float:
        P = 2 * (length + width)
        return P

    @staticmethod
    def rectangle_geron(a: float, b: int, c: float) -> float:
        p = (a + b + c) / 2
        Geron = math.sqrt(p * (p - a) * (p - b) * (p - c))
        return Geron




