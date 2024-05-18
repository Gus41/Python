class Endereco:
    def __init__(self,rua,numero) -> None:
        self.rua = rua
        self.numero = numero
        

class Client:
    def __init__(self,name) -> None:
        self.name = name
        self.enderecos = []

    def insertEnderecos(self,rua,numero):
        self.enderecos.append(Endereco(rua,numero))
    
    def listarEnderecos(self):
        for end in self.enderecos:
            print(end.rua)


Andre = Client("Andre")
Andre.insertEnderecos("Br-116",123)
Andre.listarEnderecos()
#Quando o objeto Cliente deixar de dexistir, os endereços também irão
class Motor:
    
    def __init__(self,nome) -> None:
        self.nome = nome
    

class Fabricante:
    
    def __init__(self,name):
        self.name = name
        self._carros = []
    
    def inserNewCar(self,car):
        self.carros.append(car)

class Car:
    _motor : Motor
    fabircante : Fabricante

    def __init__(self,name):
        self.name = name
        self._motor = None
        self._fabircante = None

    @property
    def motor(self):
        return self._motor

    @motor.setter
    def motor(self,motor):
        self._motor = motor    

    
