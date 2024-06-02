import enum

#Directions = enum.Enum("Directions",['LEFT','RIGTH'])

class Directions(enum.Enum):
    LEFT = 1
    RIGTH = 2


def move(direction : Directions):
    if not isinstance(direction, Directions):
        raise ValueError("Valor inválido")
    
    print(f'Movendo para {direction}')
    

move(Directions.LEFT)
move(Directions.RIGTH)
print(Directions(1).name)