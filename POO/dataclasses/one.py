from dataclasses import dataclass,field

@dataclass(init=False) #tira o init da dataclass  (tem que definir)
class Pessoa:
    name:str
    age:int
    def __init__(self,name:str,age:int) -> None:
        print("init")
        self.name = name
        self.age = age
    
    def __post_init__(self):
        print("pós init")
    @property
    def data(self):
        d = f'{self.name} - {self.age}'
        return d
    @data.setter
    def data(self,value : str):
        self.name, self.age = value.split(" - ")


@dataclass(frozen=True)
class Fr:
    name:str

@dataclass
class Def_:
    value:str = 'default_value'
    test : list[str] = field(default_factory=list)

if __name__ == "__main__":
    p1 = Pessoa("Luiz",30)
    print(p1)
    p1.data = "Luiz - 31"
    print(p1.data)
    f = Fr("Teste")
    print(f)
    defa = Def_()
    print(defa)
