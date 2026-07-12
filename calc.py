def calc():
    while 1:
        try:
            num1 = int(input("Введите первое число: "))
            num2 = int(input("Введите второе число: "))
        except:
            print("Нужно ввести число!")
        else:
            char1 = input("Выберите опирацию:\n+ сложение\n- вычетание\n* умножение\n/ деление\nОперация: ").strip()
            if char1 == '+':
                return print(f"{num1 + num2}")
            elif char1 == '-':
                return print(f"{num1 - num2}")
            elif char1 == '*':
                return print(f"{num1 * num2}")
            elif char1 == '/':
                return print(f"{num1 / num2}")
            else:
                print("Пользуетесь встроенными операторами!")