from typing import Any


class CalMe:
    def __init__(self,phone) -> None:
        self._phone = phone

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        print("Chamando",self._phone,"...")

call = CalMe("123456789876543")
call()
