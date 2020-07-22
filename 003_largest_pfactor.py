def main():
    print(eratos_sieve(100000))

# Sieve of Eratosthenes
def eratos_sieve(max_prime):
    # Candidates list
    cddts_list = [[integer, True] for integer in range(2, max_prime+1)]
    prime_list = []

    # Sieve Logic
    for i, test_item in enumerate(cddts_list):
        if test_item[1] == True:
            nof_divisors = 0
            for prime in prime_list:
                if test_item[0] % prime == 0:
                    nof_divisors += 1
            if nof_divisors > 0:
                j = 0
                while i + j < len(cddts_list):
                    cddts_list[i + j][1] = False
                    j += test_item[0]
            else:
                prime_list.append(test_item[0])
    
    return prime_list

if __name__== '__main__':
    main()
