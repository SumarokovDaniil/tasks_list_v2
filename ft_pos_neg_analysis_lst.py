def ft_pos_neg_analysis_lst(lst):
    count_positive = count_negative = count_zero = 0
    max_positive_number = max_negative_number = float('-inf')
    min_positive_number = min_negative_number = float('+inf')
    positive_summary = negative_summary = 0
    for i in lst:
        if i > 0:
            count_positive += 1
            positive_summary += i
            if i > max_positive_number:
                max_positive_number = i
            if i < min_positive_number:
                min_positive_number = i
        elif i < 0:
            count_negative += 1
            negative_summary += i
            if i > max_negative_number:
                max_negative_number = i
            if i < min_negative_number:
                min_negative_number = i
        else:
            count_zero += 1
    positive_avg = positive_summary / count_positive
    negative_avg = negative_summary / count_negative
    print('Положительные:', end='\t')
    print('Отрицательные:', end='\n')
    print(f'Количество чисел: {count_positive},', end='\t')
    print(f'Количество чисел: {count_negative},', end='\n')
    print(f'Максимальная цифра: {max_positive_number},', end='\t')
    print(f'Максимальная цифра: {max_negative_number},', end='\n')
    print(f'Минимальная цифра: {min_positive_number},', end='\t')
    print(f'Минимальная цифра: {min_negative_number},', end='\n')
    print(f'Сумма чисел: {positive_summary},', end='\t')
    print(f'Сумма чисел: {negative_summary},', end='\n')
    print(f'Среднее значение: {f"{positive_avg: .2f}"}', end='\t')
    print(f'Среднее значение: {f"{negative_avg: .2f}"}', end='\n')
    print()
    print(f'Количество нулей: {count_zero}')
