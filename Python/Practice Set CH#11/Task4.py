class Complex:
    def __init__(self, r, i):
        self.r = r
        self.i = i
    
    def __add__(self, n):
        return Complex(self.r + n.r, self.i + n.i)
    
    def __mul__(self, n):
        real = self.r * n.r - self.i * n.i
        imag = self.r * n.i + self.i * n.r
        return Complex(real, imag)

    def __str__(self):
        return f"{self.r}+{self.i}i"


c1 = Complex(1, 2)
c2 = Complex(4, 5)

print(c1 + c2)   # 5+7i
print(c1 * c2)   # -6+13i
