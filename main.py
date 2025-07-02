def main():
    print("Hello from lab-simple-calculator!")
    
    equation = input("Enter an equation (e.g., 1 + 2): ")
    
    number1 = float(equation.split(" ")[0])
    number2 = float(equation.split(" ")[2])
    operation = equation.split(" ")[1]
    
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
    else:
        print("Error: Invalid operation!")
        return
    
    print("Using next-gen AI, the result is: ", output)

if __name__ == "__main__":
    main()
