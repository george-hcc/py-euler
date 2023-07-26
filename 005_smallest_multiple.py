#!/usr/bin/python3

from tools.eratos_sieve import eratos_sieve

class factor_dict():

    def factorize(number):
        lof_primes = eratos_sieve(number)
        dict_factors = { prime:0 for prime in lof_primes }
        for prime in lof_primes:
            while number % prime == 0:
                dict_factors[prime] += 1
                number = number // prime
        return dict_factors

    def mmc(fdict_a, fdict_b):
        if len(fdict_b) > len(fdict_a):
            biggst = fdict_b
            smalst = fdict_a
        else:
            biggst = fdict_a
            smalst = fdict_b
        for key in smalst:
            if smalst[key] > biggst[key]:
                biggst[key] = smalst[key]
        return biggst

    def mount_number(fdict):
        prod = 1
        for key in fdict:
            prod *= (key ** fdict[key])
        return prod            

def main():
    multiple = {}
    for number in range(21):
        multiple = factor_dict.mmc(multiple, factor_dict.factorize(number))
    print(factor_dict.mount_number(multiple), multiple)
    
if __name__== '__main__':
    main()
