# Python3

# Time complexity is O(1).
import math
import decimal as decimal

T = int(input())
i = 0

while i < T:

    # Read numbers n and m
    n,m = input().strip().split(" ")
    n = int(n)
    m = int(m)

    if (n % m == 0):
        print(n)
    else:
        _mod = n / m;
        # This didn't work properly under python 3
        # r_mod = roand(float(abs(_mod)))
        # BECAUSE OF PYTHON 3. !!!
        # https://docs.python.org/3/whatsnew/3.0.html
        r_mod = decimal.Decimal(_mod).quantize(decimal.Decimal('1'), rounding=decimal.ROUND_HALF_UP)

        # print('MOD:' +  str(_mod) + ' Rmod: ' + str(r_mod))
        res = m * r_mod
        print(res)

    i = i+1
# End of While

# Code by Michal Slovik
