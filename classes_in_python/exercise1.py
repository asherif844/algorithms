class Robot:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def introduce_self(self):
        print('My name is ' + self.name)  # 'this' equivalent in Java


r1 = Robot('Tom', 'red', 30)
r2 = Robot('Jerry', 'blue', 40)

r1.introduce_self()
r2.introduce_self()


class Person:
    def __init__(self, name, personality, isSitting, robotOwned):
        self.name = name
        self.personality = personality
        self.isSitting = isSitting
        self.robotOwned = robotOwned

    def stand_up(self):
        self.isSitting = False

    def sit_down(self):
        self.isSitting = True


p1 = Person('Alice', 'Aggressive', False, r2)
p2 = Person('Becky', 'Talkative', True, r1)