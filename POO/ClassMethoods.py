class Person:
    year = 2024

    def __init__(self,name,age):
        self.name = name
        self.age = age
    
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
print(vars(p1))


