def ft_rmstrspc(string):
    result_string = str()
    for i in string:
        if i != ' ':
            result_string += str(i)
    return result_string
