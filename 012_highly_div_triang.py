#!/usr/bin/python3

from tools.eratos_sieve import eratos_sieve

def main():
    lof_primes = eratos_sieve(100000)
    i = 1
    tnum = 1
    while True:
        i += 1
        tnum += i
        if count_factors(factorize(tnum, lof_primes)) > 500:
            break
    print(tnum, i)

def factorize(number, lof_primes):
    idx = 0
    fact_dict = {}
    while number != 1:
        fact_dict[lof_primes[idx]] = 0
        while number % lof_primes[idx] == 0:
            number = (number // lof_primes[idx])
            fact_dict[lof_primes[idx]] += 1
        idx += 1
    return fact_dict

def count_factors(fact_dict):
    nof_factors = 1
    for factor in fact_dict:
        if fact_dict[factor] != 0:
            nof_factors *= (fact_dict[factor] + 1)
    return nof_factors

if __name__ == '__main__':
    main()
