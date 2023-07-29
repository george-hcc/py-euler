#!/usr/bin/python3

from functools import reduce
import math

def main():
    solution_set = []
    accb_search(solution_set)
    num = reduce(lambda x, y: x*y, (item[0] for item in solution_set))
    den = reduce(lambda x, y: x*y, (item[1] for item in solution_set))
    gcd = math.gcd(num, den)
    print("The solution is {}/{}".format(num, den))
    print("Simplifying to the lowest common terms the result is {}/{}".format(num//gcd, den//gcd))
    return

def accb_search(solutions):
    for c in range(1, 10):
        for a in range(1, 10):
            for b in range(a+1, 10):
                num = 10*a+c
                den = 10*c+b
                if num == den:
                    continue
                elif num/den == a/b and num <= den:
                    solutions.append([num, den])
    return solutions

if __name__ == '__main__':
    main()
