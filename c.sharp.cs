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