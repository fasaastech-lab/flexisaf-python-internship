from week10_math_tools import add, subtract, multiply, divide



while True:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Choose an operation: ")
    if choice == "1":
        a = float(input("Enter a: "))
        b = float(input("Enter b: "))
        sum = add(a, b)
        print(sum)

    elif choice == "2":
        a = float(input("Enter a: "))
        b = float(input("Enter b: "))
        difference = subtract(a, b)
        print(difference)

    elif choice == "3":
        a = float(input("Enter a: "))
        b = float(input("Enter b: "))
        product = multiply(a, b)
        print(product)

    elif choice == "4":
        a = float(input("Enter a: "))
        b = float(input("Enter b: "))
        quotient = divide(a, b)
        print(quotient)

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Input a number between 1 to 5")