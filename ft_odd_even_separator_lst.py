def ft_odd_even_separator_lst(lst):
    odd = list()
    even = list()
    for i in lst:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return [even, odd]
