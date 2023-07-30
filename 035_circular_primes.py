#!/usr/bin/python3

def main(upper_limit):
    solutions_set = set()
    # Generate dictionary of primes
    prime_dict = custom_eratos(upper_limit)

    for prime in prime_dict:
        # Is already checked?
        if prime_dict[prime]:
            continue

        # Generating circulars
        circulars = generate_circulars(prime, num_len(prime))

        # Checking for irregular circulars
        if circulars == None:
            continue
            
        # Counting the number of primes inside circulars
        number_of_primes = 0
        for circular in circulars:
            if circular in prime_dict:
                prime_dict[circular] = True
                number_of_primes += 1

        # Checking if a circular prime family was found
        if number_of_primes == len(circulars):
            solutions_set.update(circulars)
            print("Prime family:", sorted(list(circulars)))

    print("The solution is:", len(solutions_set))
    return

def generate_circulars(n, size_of_n):
    str_n = str(n)
    circulars = {str_n}
    for i in range(size_of_n-1):
        if int(str_n[1]) % 2 == 0:
           return None
        str_n = str_n[1:]+str_n[0] 
        circulars.add(str_n)
    return set(int(string) for string in circulars)

def num_len(n):
    digits = 0
    while n > 0:
        digits += 1
        n = n // 10
    return digits        

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

    return {n:False for n, boolean in enumerate(cddts_list) if boolean}


if __name__ == '__main__':
    main(10**6)
