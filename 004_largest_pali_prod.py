#!/usr/bin/python3

from tools.eratos_sieve import eratos_sieve
import math

def main():
    print(larg_pali_prod(100, 999))

def larg_pali_prod(minor_n, major_n):
    pali_prod = 0
    for a in range(minor_n, major_n+1):
        for b in range(a, major_n+1):
            prod = a*b
            if is_palindrome(prod) and prod > pali_prod:
                pali_prod = prod
    return pali_prod

def is_palindrome(number):
    lst_number = list(str(number))
    pivot = len(lst_number) // 2
    return lst_number[0:pivot] == lst_number[-1:-(pivot+1):-1]
    
if __name__== '__main__':
    main()
