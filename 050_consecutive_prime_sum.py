#!/usr/bin/python3

from tools.eratos_sieve import eratos_sieve

def main():
    n = 6
    prime_list = eratos_sieve(10**n)
    prime_set = set(prime_list)

    starting_slice = 0
    slice_sum = 0
    for i, prime in enumerate(prime_list):
        slice_sum += prime
        if slice_sum >= 10**n:
            starting_slice = i
            break

    for slice_len in range(starting_slice, 0, -1):
        idx = 0
        slice_sum = sum(prime_list[:slice_len])
        while slice_sum < 10**n:
            if slice_sum in prime_set:
                return slice_sum
            slice_sum += prime_list[idx+slice_len] - prime_list[idx]
            idx += 1
    return

if __name__ == '__main__':
    print("The solution is:", main())
