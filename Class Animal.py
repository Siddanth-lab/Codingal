from abc import ABC, abstractmethod
class Animal(ABC):
    def move(self):
        pass

class Human(Animal):
    def move (self):
        print("I can walk and run")

class Snake(Animal):
    def move (self):
        print("I can walk and run")

class Dog (Animal):
    def move (self):
        print("I can bark very loud")

class Lion(Animal):
    def move (self):
        print("I can roar with much force")

R=Human()
R.move()

K=Snake()
K.move()

R=Dog()
R.move()

K=Lion()
K.move()