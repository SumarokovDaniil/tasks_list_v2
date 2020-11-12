def ft_len(string):
    count = 0
    for _ in string:
        count += 1
    return count


def ft_join(lst, separator=' '):
    res = ''
    for i in range(ft_len(lst)):
        if i == ft_len(lst) - 1:
            res += lst[i]
        else:
            res += lst[i] + separator
    return res
