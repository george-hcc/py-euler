#!/usr/bin/python3

from tools.eratos_sieve import eratos_sieve
import math

def main():
    tbf_number = 600851475143
    lof_primes = eratos_sieve(math.ceil(tbf_number ** 0.5))
    factor_list = trial_method(tbf_number, lof_primes)
    print(factor_list)

def trial_method(tbf_number, lof_primes):
    factor_list = []
    end_loop_bool = False
    for prime in lof_primes:
        while tbf_number % prime == 0:
            factor_list.append(prime)
            tbf_number = tbf_number // prime
    return factor_list

if __name__== '__main__':
    main()
