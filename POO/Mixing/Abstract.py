from abc import ABC,abstractmethod

class AbstractFoo(ABC):
    def __init__(self,name) -> None:
        super().__init__
        self._name = name

    @property
    @abstractmethod
    def name(self):...
    
    @name.setter
    @abstractmethod
    def name(self,name):...



class Foo(AbstractFoo):
    def __init__(self, name) -> None:
        super().__init__(name)
        print("Abstract?")

    @property
    def name(self):
        return self._name
    
    @AbstractFoo.name.setter
    def name(self,name):
        self._name = name
    

f = Foo("bar")
print(f.name)