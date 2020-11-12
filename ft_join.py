def ft_len(string):
    count = 0
    for _ in string:
        count += 1
    return count


def ft_join(lst, sep=''):
    string = str()
    if sep == '':
        for i in lst:
            string += str(i) + sep
        return string
    for i in lst:
        string += str(i) + sep
    return string[:-ft_len(sep)]
