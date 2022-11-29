import math
import os
import random
import re
import sys




def solve(r1, r2, p1, a1, p2, a2):
    a = ((a1[0]-a2[0])**2 + (a1[1]-a2[1])**2 + (a1[2]-a2[2])**2)/4;
    b = ((p1[0]-p2[0])*(a1[0]-a2[0])) + ((p1[1]-p2[1])*(a1[1]-a2[1])) + ((p1[2]-p2[2])*(a1[2]-a2[2]))

    c = (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 + (p1[2]-p2[2])**2

    d = (r1+r2)**2;

    if(c < d):
        return "YES"

    disc = b**2 - 4*a*c
    if(disc < 0):
        return "NO"

    root1 = (-b+disc)/(2*a)
    root2 = (-b-disc)/(2*a)
    
    if(root1<0 and root2<0):
        return "NO"
    
    return "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        r1R2 = input().split()

        r1 = int(r1R2[0])

        r2 = int(r1R2[1])

        position = list(map(int, input().rstrip().split()))

        acceleration = list(map(int, input().rstrip().split()))

        position2 = list(map(int, input().rstrip().split()))

        acceleration2 = list(map(int, input().rstrip().split()))

        result = solve(r1, r2, position, acceleration, position2, acceleration2)

        fptr.write(result + '\n')

    fptr.close()

