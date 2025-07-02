class Calculator:
    def __init__(self, v1, v2):
        self.value1 = v1
        self.value2 = v2

    def add(self):
        print(f'Sum of {self.value1}, {self.value2} is {self.value1 + self.value2}')

    def sub(self):
        print(f'Diff of {self.value1}, {self.value2} is {self.value1 - self.value2}')

calculator1 = Calculator(5, 2)
calculator1.add()
calculator1.sub()
