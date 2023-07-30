#!/usr/bin/python3

from tools.eratos_sieve import eratos_sieve_set
import math

def main():
    solution_list = []
    
    r_trunc_primes = generate_rtrunc_primes()
    for prime in r_trunc_primes:
        l_truncables = generate_l_truncables(prime)
        if all(is_prime(item) for item in l_truncables):
            solution_list.append(prime)

    print(solution_list)
    print("The solution is:", sum(solution_list))
    return


def check_ltrun_primes(prime_set):
    return

def generate_l_truncables(n):
    truncables = {n}
    str_n = str(n)
    for i in range(1, len(str_n)):
        truncables.add(int(str_n[i:]))
    return truncables

def generate_r_truncables(n):
    truncables = set()
    while n > 0:
        truncables.add(n)
        n = n // 10
    return truncables

def generate_rtrunc_primes(total_d = 8):
    total_rtrunc_primes = []
    prev_rtrunc_primes = [2, 3, 5, 7]
    possible_new = [1, 3, 7, 9]
    for d in range(2, total_d+1):
        new_rtrunc_primes = []
        for leftmost in prev_rtrunc_primes:
            for digit in possible_new:
                n = 10*leftmost + digit
                if is_prime(n):
                    new_rtrunc_primes.append(n)
                else:
                    continue

        prev_rtrunc_primes = new_rtrunc_primes
        total_rtrunc_primes.extend(new_rtrunc_primes)
    return total_rtrunc_primes


def is_prime(n):
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False

    r = math.floor(math.sqrt(n))
    f = 5
    while f <= r:
        if n % f == 0:
            return False
        if n % (f+2) == 0:
            return False
        f += 6

    return True


if __name__ == '__main__':
    main()
    #print(generate_rtrunc_primes())
    #main(10**3)
    #print(generate_l_truncables(33933))
    #print(generate_r_truncables(33933))
