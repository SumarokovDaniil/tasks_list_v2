def ft_join(lst, sep=''):
    string = str()
    for i in lst:
        string += str(i) + sep
    return string[:-1]
