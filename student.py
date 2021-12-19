class Human:
    def __init__(self, name, color, age, gender, height, weight):
        self.name = name
        self.color = color
        self.age = age
        self.gender = gender
        self.height = height
        self.weight = weight

class Student(Human):
    def __init__(self, name, color, age, gender, height, weight, homeworks):
        super().__init__(name, color, age, gender, height, weight)     
        self.homeworks = homeworks

    def study(self):
        print(f"{self.name} делает {self.homeworks + 1} домашку")


dima = Student('Дима', 'блондин', 16, 'мужской', 170, 65, 15) 
dima.study()

dasha = Student('Даша', 'брюнетка', 17, 'женский', 167, 55, 21) 
dasha.study()