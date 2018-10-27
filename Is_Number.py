def is_number(n):
    """
        :param n: Input data
        :returns: True if the input is a number instinctively
                   and False otherwise
    """
    flag = True
    try:
        num = float(n)
        flag = num == num
    except ValueError:
        flag = False
    return flag
