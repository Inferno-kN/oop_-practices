#Задача 1

class Patient:
    def __init__(self, fio: str, age: int, zabolev: str):
        self.fio = fio
        self.age = age
        self.disease = disease

    def zapis(self, date: str, time: str):
        print(f"{self.fio}, Вы записаны на приём в дату {date} и время {time}")

    def info(self):
        print(f"ФИО: {self.fio}, Возраст: {self.age}, Текущее заболевание: {self.disease}")

#Задача 2

class TouristSpot:
    def __init__(self, place: str, country: str, dostopr: str):
        self.place = place
        self.country = country
        self.sight = sight

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

    def movement_vertikal(self, delta) -> bool:
       new_y = self.koord_y + delta
        if 0 <= new_y <= ModelWindow.height_screen - self.height:
            self.koord_y = new_y
            print(f"Окно перемещено по вертикали на {delta}, Текущая координата Y: {self.koord_y}")
            return True
        else:
            print(f"Перемещение по вертикали на {delta} невозможно. Окно выходит за границы экрана.")
            return False

    def move_horizontal(self, delta: int) -> bool:
        new_x = self.koord_x + delta
        if 0 <= new_x <= ModelWindow.width_screen - self.width:
            self.koord_x = new_x
            print(f"Окно перемещено по горизонтали на {delta}, Текущая координата X: {self.koord_x}")
            return True
        else:
            print(f"Перемещение по горизонтали на {delta} невозможно. Окно выходит за границы экрана.")
            return False


    def change_height(self, new_height: int) -> bool:
        if 0 <= new_height <= ModelWindow.height_screen:
            self.height = new_height
            print(f"Высота окна изменена на {new_height}.")
            return True
        else:
            print(f"Недопустимая высота: {new_height}. Высота должна быть в пределах от 0 до {ModelWindow.height_screen}.")
            return False

    def change_width(self, new_width: int) -> bool:
        if 0 <= new_width <= ModelWindow.width_screen:
            self.width = new_width
            print(f"Ширина окна изменена на {new_width}.")
            return True
        else:
            print(f"Недопустимая ширина: {new_width}. Ширина должна быть в пределах от 0 до {ModelWindow.width_screen}.")
            return False

    def update_color(self, new_color: str) -> bool:
        if self.color != new_color:
            old_color = self.color
            self.color = new_color
            print(f"Цвет окна изменен с {old_color} на {new_color}.")
            return True
        else:
            print(f"Цвет остался без изменений: {self.color}.")
            return False

    def toggle_visibility(self):
        self.visible = not self.visible
        state = "видимое" if self.visible else "невидимое"
        print(f"Состояние окна изменено на {state}.")

    def toggle_frame(self):
        self.frame = not self.frame
        state = "с рамкой" if self.frame else "без рамки"
        print(f"Состояние рамки изменено на {state}.")

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
        if min1 > arr[0]:
            min1 = arr[0]
        return min1

#Задача 5

class Vector:
    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
            
    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
            
    def __mul__(self, other):
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y + self.z * other.z # Скалярное произведение

     def cross(self, other): # Векторное произведение
        if isinstance(other, Vector):
            new_x = self.y * other.z - self.z * other.y
            new_y = self.z * other.x - self.x * other.z
            new_z = self.x * other.y - self.y * other.x
            return Vector(x_component, y_component, z_component)

    def length(self):
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


#Задача 8

class Time:
    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours + (minutes // 60) # если задано минут > 60, то присваиваем целое
        self.minutes = (minutes % 60) + (seconds // 60)
        self.seconds = seconds % 60

    def __add__(self, other):
        new_hours = self.hours + other.hours
        new_minutes = self.minutes + other.minutes
        new_seconds = self.seconds + other.seconds
        return new_hours, new_minutes, new_seconds

    def __sub__(self, other):
        new_hours = self.hours - other.hours
        new_minutes = self.minutes - other.minutes
        new_seconds = self.seconds - other.seconds
        return new_hours, new_minutes, new_seconds

    def __mul__(self, other):
        new_hours = self.hours * other.hours
        new_minutes = self.minutes * other.minutes
        new_seconds = self.seconds * other.seconds
        return new_hours, new_minutes, new_seconds

    def __str__(self):
        return f"{(self.hours % 100) // 10}{(self.hours // 1) % 10}:{(self.minutes % 100) // 10}{self.minutes % 10}:{(self.seconds % 100) // 10}{self.seconds % 10}"

