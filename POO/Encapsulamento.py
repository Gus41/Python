class Foo:
    def __init__(self) -> None:
        self.public = "public atribute"
        self._proteced = "protected atribute" #um underline == proteced (acessar na classe e nas suas filhas )
        self.__private = "private atribute" #dois underlines == private ( apenas dentro da classe )
    def publicMethod(self):
        return "publicMethod"

f = Foo()
print(f.publicMethod())


class Carrinho:
    def __init__(self) -> None:
        self._products = []

    def total(self):
        return sum([p.value for p in self._products])
    
    def listProducts(self):
        print()
        for p in self._products:
            print(p.name, p.value)
        print()

    def insertProcuts(self, *products):
        for product in products:
            self._products.append(product)



class Product:
    def __init__(self,name,value) -> None:
        self.name = name
        self.value = value

p1,p2 = Product("Produto1",30), Product("Produto2",10)

carrinho = Carrinho()
carrinho.insertProcuts(p1,p2)
carrinho.listProducts()
print(carrinho.total())