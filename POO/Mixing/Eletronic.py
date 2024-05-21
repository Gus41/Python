from log import LogFileMixin
class Eletronic:
    def __init__(self,name) -> None:
        self._name = name
        self._stateOn = False
    def On(self):
        self._stateOn = True
    def Off(self):
        self._stateOn = False

class SmartPhone(Eletronic, LogFileMixin):
    def On(self):
        super().On()

        self.logSucces(f'{self._name} foi ligado')


    def Off(self):
        super().Off()
        self.LogError(f'{self._name} foi desligado')