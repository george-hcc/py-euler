#!/usr/bin/python3

def main():
    prime_list = eratos_sieve(1000000)
    for prime in prime_list:
        print(prime)

# Sieve of Eratosthenes
def eratos_sieve(max_prime):
    # Candidates list
    cddts_list = [True for integer in range(max_prime+1)]
    cddts_list[0] = cddts_list[1] = False

    # Sieve Logic
    p = 2
    while (p*p <= max_prime):
        if cddts_list[p] == True:
            for i in range(p*p, max_prime+1, p):
                cddts_list[i] = False
        p += 1
    
    return [n for n, boolean in enumerate(cddts_list) if boolean]

if __name__== '__main__':
    main()
