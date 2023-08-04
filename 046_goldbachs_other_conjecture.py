#!/usr/bin/python3

def main():
    upper_limit = 10**4
    dsquare_list = generate_dsquares(upper_limit)
    prime_set, oddcomp_list = custom_eratos(upper_limit)
    for oddcomp in oddcomp_list:
        found = True
        for dsquare in dsquare_list:
            diff = oddcomp - dsquare
            if diff < 2:
                break
            if diff in prime_set:
                found = False
                break

        if found:
            return oddcomp
    return

def generate_dsquares(upper_limit):
    dsquare_list = []
    i = 0
    dsquare = 2
    while dsquare <= upper_limit:
        dsquare_list.append(dsquare)
        i += 1
        dsquare += (4*i+2)
    return dsquare_list

# Sieve of Eratosthenes
def custom_eratos(max_prime):
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

    prime_set = set()
    oddcomp_list = []
    for n, boolean in enumerate(cddts_list[2:]):
        if boolean:
            prime_set.add(n+2)
        elif (n+2) % 2 == 1:
            oddcomp_list.append(n+2)

    return prime_set, oddcomp_list

if __name__ == '__main__':
    print("The solution is:", main())
