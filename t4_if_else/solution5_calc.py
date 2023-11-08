def calc(l:list):
    op = input('Введите тип операции - /, *, - либо + :')
    match op:
        case '/':
            if l[1]==0:
                return 'Попытка деления на ноль. '
            res = l[0]/l[1]
        case '*':
            res = l[0]*l[1]
        case '+':
            res = l[0]+l[1]
        case '-':
            res = l[0]-l[1]
        case _:
            return 'Операция была не опознана'
    return 'Результат операции: '+str(res)        
if __name__ == "__main__":
    try:
        num_list = list(map(int, input("Введите через пробел два целых числа: ").split()))
    except ValueError:
        print("некорректные данные. берём для теста 8 и 4")
        num_list = [8, 4]
    if not num_list:
        print("некорректные данные. берём для теста 8 и 4")
        num_list = [8, 4]
    # print(num_list)
    print(calc(num_list))
    #
    # *** Реализуйте программу калькулятор. На вход подается три значения: первое число, второе число и операция( *, /, + или -) . На выходе должны получить число, после выполнения операции.
