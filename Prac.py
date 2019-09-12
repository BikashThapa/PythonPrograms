class Person:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print(f'Hi, this is {self.name} here')


person1 = Person("Biaksh Thapa")
person1.talk()

Bob = Person("Bob")
Bob.talk()