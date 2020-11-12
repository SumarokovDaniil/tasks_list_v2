def ft_sum_even_part_lst(lst):
    summary = 0
    for i in lst:
        if i % 2 == 0:
            summary += i
    return summary
