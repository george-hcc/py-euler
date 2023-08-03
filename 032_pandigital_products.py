#!/usr/bin/python3

from itertools import permutations
import math

comp_str = list('123456789')

def main():
    solution = set()
    a_0 = [i for i in range(2, 10)]
    b_0 = [int(''.join(item)) for item in permutations('123456789', 4)]
    solution |= find_pandigitals(a_0, b_0)
    a_1 = [int(''.join(item)) for item in permutations('123456789', 2)]
    b_1 = [int(''.join(item)) for item in permutations('123456789', 3)]
    solution |= find_pandigitals(a_1, b_1)
    return sum(solution)

def find_pandigitals(a_list, b_list):
    products = set()
    for a in a_list:
        limit = math.floor(10000 // a)
        for b in b_list:
            if b > limit:
                break
            c = a*b
            if sorted(str(a)+str(b)+str(c)) == comp_str:
                products.add(c)
    return products

if __name__ == '__main__':
    print("The solution is:", main())
