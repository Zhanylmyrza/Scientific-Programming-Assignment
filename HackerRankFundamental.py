import math
import os
import random
import re
import sys

def maximumDraws(n):
    return n+1 if n > 0 else 0

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = maximumDraws(n)

        fptr.write(str(result) + '\n')

    fptr.close()
