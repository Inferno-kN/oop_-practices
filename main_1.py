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





class Animal // Задача 1
{
    string name;
    string vid;
    int age;
    string sound;

    Animal(string name, string vid, int age)
    {
        this.name = name;
        this.vid = vid;
        this.age = age;
    }

    void Sound(string sound)
    {
        this.sound = sound;
    }
    void Info()
    {
        Console.WriteLine($"Имя: {this.name}, Вид: {this.vid}, Возраст: {this.age}, Звук: {this.sound}");
    }
}

// Задача 2

class Book
{
    string name;
    string author;
    string kollvo;

    Book(string name, string author, string kollvo)
    {
        this.name = name;
        this.author = author;
        this.kollvo = kollvo;
    }

    void Open(int NumberPage)
    {
        if (NumberPage <= kollvo && NumberPage >= 1)
    }
        Console.WriteLine($"Книга открыта на какой либо из: {this.kollvo} страниц");
        else
        {
        Console.WriteLine($"Ошибка. Указанная страница не найдена в {this.kollvo} страницах");
        }
    void Info()
    {
        Console.WriteLine($"Наименование книги: {this.name}, Автор: {this.author}, Количество страниц: {this.kollvo}")
    }
}

// Задание 3

class PassengerPlane:
{
    string manufacturer;
    string model;
    int capacity;
    int passenger;
    int height;
    int speed;

    PassengerPlane(string manufacturer, string model, int capacity, int passenger, int height, int speed)
    {
        this.manufacturer = manufacturer;
        this.model = model;
        this.capacity = capacity;
        this.passenger = passenger;
        this.height = height;
        this.speed = speed;
    }

    void TakeOff
    {
        Console.WriteLine($"Самолет взлетел!");
    }

    void Landing
    {
        Console.WriteLine($"Самолет приземлился!");
    }

    void SpeedChange(int speed_1)
    {
        if speed_1 >= 0
            this.speed = speed_1;
            Console.WriteLine($"Скорость изменилась на {speed_1} км/ч");
        else
            Console.WriteLine($"Отрицательная скорость невозможна!");
    }

    void Height_Change(int height_1)
    {
        if height_1 >= 0
            this.height = height_1;
            Console.WriteLine($"Высота изменилась на {height_1} метров");
        else
            Console.WriteLine($"Отрицательная высота невозможна!");
    }

    void Info
    {
        Console.WriteLine($"Производитель самолета: {this.manufacturer}, Модель: {this.model}, Вместимость: {this.capacity}, Пассажиры: {this.passenger}, Текущая высота: {this.height}, Текущая скорость: {this.speed}");
    }
}

class MusicAlbum
{
    string musician;
    string title;
    string genre;
    List <string> TrackList;

    MusicAlbum(string musician, string title, string genre, List <string> TrackList)
    {
        this.musician = musician;
        this.title = title;
        this.genre = genre;
        this.TrackList = TrackList;
    }

    void AddTrack(string track)
    {
        this.AddTrack.append(track);
        Console.WriteLine("Добавлен трек ", track, " в альбом");
    }

    void DeleteTrack(string track)
    {
        this.DeleteTrack.remove(track);
        Console.WriteLine("Трек ", track, " был удалён из альбома");
    }

    void PlayTrack(string track)
    {
        if track in this.TrackList
            Console.WriteLine("Трек ", track, " воспроизводится");
        else
            Console.WriteLine("Такого трека в альбоме под названием ", track, " не существует.");
    }

    void Info
    {
        Console.WriteLine($"Музыкант: {this.musician}, Название: {this.track}, Жанр: {this.genre}, Список треков: {this.TrackList}");
    }

}