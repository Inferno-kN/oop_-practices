// ЗАДАЧА 1
// ВАРИАНТ 1
using System;

public interface IMovable
{
    void Move();
}

class Vehicle : IMovable
{
    protected int _speed;
    protected int _year;

    public Vehicle(int speed, int year)
    {
        _speed = speed;
        _year = year;
    }

    public virtual void Move()
    {
        Console.WriteLine("transport is moving");
    }
}

class PersonalTransport : Vehicle, IMovable
{
    protected int _speed;
    protected int _year;
    protected string _master;

    public PersonalTransport(int speed, int year, string master) : base(speed, year)
    {
        Master = master;
    }
}

class PublicTransport : Vehicle, IMovable
{
    protected int _speed;
    protected int _year;
    protected int _capacity;

    public PublicTransport(int speed, int year, int capacity) : base(speed, year)
    {
        Capacity = capacity;
    }
}

class Autobus : PublicTransport
{
    protected int _speed;
    protected int _year;
    protected _capacity;
    protected _conductor;

    public Autobus(int speed, int year, int capacity, string conductor) : base(speed, year, capacity)
    {
        Conductor = conductor;
    }
}

class Scooter : PersonalTransport
{
    protected int _speed;
    protected int _year;
    protected string _master;
    protected int _battery;

    public Scooter(int speed, int year, string master, int battery)
    {
        Battery = battery;
    }
}

class Tram : PublicTransport
{
    protected int _speed;
    protected int year;
    protected int _capacity;
    protected int _number;

    public Tram(int speed, int year, int capacity, int number)
    {
        Number = number;
    }
}

class Car : PersonalTransport
{
    protected int _speed;
    protected int _year;
    protected string _master;
    protected string _model;

    public Car(int speed, int year, string master, string model)
    {
        Master = master;
        Model = model;
    }
}

//ВАРИАНТ 2

public interface IIdentificationFigure
{
    void IdentificationFigure();
}

public class Figure : IIdentificationFigure
{
    protected _size;

    public Figure(int size)
    {
        Size = size;
    }

    public virtual void FindSide()
    {
        Console.WriteLine("В поиске стороны фигуры");
    }

    public virtual void IIdentificationFigure()
    {
        Console.WriteLine("Идентификация фигуры...");
    }
}

class TwoDimensional : Figure
{
    protected int _size;

    public TwoDimensional(int size) : base(size)
}

    public void IIdentificationFigure()
    {
        Console.WriteLine("Это двумерная фигура");
    }
}

class ThreeDimensional : Figure
{
    protected int _size;

    public ThreeDimensional(int size) : base(size)
}

    public void IIdentificationFigure()
    {
        Console.WriteLine("Это трёхмерная фигура");
    }
}

class Orb : ThreeDimensional
{
    protected int _size;
    protected int _radius;

    public Orb(int size, int radius) : base(size)
    {
        Radius = radius;
    }

    public void IIdentificationFigure()
    {
        Console.WriteLine("Это сфера");
    }
}

class Cube : ThreeDimensional
{
    protected int _size;
    protected int _edge;

    public Cube(int size, int edge)
    {
        Edge = edge;
    }

    public void IIdentificationFigure()
    {
        Console.WriteLine("Это куб");
    }
}

class Circle : TwoDimensional
{
    protected int _size;
    protected int _radius;

    public Circle(int size, int radius) : base(size)
    {
        Size = size;
    }

    public void IIdentificationFigure()
    {
        Console.WriteLine("Это круг");
    }
}

class Triangle : TwoDimensional
{
    protected int _size;
    protected int _a;
    protected int _b;
    protected int _c;

    public Triangle(int size, int a, int b, int c)
    {
        A = a;
        B = b;
        C = c;
    }

    public void IIdentificationFigure()
    {
        Console.WriteLine("Это треугольник");
    }
}

class Rectangle : TwoDimensional
{
    protected int _size;
    protected int _width;
    protected int _height;

    public Rectangle(int size, int width, int height)
    {
        Width = width;
        Height = height;
    }

    public void IIdentificationFigure()
    {
        Console.WriteLine("Это прямоугольник");
    }
}

//ВАРИАНТ 3(ПО ЖЕЛАНИЮ)

public interface IProgram
{
    void Run();
}

class Program : IProgram
{
    public void Run()
    {
        Console.WriteLine("Запуск программы...");
    }
}

class OperationSystem : IProgram
{
    public void Run()
    {
        Console.WriteLine("Запуск операционной системы...");
    }
}

class CLI : IProgram
{
    public void Run()
    {
        Console.WriteLine("Запуск CLI...");
    }
}

