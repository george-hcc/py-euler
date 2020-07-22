def main():
    prime_list = eratos_sieve(1000000)
    for prime in prime_list:
        print(prime)

# Sieve of Eratosthenes
def eratos_sieve(max_prime):
    # Candidates list
    cddts_list = [[integer, True] for integer in range(2, max_prime+1)]
    prime_list = []

    # Sieve Logic
    for i, test_item in enumerate(cddts_list):
        if test_item[1] == True:
            prime_list.append(test_item[0])
            j = test_item[0]
            while i + j < len(cddts_list):
                cddts_list[i + j][1] = False
                j += test_item[0]
            
    
    return prime_list

if __name__== '__main__':
    main()
