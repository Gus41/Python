from collections.abc import Iterable,Sequence
from typing import Iterator

#Optar por Sequence

class MyList(Sequence):
    def __init__(self) -> None:
        self._data = {}
        self._index = 0
        self._next_index = 0

    def append(self,value): 
        self._data[self._index] = value
        self._index += 1
        
    def __iter__(self) -> Iterator:
        return super().__iter__()
    def __len__(self) -> int:
        return self._index
    def __getitem__(seld,index):
        
        return seld._data[index]
    def __iter__(self):
        return self
    
    def __next__(self):
        val = self._data[self._next_index]
        self._




if __name__ == '__main__':
    lista = MyList()
    lista.append(1)
    lista.append(2)
    for item in lista:
        print(item)