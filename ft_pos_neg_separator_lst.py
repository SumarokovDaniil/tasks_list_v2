def ft_pos_neg_separator_lst(lst):
    negative = list()
    positive = list()
    zero = list()
    for i in lst:
        if i > 0:
            positive.append(i)
        elif i < 0:
            negative.append(i)
        else:
            zero.append(i)
    return negative, zero, positive
