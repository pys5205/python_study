class Calculate:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        res = self.first + self.second
        return res
    
    def sub(self):
        res = self.first - self.second
        return res
    
    def mul(self):
        res = self.first*self.second
        return res
    
    def div(self):
        res = self.first/self.second
        return res

i= int(input('i=>'))
j= int(input('j=>'))
calc = Calculate(i, j)
print(calc.add())
print(calc.sub())
print(calc.mul())
print(calc.div())