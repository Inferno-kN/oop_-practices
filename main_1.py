#Задача 1
from fontTools.cffLib.width import missingdict


class Animal:
    def __init__(self, name: str, vid: str, age: int):
        self.name = name
        self.vid = vid
        self.age = age

    def sound(self, sound: str):
        self.sound = sound

    def info(self):
        print(f"Имя: {self.name}, Вид {self.vid}, Возраст {self.age}, Звук {self.sound}")

#Задача 2

class Book:
    def __init__(self, name: str, author: str, kollvo: str):
        self.name = name
        self.author = author
        self.kollvo = kollvo

    def open(self, number_page: int):
        if number_page <= self.kollvo and number_page >= 1:
            print(f"Книга открыта на какой либо из: {self.kollvo} страниц")
        else:
            print(f"Ошибка. Указанная страница не найдена в {self.kollvo} страницах")

    def info(self):
        print(f"Наименование книги: {self.name}, Автор: {self.author}, Количество страниц: {self.kollvo}")

#Задание 3

class PassengerPlane:
    def __init__(self, manufacturer: str, model: str, capacity: int, passenger: int, height: int, speed: int):
        self.manufacturer = manufacturer
        self.model = model
        self.capacity = capacity
        self.passenger = passenger
        self.height = height # м текущая высота
        self.speed = speed # км/ч текущая скорость

    def take_off(self):
        print("Самолет взлетел!")

    def landing(self):
        print("Самолет приземлился!")

    def speed_change(self, speed_1: int):
        if speed_1 >= 0:
            self.speed = speed_1
            print (f"Скорость изменилась на {speed_1} км/ч")
        else:
            print (f"Отрицательная скорость невозможна!")


    def height_change(self, height_1: int):
        if height_1 >= 0:
            self.height = height_1
            print(f"Высота изменилась на {height_1} метров")
        else:
            print(f"Отрицательная высота невозможна!")

    def info(self):
        print(self.manufacturer, self.model, self.capacity, self.passenger, self.height, self.speed)


class MusicAlbum:
    def __init__(self, musician: str, title: str, genre: str, track_list: list[str]):
        self.musician = musician
        self.title = title
        self.genre = genre
        self.track_list = track_list

    def add_track(self, track: str):
        self.track_list.append(track)
        print("Добавлен трек ", track, " в альбом")

    def delete_track(self, track: str):
        self.track_list.remove(track)
        print("Трек ", track, " был удалён из альбома")

    def play_track(self, track: str):
        if track in self.track_list:
            print("Трек ", track, " воспроизводится")
        else:
            print("Такого трека в альбоме под названием ", track, " не существует.")

    def info(self):
        print(self.musician, self.title, self.genre, self.track_list)

