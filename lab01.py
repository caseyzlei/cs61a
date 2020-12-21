from operator import add, sub, mul

def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    factor = n - k + 1
    if k == 0:
        return 1
    else:
        while k > 1:
            factorial = mul(factor, n - k + 2)
            factor = factorial
            k = k - 1    
        
        return factor




def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    digit = 0
    while y > 0:
        digit = digit + y % 10
        y = y // 10
        
    return digit
        




def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    while n > 0:
        check = n % 10
        if check == 8:
            n = n // 10
            if n % 10 == 8:
                return True
        else:
            n = n // 10
    return False





