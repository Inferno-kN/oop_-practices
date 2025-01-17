// Задача 1

class Patient
{
    string fio;
    int age;
    string zabolev;

    Patient(string fio, int age, string zabolev)
    {
        this.fio = fio;
        this.age = age;
        this.zabolev = zabolev;
    }

    void Zapis(string date, string time)
    {
        this.date = date;
        this.time = time:
    }
    void Info()
    {
        Console.WriteLine($"ФИО: {this.fio}, Возраст: {this.age}, Текущее заболевание: {this.zabolev}");
    }
}

// Задача 2

class TouristSpot
{
    string place;
    string country;
    string dostopr;

    TouristSpot(string place, string country, string dostopr)
    {
        this.place = place;
        this.country = country;
        this.dostopr = dostopr;
    }

    void VisitPlace(string name)
    {
        this.name = name;
    }
    void Info()
    {
        Console.WriteLine($"Место: {this.place}, Страна: {this.country}, Достопримечательность: {this.dostopr}");
    }
}

// Задача 3

class ModelWindow

WidthScreen = 1960 //ширина экрана, а это горизонталь gorizont
HeightScreen = 1080 //высота экрана, то есть вертикаль vertikal

{
    string title;
    int koord;
    int vertikal;
    int gorizont;
    string color;
    bool visible;
    bool frame;

    ModelWindow(string title, int koord, int vertikal, int gorizont, string color, bool visible, bool frame)
    {
        this.title = title;
        this.koord = koord;
        this.vertikal = vertikal;
        this.gorizont = gorizont;
        this.color = color;
        this.visible = visible;
        this.frame = frame;
    }

    bool MovementVertikal()
    {
        if 0 <= this.vertikal <= ModelWindow.HeightScreen
            Console.WriteLine($"Окно по вертикали {this.vertikal} двигается или находится в состоянии покоя на высоте {ModelWindow.HeightScreen} экрана");
            return True
        else
            Console.WriteLine($"Окно по вертикали {this.vertikal} не может превышать высоту {ModelWindow.HeightScreen} экрана");
            return False
    }

    bool MovementGorizont()
    {
        if 0 <= this.vertikal <= ModelWindow.WidthScreen
            Console.WriteLine($"Окно по горизонтали {this.gorizont} двигается или находится в состоянии покоя на ширине {ModelWindow.WidthScreen} экрана");
            return True
        else
            Console.WriteLine($"Окно по горизонтали {this.gorizont} не может превышать ширину {ModelWindow.WidthScreen} экрана");
            return False
    }

    void HeightChange(int height)
    {
        this.height = height;
    }

        if 0 <= height <= ModelWindow.HeightScreen
            Console.WriteLine($"Высота изменилась на {this.height} сантиметров");
        else
            Console.WriteLine($"Отрицательная высота или высота, превышающая высоту экрана невозможна!");

    void WidthChange(int width)
    {
        this.width = width;
    }
        if 0 <= width <= ModelWindow.WidthScreen
            Console.WriteLine($"Ширина изменилась на {this.width} сантиметров");
        else
            Console.WriteLine($"Отрицательная ширина или ширина, превышающая ширину экрана невозможна!");

    bool UpdateColor(string NewColor)
    {
        this.NewColor = NewColor;
    }
        if this.color != this.NewColor
            Console.WriteLine($"Цвет {this.color} остался без изменений");
            return False;
        else
            Console.WriteLine($"Цвет {this.color} был изменён на {this.NewColor}");
            return True;

    bool UpdateFrame(string NewFrame)
    {
        this.NewFrame = NewFrame;
    }
        if this.frame != this.NewFrame
            Console.WriteLine($"Рамка {this.frame} осталось такой же");
            return False;
        else
            Console.WriteLine($"Рамка {this.frame} была изменена на рамку {this.NewFrame}");
            return True;

    void StringInfo()
    {
        return ($"Заголовок окна: this.title}, Координаты левого верхнего угла: {this.koord},\nРазмер по горизонтали, Размер по вертикали:{this.gorizont}, {this.vertikal}, Цвет окна: {this.color}, Cостояние видимое/невидимое: {this.visible}, состояние с рамкой/без рамки: {this.frame}");
    }
}