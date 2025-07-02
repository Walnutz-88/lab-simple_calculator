def main():
    print("Hello from lab-simple-calculator!")
    
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))
    operation = input("Enter an operation (+, -, *, /): ")
    
    if operation == "+":
        output = number1 + number2
    elif operation == "-":
        output = number1 - number2
    elif operation == "*":
        output = number1 * number2
    elif operation == "/":
        if number2 == 0:
            print("Error: Division by zero is not allowed!")
            return
        output = number1 / number2
        
    print("Result: ", output)

if __name__ == "__main__":
    main()
