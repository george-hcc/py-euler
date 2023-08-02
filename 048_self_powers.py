#!/usr/bin/python3

def main():
    mod_powers = [mod_pow(i, i, 10**10) for i in range(1, 1000+1)]
    print("The solution is:", sum(mod_powers)%(10**10))
    return

def mod_pow(b, e, mod=0):
    if mod == 0:
        return b**e
    ans = 1
    for i in range(e):
        ans = (ans * b) % mod
    return ans

if __name__ == '__main__':
    main()
