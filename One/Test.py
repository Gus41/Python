class Pessoa:
    def __init__(self,name):
        self.name = name

    def saiHy(self):
        print(f'{self.name} is saing hy!')

p1 = Pessoa("Teste")
p1.saiHy()