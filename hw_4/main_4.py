#Задача 1
from __future__ import annotations

class Student:

    def __init__(self, name: str, surname: str, age: int, avg: float):
        self.name = name
        self.surname = surname
        self.age = age
        self.avg = avg

    def get_name(self):
        return self.name

    def get_surname(self):
        return self.surname

    def get_age(self):
        return self.age

    def get_avg(self):
        return self.avg

    def set_name(self, name):
        self.name = name

    def set_surname(self, surname):
        self.surname = surname

    def set_age(self, age):
        self.age = age

    def set_avg(self, avg):
        self.avg = avg

    def __str__(self):
        return f"Студент: {self.name} {self.surname}, Возраст: {self.age}, Средний балл: {self.avg}"

    def __eq__(self, other):
        return self.avg == other.avg

    def __ne__(self, other):
        return self.avg != other.avg

    def __lt__(self, other):
        return self.avg < other.avg

    def __le__(self, other):
        return self.avg <= other.avg

    def __gt__(self, other):
        return self.avg > other.avg

    def __ge__(self, other):
        return self.avg >= other.avg

#задача 2

class Library:

    def __init__(self, name: str, address: str):
        self.__name = name
        self.__address = address
        self.__books = []
        self.__employees = []

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_books(self):
        return self.__books

    def get_employees(self):
        return self.__employees

    def set_address(self, address: str):
        self.__address = address

    def add_book(self, book: Book):
        if book not in self.__books:
            self.__books.append(book)

    def remove_book(self, book: Book):
        if book in self.__books:
            self.__books.remove(book)

    def add_employee(self, employee: Employee):
        if employee not in self.__employees:
            self.__employees.append(employee)

    def remove_employee(self, employee: Employee):
        if employee in self.__employees:
            self.__employees.remove(employee)

    def __str__(self):
        return f"Имя библиотеки: {self.__name}, Адрес: {self.__address}, Список книг: {self.__books}, Список сотрудников: {self.__employees}"


class Book:

    def __init__(self, title, author, year, book_id):
        self.__title = title
        self.__author = author
        self.__year = year
        self.__id = book_id
        self.__genres = []

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_year(self):
        return self.__year

    def get_id(self):
        return self.__id

    def get_genres(self):
        return self.__genres

    def set_year(self, year):
        self.__year = year

    def add_genre(self, genre: Genre):
        if genre not in self.__genres:
            self.__genres.append(genre)

    def remove_genre(self, genre: Genre):
        if genre in self.__genres:
            self.__genres.remove(genre)

    def __str__(self):
        return f"Название: {self.__title}, Автор: {self.__author}, Год: {self.__year}, ID: {self.__id}, Жанры: {self.__genres}"

class Employee:
    def __init__(self, name, position, employee_id):
        self.__name = name
        self.__position = position
        self.__id = employee_id
        self.__contact_info = []

    def get_name(self):
        return self.__name

    def get_position(self):
        return self.__position

    def get_id(self):
        return self.__id

    def get_contact_info(self):
        return self.__contact_info

    def set_position(self, position: str):
        self.__position = position

    def add_contact_info(self, contact_info: ContactInfo):
        if contact_info not in self.__contact_info:
            self.__contact_info.append(contact_info)

    def remove_contact_info(self, contact_info: ContactInfo):
        if contact_info in self.__contact_info:
            self.__contact_info.remove(contact_info)

    def __str__(self):
        return f"Сотрудник: {self.__name}, Должность: {self.__position}, ID: {self.__id}"

class Genre:

    def __init__(self, name, description):
        self.__name = name
        self.__description = description

    def get_name(self):
        return self.__name

    def get_description(self):
        return self.__description

    def set_name(self, name):
        self.__name = name

    def set_description(self, description):
        self.__description = description

    def __str__(self):
        return f"Жанр: {self.__name}, Описание: {self.__description}"


class ContactInfo:

    def __init__(self, type, value):
        self.__type = type
        self.__value = value

    # Геттеры
    def get_type(self):
        return self.__type

    def get_value(self):
        return self.__value

    # Сеттеры
    def set_value(self, value):
        self.__value = value

    def __str__(self):
        return f"Тип контакта: {self.__type}, Значение контакта: {self.__value}"

#Задача 3

class Car:

    def __init__(self, mark: str, model: str, year: int, price: float, status="None"):
        self.__mark = mark
        self.__model = model
        self.__year = year
        self.__price = price
        self.__status = status

    def get_mark(self):
        return self.__mark

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    def get_price(self):
        return self.__price

    def get_status(self):
        return self.__status

    def set_price(self, price):
        self.__price = price

    def set_status(self, status):
        self.__status = status

        if self.__status != status:
            print("Статус должен быть: В наличии, Продано, Ожидает")

    def __str__(self):
        return f"Марка: {self.__mark}, Модель: {self.__mark}, Год производства: {self.__year}, Цена: {self.__price}, Статус: {self.__status}"

class Seller:

    def __init__(self, name: str, experience: int, sold_cars: list[str]):
        self.__name = name
        self.__experience = experience
        self.__sold_cars = []

    def get_name(self):
        return self.__name

    def get_experience(self):
        return self.__experience

    def get_sold_cars(self):
        return self.__sold_cars

    def set_experience(self, experience):
        self.__experience = experience

    def add_sold_car(self, car: Car):
        if car not in self.__sold_cars:
            self.__sold_cars.append(car)

    def remove_sold_car(self, car: Car):
        if car in self.__sold_cars:
            self.__sold_cars.remove(car)

    def __str__(self):
        return f"Продавец: {self.__name}, Стаж: {self.__experience} лет, Проданные автомобили: [{self.__sold_cars}]"


class Customer:
    def __init__(self, name: str, phone: str, email: str, purchased_cars: list[str]):
        self.__name = name
        self.__phone = phone
        self.__email = email
        self.__purchased_cars = []

    def get_name(self):
        return self.__name

    def get_phone(self):
        return self.__phone

    def get_email(self):
        return self.__email

    def get_purchased_cars(self):
        return self.__purchased_cars

    def set_phone(self, phone):
        self.__phone = phone

    def set_email(self, email):
        self.__email = email

    def add_purchased_car(self, car: Car):
        if car not in self.__purchased_cars:
            self.__purchased_cars.append(car)

    def remove_purchased_car(self, car: Car):
        if car in self.__purchased_cars:
            self.__purchased_cars.remove(car)

    def __str__(self):
        return f"Клиент: {self.__name}, Телефон: {self.__phone}, Email: {self.__email}, Купленные автомобили: {self.__purchased_cars}"


class Dealership:
    def __init__(self):
        self.__cars = []
        self.__sellers = []
        self.__customers = []

    # Геттеры
    def get_cars_in_stock(self):
        return self.__cars

    def get_salespeople(self):
        return self.__sellers

    def get_customers(self):
        return self.__customers

    def add_car(self, car: Car):
        if car not in self.__cars:
            self.__cars.append(car)

    def remove_car(self, car: Car):
        if car in self.__cars:
            self.__cars.remove(car)

    def register_salesperson(self, salesperson: Seller):
        if salesperson not in self.__sellers:
            self.__sellers.append(salesperson)

    def fire_salesperson(self, salesperson: Seller):
        if salesperson in self.__sellers:
            self.__sellers.remove(salesperson)

    def register_customer(self, customer: Customer):
        if customer not in self.__customers:
            self.__customers.append(customer)

    def __str__(self):
        return f"Автомобили в наличии: {self.__cars}, Продавцы: {self.__sellers}, Клиенты: {self.__customers}"

