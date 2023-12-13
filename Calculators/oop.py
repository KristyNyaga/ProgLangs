class Calculator:
    def __init__(self, num1, num2, choice):
        self.num1 = num1
        self.num2 = num2
        self.choice = choice

    def add(self):
        return self.num1 + self.num2
       
    def subtract(self):
        return self.num1 - self.num2
    
    def multiply(self):
        return self.num1 * self.num2
    #Exception handling
    def divide(self):
        try:
          return self.num1 / self.num2
        except ZeroDivisionError:
            print("Cannot divide by zero.Please try again")
    
    def takeinput(self):
        self.num1 = int(input("Enter the first number "))
        self.num2 = int(input("Enter the second number "))
        self.choice = str(input("Please enter what operation you would like to undertake(+ - * /) "))

    def evaluate_choice(self):
        if self.choice == "+":
            return self.add()
        elif self.choice == "-":
            return self.subtract()
        elif self.choice == "*":
            return self.multiply()
        elif self.choice == "/":
            return self.divide()
        else:
            print("Please enter a valid choice")

def main():
        calculator = Calculator(num1=None, num2=None, choice=None)
        #calculator = Calculator(12,7,"add")
        calculator.takeinput()
        calculator.evaluate_choice()
        print(calculator.evaluate_choice())

if __name__ == "__main__":
    main()