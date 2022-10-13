from abc import ABC, abstractmethod

#abstractclass
class AbstractDemo(ABC):
    #abstractmethod
    @abstractmethod
    def sk(self):
        None
class ConcreteClass(AbstractDemo):
    def sk(self):
        print("this is function")
obj=ConcreteClass()
obj.sk()

    