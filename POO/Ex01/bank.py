import people
import account


class Bank:
    def __init__(self,name:str = 'default',
                 agencias : list[int] | None = None,
                 clientes : list[people.Pessoa] | None = None,
                 contas : list[account.Account] | None = None
    ) -> None:
        self._name = name
        self._clientes = clientes or []
        self._agencias = agencias or []
        self._contas = contas or []

    @property
    def name(self):
        return self._name
    @property
    def agencias(self):
        return self._agencias
    @property
    def contas(self):
        return self._contas
    
    def authCliente(self,cliente:people.Cliente):
        if cliente not in self._clientes:
            return False
        return True

    def authConta(self,conta: account.Account):
        if conta not in self._contas:
            return False
        return True

    def authAgencia(self,conta:account.Account):
        if conta._agencia not in self._agencias:
            return False
        return True
    
    def auth(self,cliente : people.Cliente , account : account.Account):
        return self.authAgencia(account) and self.authCliente(cliente) and self.authConta(account)
    
    def __repr__(self) -> str:
        return f'Bank({self._agencias} , {self._clientes})'
    


if __name__ == '__main__':
    c1 = people.Cliente('Luiz', 30)
    c1.conta = account.CourrentAccount(111, 222, 0, 0)
    print(c1)
    print(c1.conta)
    c2 = people.Cliente('Maria', 18)
    c2.conta = account.CourrentAccount(112, 223, 100)
    print(c2)
    print(c2.conta)
    bank = Bank()
    bank._clientes.extend([c1,c2])
    bank._agencias.extend([111,222])
    print(bank.auth(c1,c1.conta))
    print(bank)