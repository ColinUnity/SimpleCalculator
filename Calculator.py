print("to turn on calculator say \"yes\"") #asks if user wants to open calculator

turn_on = input("calculator start?") #creates variable to hold the user input that will start the calculator

if turn_on == ("yes"): #if the user says "yes" then runs the calculator

    number1 = input("number 1 ") #asks the first number 
    
    operation = input("operation ") #asks for operation
    
    number2 = input("number 2 ") #asks for second number
    
    if operation == ("+"): #if player states "+" as operation, adds the two numbers
        add = int(number1) + int(number2) #turns the operation into a intiger, and adds them together
        print(str(number1) + " + " + str(number2) + " = " + str(add)) # prints the equation with the answer
    
    if operation == ("-"): #if player states "-" as operation, subtracts the two numbers
        subtract = int(number1) - int(number2) #turns the operation into a intiger, and subtracts them together
        print(str(number1) + " - " + str(number2) + " = " + str(subtract)) # prints the equation with the answer
    
    if operation == ("*"): #if player states "*" as operation, adds the two numbers
        multiply = int(number1) * int(number2) #turns the operation into a intiger, and adds them together
        print(str(number1) + " * " + str(number2) + " = " + str(multiply)) # prints the equation with the answer
    
    if operation == ("/"): #if player states "/" as operation, divide the two numbers
        divide = int(number1) / int(number2) #turns the operation into a intiger, and divide them together
        print(str(number1) + " / " + str(number2) + " = " + str(divide)) # prints the equation with the answer

if turn_on == ("no"):
    exit()
