def is_number(n):
    """
        :Synopsis: Judge if an input is a number
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
