# Funções decoradoras e decoradores com classes

def meu_repr(self):
    class_name = self.__class__.__name__
    class_dict = self.__dict__
    class_repr = f'{class_name}({class_dict})'
    return class_repr


def adiciona_repr(cls):
    cls.__repr__ = meu_repr
    return cls


@adiciona_repr
class Time:
    def __init__(self, nome):
        self.nome = nome



def my_planet(method):
    def internFunction(self, *arg, **kwargd):
        result = method(self)

        if 'Terra' in result:
            return "Terra, voce esta em casa"
        return result
    return internFunction


@adiciona_repr
class Planeta:
    def __init__(self, nome):
        self.nome = nome

    @my_planet
    def sayName(self):
        return f'O planeta é : {self.nome}'
    




brasil = Time('Brasil')
portugal = Time('Portugal')

terra = Planeta('Terra')
marte = Planeta('Marte')

print(terra.sayName())