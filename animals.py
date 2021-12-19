class Animals:
    def __init__(self, name, color, age, gender):
        self.name = name
        self.color = color
        self.age = age
        self.gender = gender
    
    def sleep(self, time):
            print(f'{self.name} проспал(а) {time} час(а/ов)')

    def eat(self, food):
        print(f'{self.name} съел(а) {food}')


class Mammals(Animals):
    def __init__(self, name, color, age, gender, hunter=False):
        super().__init__(name, color, age, gender)
        self.hunter = hunter

    def hunting(self):
        if self.hunter == True:
            print(f"{self.name} может охотиться")
    
    def feed(self, child):
        if self.gender.lower() == "женский":
            print(f"{self.name} кормит {child.name}")
        else:
            print("не может кормить")

    
class Human(Mammals):
    def __init__(self, name, color, age, gender, hunter, education, clothes):
        super().__init__(name, color, age, gender, hunter)
        self.education = education
        self.clothes = clothes

    def be_friends(self):
        print(f"{self.name} дружит с кем-то")


class Dog(Mammals):
    def __init__(self, name, color, age, gender, hunter, master):
        super().__init__(name, color, age, gender, hunter)
        self.master = master

    def talk(self):
        print("гав")

    def walk(self):
        print(f"{self.name} гуляет вместе с {self.master}")


class Cat(Mammals):
    def __init__(self, name, color, age, gender, hunter, game):
        super().__init__(name, color, age, gender, hunter)
        self.game = game

    def talk(self):
        print("мяу")

    def play(self):
        print(f"{self.name} играет с {self.game}")


print()
bird = Animals('Кеша', 'красный', 3, 'мужской')
bird.eat('зерно')
bird.sleep(1)

print()
teddy_bear = Mammals('Тэдди', 'бурый', 1.5, 'мужской', True)
teddy_bear.eat('рыбу наверное')

print()
bear = Mammals('Маша', 'черный', 6, 'женский', True)
bear.eat('мед')
bear.feed(teddy_bear)
bear.hunting()

print()
human = Human('Катя', 'рыжая', 13, 'женский', True, 'школа', 'платье')
human.be_friends()
human.eat('конфету')

print()
dog = Dog('Джек', 'белый', 4, 'мужской', True, 'Катя')
dog.talk()
dog.hunting()
dog.walk()

print()
cat = Cat('Шустрик', 'Рыжий', 7, 'мужской', True, 'клубок')
cat.talk()
cat.hunting()
cat.play()

