class Person:
    year = 2024
    name:str
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self._propriedade = 'private'
    
    #atributos que começam com um ou dois underlines
    #não deve ser usado fora da classe

    def getName(self):
        return self.name
    
    @property
    def propriedade(self):
        return self._propriedade
    
    @propriedade.setter
    def propriedade(self,prop):
        if prop == 'value':
            raise ValueError("Error")
        self._propriedade = prop

    
    def saiHy(self):
        print(f'{self.name} is saing Hy!')

    @classmethod
    def method(cls):
        print("Static method")

    @classmethod
    def createWithAgeEqual(cls,name):
        return cls(name,20)
    
Person.method()
p1 = Person.createWithAgeEqual('Person20Old')
p1.propriedade = 'value'
print(vars(p1))


