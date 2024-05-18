class Pessoa:
    def __init__(self,name) -> None:
        self.name = name

    def saiHy(self):
        print(self.__class__)

class Cliente(Pessoa):
    def __init__(self, name) -> None:
        super().__init__(name)

class Aluno(Pessoa):
    def __init__(self, name) -> None:
        super().__init__(name)
