class TwoDimensionalVector:
    def __init__(self,i,j):
        self.i = i
        self.j = j
    def show(self):
        print(f"Vector({self.i}i,{self.j}j)")

class ThreeDimensionalVector(TwoDimensionalVector):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k = k
    def show(self):
        print(f"Vector({self.i}i,{self.j}j,{self.k}k)")

a = TwoDimensionalVector(4,5)
a.show()
b = ThreeDimensionalVector(4,5,9)
b.show()
