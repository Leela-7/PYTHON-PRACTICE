while True:
    try:
        n1 = int(input("Enter first integer value: "))
        n2 = int(input("Enter second integer value: "))
        n3 = n1 / n2
        print(f'Division of {n1}/{n2} = {n3}')
        break
    except (ValueError, ZeroDivisionError):
        print('''Input only integers or number
cannot divide with zero''')
