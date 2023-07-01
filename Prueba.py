import math
import os
import random
import re
import sys



def superDigit(n, k):
    sumNum =0
    for i in n:
      sumNum += i
    return sumNum  

print(superDigit)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')


    fptr.close()

