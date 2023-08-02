#!/usr/bin/python3

def main():
    limit = 10**6
    ans = 0
    num = 1
    for n in range(2, 101):
        num *= n
        den = num
        for r in range(1, n//2+1):
            den = (den * r) // (n-r+1)
            binomial = num//den
            if binomial >= limit:
                if n % 2 != 0:
                    ans += 2
                else:
                    ans += 1 if r == (n//2) else 2

    print("The solution is:", ans)
    return

if __name__ == '__main__':
    main()
