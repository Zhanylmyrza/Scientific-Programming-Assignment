import math
import os
import random
import re
import sys


def solve(n):
    return 'Go On Bob '+str(int(((1 + 8*n)**0.5 - 1)/2)) if ((1 + 8*n)**0.5 - 1)/2 == ((1 + 8*n)**0.5 - 1)//2 else "Better Luck Next Time"

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = solve(n)

        fptr.write(result + '\n')

    fptr.close()