class AppMobile : IProgram
{
    public void Run()
    {
        Console.WriteLine("Запуск мобильного приложения...");
    }
}

class GraphicEditor : IProgram
{
    public void Run()
    {
        Console.WriteLine("Запуск графического редактора...");
    }
}

class Antivirus : IProgram
{
    public void Run()
    {
        Console.WriteLine("Запуск антивируса...");
    }
}

class GamingPlatform : IProgram
{
    public void Run()
    {
        Console.WriteLine("Запуск игровой платформы...");
    }
}

class AppWeb : IProgram
{
    public void Run()
    {
        Console.WriteLine("Запуск веб-приложения...");
    }
}

class CloudService : IProgram
{
    public void Run()
    {
        Console.WriteLine("Запуск облачного сервиса...");
    }
}

class ConsoleGame : IProgram
{
    public void Run()
    {
        Console.WriteLine("Запуск консольной игры...");
    }
}

// ЗАДАЧА 2
//ВАРИАНТ 1

class FarmAnimal
{
    protected bool skillBreath;
    protected string size;

    public FarmAnimal(bool skillBreath)
    {
        SkillBreath = skillBreath;
    }

    void Breath()
    {
        Console.WriteLine("animal to breath...");
    }
}

class Cow : FarmAnimal
{
    protected bool skillBreath;
    protected string size;

    public Cow(bool skillBreath, string size) : base(skillBreath)
    {
        Size = size;
    }

    void Move()
    {
        Console.WriteLine("cow is moving");
    }
}

class Chicken : FarmAnimal
{
    protected bool skillBreath;
    protected string size;
    public Chicken(bool skillBreath, string size) base(skillBreath)
    {
        Size = size;
    }

    void Move()
    {
        Console.WriteLine("chicken is moving...");
    }
}

class Pig : FarmAnimal
{
    protected bool skillBreath;
    protected string size;

    public Pig(bool skillBreath, string size) : base(skillBreath)
    {
        Size = size;
    }

    void Move()
    {
        Console.WriteLine("pig is moving...");
    }
}

class Sheep : FarmAnimal
{
    protected bool _skillBreath;
    protected string _size;

    public Sheep(bool skillBreath, string size) : base(skillBreath)
    {
        Size = size;
    }

    void Move()
    {
        Console.WriteLine("sheep is moving");
    }
}

//ВАРИАНТ 2

class Account
{
    protected int _number;
    protected float _balance;

    public Account(int number, float balance)
    {
        Number = number;
        Balance = balance;
    }

    void MoneyAccount()
    {
        if Balance > 0
            Console.WriteLine("На вашем счету есть несколько денежных средств");
        else
            Console.WriteLine("Пополните счёт");
    }
}

class CreditAccount : Account
{
    protected int _number;
    protected float _balance;
    protected float _credit;

    public CreditAccount(int number, float balance, float credit) : base(number, balance)
    {
        Credit = credit;
    }

    void CreditLimit()
    {
        if Credit == 0
            Console.WriteLine("Кредитный лимит карты был исчерпан");
        else
            Console.WriteLine("На вашей кредитной карте ещё есть средства");
    }
}

class DebitAccount : Account
{
    protected int _number;
    protected float _balance;

    public DebitAccount(int number, float balance) : base(number, balance)

    void MakeDeposit()
    {
        Balance += 150;
        Console.WriteLine("Вы успешно добавили на баланс 150 рублей");
    }
}

// ЗАДАЧА 3

class Human
{
    protected string _name;

    public Human(string name)
    {
        Name = name;
    }

    void GetName()
    {
        return Name
    }
}

class FlightAttendant : Human
{
    protected string _name;
    protected int _age;

    public FlightAttendant(string name, int age) : base(name)
    {
        Age = age;
    }
    public void HelpPassengers()
    {
        Console.WriteLine("Помогаю пассажирам...");
    }
}

class Passenger : Human
{
    protected string _name;
    protected int _age;
    protected bool _luggage;
    protected bool _hand_luggage;

    public Passenger(string name, int age, bool luggage, bool hand_luggage) : base(name)
    {
        Age = age;
        Luggage = luggage;
        HandLuggage = handLuggage;
    }

    public void SearchPlace()
    {
        Console.WriteLine("Ищу свое место в самолёте...");
    }
}

class Pilot : Human
{
    protected string _name;
    protected int _age;
    protected int _experience;

    public Pilot(string name, int age, int experience)
    {
        Age = age;
        Exp = experience;
    }

    void Fly()
    {
        Console.WriteLine("Господа и дамы, мы взлетаем..!")
    }
}
