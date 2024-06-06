from collections import namedtuple

Card = namedtuple("Card",['value','nipe'])

espada = Card("A","Espada")

print(espada)

#optar por typing
from typing import NamedTuple


class Date(NamedTuple):
    value:str = 'default'
    year:int = 2024

d : Date = Date()
print(d)


