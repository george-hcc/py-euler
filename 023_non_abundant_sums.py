#!/usr/bin/python3

import sympy

def main(upper_limit):
    # Building list of proper divisors and sum of divisor up to the upper limit
    lof_divsets = [{0}, {0}]+[{1} for _ in range(2, upper_limit)]
    for i in range(2, upper_limit//2):
        for j in range(2*i, upper_limit, i):
            lof_divsets[j].add(i)

    # Creating list of abundant numbers
    lof_abundants = [idx for idx in range(upper_limit) if sum(lof_divsets[idx]) > idx]

    # Filtering which numbers are sums of pairs of abundants
    lof_2abun_sum_bool = [False for _ in range(upper_limit)]
    for num_a in lof_abundants:
        for num_b in lof_abundants:
            sum_ab = num_a + num_b
            if sum_ab < upper_limit:
                lof_2abun_sum_bool[sum_ab] = True

    # Calculating the sum of all filtered numbers
    print("Solution: " + str(sum(i for i in range(upper_limit) if not lof_2abun_sum_bool[i])))


if __name__ == '__main__':
    main(20162)
