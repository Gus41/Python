
from typing import Any


class Multiply:
    def __init__(self, args) -> None:
        print("Argumentos passados: ", args)
        self._func = args
        self._z = 10
    
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        result = self._func(*args,**kwds)
        return self._z * result


@Multiply
def sum(x,y):
    return x+y

result = sum(2,2)
print(result)