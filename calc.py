print('Здравствуйте! Я программа калькулятор')
operants_list = ['+', '-', ':', '*', '%', 'q']
while True:
    op = input('Введите желаемую операцию(+,-,:,*,%) или "q" для выхода: ')
    if not(op in operants_list):
        print ('Такой операции не знаю')
        continue
    else:
        if op == 'q':
            break
        a = float(input('введите первое число или число, от которого надо вычислить проценты: '))
        b = float(input('введите второе число или количество процентов: '))
        if op == '+':
            print('Сумма: ', a + b)
        elif op == '-':
            print('Разность: ', a - b)
        elif op == ':':
            print('Частное: ', a / b)
        elif op == '*':
            print('Произведение: ', a * b)
        elif op == '%':
            print('Ответ: ', a / 100 * b)