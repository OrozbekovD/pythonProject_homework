class Person:
    def __init__(self, name, surname, age, id):
        self.name = name
        self.__age = age
        self.surname = surname
        self.__id = id



class Director(Person):
    def __init__(self, name, surname, age, id):
        super().__init__(name, surname, age, id)

    def set_age(self, age):
        if age in range(1, 150):
            self.__age = age
        else:
            raise ValueError('Не допустимое значение возраста! Должно быть положительным числом!')

    def get_age(self):
        return self.__age

    def get_area(self):
        return self.name + self.surname + str(self.__age)


class Teacher(Person):
    def __init__(self, name, surname, age, id):
        super().__init__(name, surname, age, id)

    def set_age(self, age):
        if age in range(1, 150):
            self.__age = age
        else:
            raise ValueError('Не допустимое значение возраста! Должно быть положительным числом!')

    def get_age(self):
        return self.set_age(self.__age)

    def get_area(self):
        return self.name + self.surname + str(self.__age)


class Student(Person):
    def __init__(self, name, surname, age, id):
        super().__init__(name, surname, age, id)

    def set_age(self, age):
        if age in range(1, 150):
            self.__age = age
        else:
            raise ValueError('Не допустимое значение возраста! Должно быть положительным числом!')

    def get_age(self):
        return self.set_age(self.__age)

    def get_area(self):
        return self.name + self.surname + str(self.__age)
