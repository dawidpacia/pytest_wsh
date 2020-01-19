class Calculator:

    def add(self, x, y):
        return x + y

    def sub(self, x, y):
        return x - y

    def mul(self, x, y):
        return x * y

    def div(self, x, y):
        if y == 0:
            return False
        return x / y

if __name__ == "__main__":
    calculator = Calculator()
    print(calculator.add(1, 2))
