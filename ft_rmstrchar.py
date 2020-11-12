def ft_rmstrchar(string, less):
    new_string = str()
    for i in string:
        if i not in less:
            new_string += i
    return new_string
