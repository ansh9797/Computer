from abc import ABC,abstractmethod

class a(ABC):
    def print(self, x):
        print("Value is =", x)

    @abstractmethod

    def a1(self):
        print("Inside abstract method")

class b(a):
    def a1(self):
        print("in class b")

b1 = b()
b1.a1()