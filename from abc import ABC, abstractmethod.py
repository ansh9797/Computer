from abc import ABC, abstractmethod

class animals(ABC):
    def move(self):
        pass

class snake(animals):
    def move(self):
        print("I can crowl.")

class lion(animals):
    def move(self):
        print("I can walk.")

s1= snake()
s1.move()

l1 = lion()
l1.move()