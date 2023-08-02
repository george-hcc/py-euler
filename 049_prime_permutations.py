#!/usr/bin/python3

def main():
    lower_bound = 10**3
    upper_bound = 10**4
    prime_list = custom_eratos(lower_bound, upper_bound)
    prime_set = set(prime_list)

    for i in range(len(prime_list)):
        for j in range(i+1, len(prime_list)):
            diff = prime_list[j] - prime_list[i]
            if (prime_list[j]+diff) in prime_set:
                if are_3_perms(prime_list[i], prime_list[j], prime_list[j]+diff):
                    print(prime_list[i], prime_list[j], prime_list[j]+diff, diff)

    return

def custom_eratos(lower_bound, upper_bound):
    # Candidates list
    cddts_list = [True for integer in range(upper_bound)]
    cddts_list[0] = cddts_list[1] = False

    # Sieve Logic
    p = 2
    while (p*p < upper_bound):
        if cddts_list[p] == True:
            for i in range(p*p, upper_bound, p):
                cddts_list[i] = False
        p += 1

    return [n for n, boolean in enumerate(cddts_list) if (boolean and n > lower_bound)]

def are_3_perms(a, b, c):
    a_str = sorted(str(a))
    b_str = sorted(str(b))
    c_str = sorted(str(c))
    return a_str == b_str and a_str == c_str

if __name__ == '__main__':
    main()
