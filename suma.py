class Suma:
    def __init__(self, x):
        self.x = x
    def __add__(self, v):
        sumax = self.x + v.x
        vectorsuma = Suma(sumax)
        return vectorsuma
    def print(self):
        print("Resultado =", self.x)

a = Suma(25)
b = Suma(12)
c= a + b
c.print()


