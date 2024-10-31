while True:
    print('1. Addition')
    print('2. Subtraction')
    print('3. Multiplication')
    print('4. Division')

    choice = input("Enter your choice: ")

    if choice == 'y':
        break

    num1 = float(input('Enter Number 1: '))
    num2 = float(input('Enter Number 2: '))

    if choice == '1':
        print(f"{num1} + {num2} = {num1 + num2}")
    elif choice == '2':
        print(f"{num1} - {num2} = {num1 - num2}")
    elif choice == '3':
        print(f"{num1} * {num2} = {num1 * num2}")
    elif choice == '4':
        if num2 == 0.0:
            print("Error: Division by zero")
        else:
            print(f"{num1} / {num2} = {num1 / num2}")
    else:
        print('Invalid choice')

    restart = input("Would you like to perform another calculation? (yes/no): ")
    if restart.lower() != 'yes':
        break

