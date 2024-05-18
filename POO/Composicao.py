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

#Quando o objeto Cliente deixar de dexistir, os endereços também irão
