import json


arq = 'data.json'

class Pessoa:
    def __init__(self,name) -> None:
        self.name = name

p1 = Pessoa("Joana")
p2 = Pessoa("Joao")


data = [vars(p1), vars(p2)]

def createJson():
    with open(arq,'w') as file:
        print("Abrindo arquivo")
        json.dump(data,file,ensure_ascii=False,indent=2)

if __name__ == '__main__':
    print("main, fazendo dump")
    createJson()