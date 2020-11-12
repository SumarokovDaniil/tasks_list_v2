def ft_len(lst):
    count = 0
    for _ in lst:
        count += 1
    return count


def ft_sum_even_lst(lst):
    summary = 0
    for i in range(ft_len(lst)):
        if i % 2 == 0:
            summary += lst[i]
    return summary
