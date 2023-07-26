#!/usr/bin/python

from tools.eratos_sieve import eratos_sieve

def find_n_prime(n):
    lof_primes = eratos_sieve(150000)
    return lof_primes[n]


if __name__ == "__main__":
    print(find_n_prime(10000))
