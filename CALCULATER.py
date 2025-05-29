print()
print("-"*120)
print("                                              WELCOME TO CALC WORLD")
print("*"*120)
for i in range(1,500):
    com = int(input("to start or continue the calcunation press 1 or press 2 for exit or press 3 for know about our oparaters............."))
    if  com == 1:
        num1 = int(input("Enter the first number: "))
        ope = input("Enter the your operater from (+,-,*,/,//,%,**) : - ")
        num2 = int(input("Enter the second number: "))
        match ope:
            case '+':
                print("The sum of", num1, "and", num2, "is: - ", num1 + num2)
            case '-':
                print("The difference between", num1, "and", num2, "is: - ", num1 - num2)
            case '*':
                print("The product of", num1, "and", num2, "is: - ", num1 * num2)
            case '/':
                print("The division of", num1, "by", num2, "is: - ", num1 / num2)
            case '//':
                print("The floor division of", num1, "by", num2, "is: - ", num1 // num2)
            case '%':
                print("The modulus of", num1, "and", num2, "is: - ", num1 % num2)
            case '**':
                print("The power of", num1, "to the exponent of", num2, "is: - ", num1 ** num2)
        3
        print("="*120)
    elif com == 2:
        print("thank you for visiting")
        break
    elif com == 3:
        print("1. + = use for addition ") 
        print("2. - = use for substraction")
        print("3. * = use for multiplication")
        print("4. / = use for division")
        print("5. // = use for floor division")
        print("6. % = use for modulus")
        print("7. ** = use for power")
        print("="*120)

