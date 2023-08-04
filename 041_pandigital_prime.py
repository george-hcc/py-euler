#!/usr/bin/python3

from tools.eratos_sieve import eratos_sieve
from itertools import permutations
import math

def main():
    solution_list = []
    prime_list = eratos_sieve(math.floor(math.sqrt(10**7)))
    for i in [4, 7]:
        pandig_list = [int(''.join(item)) for item in list(permutations([str(i) for i in range(1,i+1)], i))]
        for pandig in pandig_list:
            limit = math.floor(math.sqrt(pandig))
            pandig_is_prime = True
            for prime in prime_list:
                if prime > limit:
                    break
                if pandig % prime == 0:
                    pandig_is_prime = False
                    break
            if pandig_is_prime:
                solution_list.append(pandig)

    return solution_list[-1]


if __name__ == '__main__':
    print("The solution is:", main())
