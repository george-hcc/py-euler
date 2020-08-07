from tools.eratos_sieve import eratos_sieve

def main():
    lof_primes = eratos_sieve(2000000)
    print(sum(lof_primes))

if __name__ == "__main__":
    main()
