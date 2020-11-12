def ft_odd_even_analysis_lst(lst):
    count_even = count_odd = 0
    max_even_number = max_odd_number = float('-inf')
    min_even_number = min_odd_number = float('+inf')
    summary_even = summary_odd = 0
    for i in lst:
        if i % 2 == 0:
            count_even += 1
            summary_even += i
            if i > max_even_number:
                max_even_number = i
            if i < min_even_number:
                min_even_number = i
        else:
            count_odd += 1
            summary_odd += i
            if i > max_odd_number:
                max_odd_number = i
            if i < min_odd_number:
                min_odd_number = i
    print('Анализ списка:')
    print(f'Количество четных чисел: {count_even},\t\t', end='')
    print(f'Количество нечетных чисел: {count_odd}', end='\n')
    print(f'Максимальная четная цифра: {max_even_number},\t', end='\t')
    print(f'Максимальная нечетная цифра: {max_odd_number},', end='\n')
    print(f'Минимальная четная цифра: {min_even_number},\t', end='\t')
    print(f'Минимальная нечетная цифра: {min_odd_number},', end='\n')
    print(f'Сумма четных чисел: {summary_even},\t', end='\t')
    print(f'Сумма нечетных чисел: {summary_odd},', end='\n')
