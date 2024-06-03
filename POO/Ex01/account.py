from abc import ABC,abstractmethod
#----------------------------------

class Account(ABC):
    def __init__(self,agencia,conta,saldo) -> None:
        self._agencia = agencia
        self._conta = conta
        self._saldo = saldo
    
    @abstractmethod
    def sacar(self,value):
        ...

    def depositar(self,value):
        self._saldo += value
        print(f'Depositando {value}')
        self.details("Depositado com sucesso!")
    
    def details(self,msg=''):
        print(f'Seu saldo eh : {self._saldo:.2f} - {msg}')

#------------------------------------------
class PoupancaAccount(Account):
    def sacar(self, value):
        previous_value = self._saldo - value
        if previous_value < 0:
            self.details("Saldo insuficiente, saque negado")
            return
        self._saldo -= value
        self.details(f"Saque efetuado: -{value}")

class CourrentAccount(Account):
    def __init__(self, agencia, conta, saldo,limite) -> None:
        super().__init__(agencia, conta, saldo)
        self._limite = limite

    def sacar(self, value):
        previous_value = self._saldo - value
        max_limit = -self._limite
        #cntrl + d
        if previous_value < max_limit:
            self.details("Saldo insuficiente, saque negado")
            return
        self._saldo -= value
        self.details(f"Saque efetuado: -{value}")
    
if __name__ == '__main__':
    accP = PoupancaAccount("111",222,0)
    accP.depositar(1)
    accP.sacar(1)
    print("------------")
    accC = CourrentAccount('122',111,0,100)
    accC.sacar(10)