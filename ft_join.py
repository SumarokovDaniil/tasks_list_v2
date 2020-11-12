def ft_join(lst, sep=' '):
    result_string = str()
    
    for i in lst[:-1]:
        result_string += str(i) + sep
    result_string += str(lst[-1])
    
    return result_string
