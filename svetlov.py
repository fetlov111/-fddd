import math
while True:
    print(' \n Добро пожаловать в калькулятор')
    print('Вот несколько команд, которые я знаю: ')
    print('1. Сложить')
    print('2. Вычесть')
    print('3. Умножить')
    print('4. Разделить')
    print('5. Возвести в степень')
    print('6. Извлечь квадратный корень')
    print('7. Факториал числа')
    print('8. Косинус угла')
    print('9. Синус угла')
    print('10. Тангенс угла')
    print('0. Выход')
    try: 
        caseID = int(input('Введите команду '))
        if(caseID <11 and caseID > -1):
            if caseID in [6,7] : one = float (input('Введите число '))
            elif caseID in [8,9,10] : one = float(input('Введите угол в градусах '))
            elif caseID == 0 : break 
            else:
                one = float (input('\nВведите первое число '))
                two = float (input('Введите второе число ')) 
        else:
            print('Вы можете вводить команды только от 0 до 10')
            break
        match caseID:
            case 1 : result = one + two
            case 2 : result = one - two
            case 3 : result = one*two
            case 4 : result = one/two 
            case 5 : result = one**two
            case 6 : result = math.isqrt(one)
            case 7 : result = math.factorial(one)
            case 8 : result = math.sin(one)
            case 9 : result = math.cos(one)
            case 10 : result = math.tan(one)
        print('\n Результат: ', result)
    except ValueError: print('\nВы допустили ошибку, попробуйте снова')
    except ZeroDivisionError: print('\nНа ноль делить нельзя')


