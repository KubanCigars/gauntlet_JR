class Calculator():
    def __init__(self,num1,num2,operator):
#this is where the two numbers and the operator are defined
        self._num1 = num1
        self._num2 = num2
        self._operator = operator
#self explantory, all the calculator functions are here        
    def add(self):
        return self._num1 + self._num2
        
    def subtract(self):
        return self._num1 - self._num2
        
    def multiply(self):
        return self._num1 * self._num2
    
    def divide(self):
        return self._num1 / self._num2
        
    def power(self):
        return self._num1 ** self._num2

def main():
    calc = []
    calc_input= input("Enter the number you would like to calculate: ")
    calc = calc_input.split(" ")
    #this means that there has to be a space, I have not found a way to split the string without a space
    try:
        num1 = float(calc[0])
        num2 = float(calc[2])
        operator = calc[1]
    #all this is in a try and except block to catch if a string is entered instead of a number
        match operator:
            case "+":
                print(Calculator(num1, num2, operator).add())
            case "-":
                print(Calculator(num1, num2, operator).subtract())
            case "*":
                print(Calculator(num1, num2, operator).multiply())
            case "/":
                print(Calculator(num1, num2, operator).divide())
            case "^":
                print(Calculator(num1, num2, operator).power())
    except ValueError:
        print("Invalid input")
        return
    
if __name__ == "__main__":
    main()
    
    
    
    



