class A:
    ...
    def method(self):
        print("Hello, A")

class B(A):
    ...
    def method(self):
        print("Hello, B")

class C(A):
    ...
    def method(self):
        print("Hello, C")

class D(B,C):
    ...
  

d = D()
d.method()