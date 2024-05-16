from ConvertJson import arq,Pessoa,createJson
import json




with open(arq,'r') as file:
    data = json.load(file)

    p1 = Pessoa(**data[0])
    p2 = Pessoa(**data[1])
    print(vars(p1))
    print(vars(p2))