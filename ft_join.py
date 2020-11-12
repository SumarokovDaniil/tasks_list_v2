def ft_join(lst, sep=''):
    string = ''
    for i in lst:
        string += str(i) + sep
    return string[:-1]
