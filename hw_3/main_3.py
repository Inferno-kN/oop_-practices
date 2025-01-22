#Задача 1
class Spell:
    def __init__(self, name: str, difficulty: int, spell_type: str, description: str):
        self.__name = name
        self.__difficulty = difficulty
        self.__spell_type = spell_type
        self.__description = description

    def get_name(self) -> str:
        return self.__name

    def get_difficulty(self) -> int:
        return self.__difficulty

    def get_spell_type(self) -> str:
        return self.__spell_type

    def get_description(self) -> str:
        return self.__description

    def set_name(self, name: str):
        self.__name = name

    def set_difficultu(self, difficulty):
        self.__difficulty = difficulty

    def set_spell_type(self, spell_type):
        self.__spell_type = spell_type

    def set_description(self, description):
        self.__description = description


    def __str__(self):
        return f"Название заклинания: {self.__name}, Уровень сложности: {self.__difficulty}, Тип заклинания: {self.__spell_type}, Описание: {self.__description}"


class Wizard:
    def __init__(self, name: str, house: str, power_level: int, spells: list[Spell], status="Hogwarts"):
        self.__name = name
        self.__house = house
        self.__power_level = power_level
        self.__spells = spells
        self.__status = status

    def get_name(self)-> str:
        return self.__name

    def get_house(self) -> str:
        return self.__house

    def get_power_level(self) -> int:
        return self.__power_level

    def get_spells(self) -> list[Spell]:
        return self.__spells

    def get_status(self) -> str:
        return self.__status

    def set_name(self, name: str):
        self.__name = name

    def set_house(self, house: str):
        self.__house = house

    def set_power_level(self, power_level: int):
        self.__power_level = power_level

    def set_status(self, status: str):
        self.__status = status

        if status not in ["Hogwarts", "Graduated"]:
            raise ValueError("Статус должен быть 'Hogwarts' или 'Graduated'")


    def add_spell(self, spell: list[Spell]):
        self.__spells.append(spell)
        print(f"Заклинание {spell} было добавлено")

    def remove_spell(self, spell: list[Spell]):
        if spell in self.__spells:
            self.__spells.remove(spell)
            print(f"Заклинание {spell} было удалено")


    def __str__(self):
        return f"Имя волшебника: {self.__name}, Факультет: {self.__house}, Уровень магической силы{self.__power_level}, Список заклинаний: {self.__spells}, Статус: {self.__status}."


#Задача 2

class Employee: #position - должность, department - отдел, salary - зп, exp - опыт работы
    def __init__(self, name: str, position: str, department: str, salary: int, experience: int, projects: list[str]):
        self.__name = name
        self.__position = position
        self.__department = department
        self.__salary = salary
        self.__experience = experience
        self.__projects = projects

    def get_name(self) -> str:
        return self.__name

    def get_position(self) -> str:
        return self.__position

    def get_department(self) -> str:
        return self.__department

    def get_salary(self) -> int:
        return self.__salary

    def get_exp(self) -> int:
        return self.__experience

    def get_project(self) -> list[str]:
        return self.__projects

    def set_name(self, name: str):
        self.__name = name

    def set_positon(self, position: str):
        self.__position = position

    def set_department(self, department: str):
        self.__department = department

    def set_exp(self, experience: int):
        self.__experience = experience

    def set_salary(self, salary: int):
        self.__salary = salary
        new_salary = self.__salary + (self.__salary // 3)
        print(f"Текущая зарплата {self.__salary} стала {new_salary}")


    def add_projects(self, project: list[str]):
        self.__projects.append(project)
        print(f"Проект под названием {project} был добавлен")

    def remove_project(self, project: list[str]):
        if project in self.__projects:
            self.__projects.remove(project)
        print(f"Проект под названием {project} был удален из списка {self.__projects}")

    def __str__(self):
        return f"Имя сотрудника: {self.__name}, Должность: {self.__position}, Отдел: {self.__department}, Зарплата: {self.__salary}, Стаж работы: {self.__experience}, Список выполненных проектов: {self.__projects}."



#Задача 3

class Robot:
    def __init__(self, number: int, model: str, current_task: str, lvl_battery: int, status="On break"):
        self.__number = number
        self.__model = model
        self.__current_task = current_task
        self.__lvl_battery = lvl_battery
        self.__status = status

    def get_number(self) -> int:
        return self.__number

    def get_model(self) -> str:
        return self.__model

    def get_current_task(self) -> str:
        return self.__current_task

    def get_lvl_battery(self) -> int:
        return self.__lvl_battery

    def get_status(self) -> str:
        return self.__status

    def set_number(self, number: int):
        self.__number = number

    def set_model(self, model: str):
        self.__model = model

    def add_task(self, new_task: str):
        lst = []
        lst.append(self.__current_task)
        lst.append(new_task)
        print(f"В список {lst} была добавлена не только текущая задача {self.__current_task}, но и новая задача {new_task}")

    def battery_change(self, new_lvl_battery):
        self.__lvl_battery += new_lvl_battery
        print(f"Текущий заряд батареи {self.__lvl_battery} был изменён на {new_lvl_battery}")
        max_value = 100
        min_value = 0
        if min_value < self.__lvl_battery <= max_value:
            print(f"Статус {self.__status} робота = On work")
        elif min_value == self.__lvl_battery:
            print(f"Статус {self.__status} робота = On break")

    def __str__(self):
        return f"Серийный номер: {self.__number}, Модель: {self.__model}, Текущая задача: {self.__current_task}, Уровень заряда батареи: {self.__lvl_battery}, Состояние: {self.__status}."


#Задача 4

class Achievement:
    def __init__(self, title: str, year: int):
        self.__title = title
        self.__year = year

    def get_title(self) -> str:
        return self.__title

    def get_year(self) -> int:
        return self.__year

    def set_title(self, title: str):
        self.__title = title

    def set_year(self, year: int):
        self.__year = year

class Athlete:
    def __init__(self, name: str, age: int, sport: str, achievements: list[Achievement], status: str="Active"):
        self.__name = name
        self.__age = age
        self.__sport = sport
        self.__achievements = achievements
        self.__status = status

    def get_name(self) -> str:
        return self.__name

    def get_age(self) -> int:
        return self.__age

    def get_sport(self) -> str:
        return self.__sport

    def get_achievement(self) -> list[Achievement]:
        return self.__achievements

    def get_status(self) -> str:
        return self.__status

    def set_name(self, name: str):
        self.__name = name

    def set_age(self, age: int):
        self.__age = age

    def set_sport(self, sport: str):
        self.__sport = sport

    def set_status(self, status: str):
        if status not in ["Active", "Retired"]:
            raise ValueError("Статус должен быть либо 'Active' либо 'Retired'")
        self.__status = status

    def add_achievement(self, achievement: Achievement):
        self.__achievements.append(achievement)

    def remove_achievement(self, achievement: Achievement):
        self.__achievements.remove(achievement)

    def __str__(self):
        return f"Имя атлета: {self.__name}, Возраст: {self.__age}, Вид спорта: {self.__sport}, Список достижений: {self.__achievements}, Текущий статус: {self.__status}."