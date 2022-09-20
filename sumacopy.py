class Suma:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.sumax = x + y
    def print(self):
        print("Resultado =",self.sumax)



a = Suma(5,10)
a.print()

