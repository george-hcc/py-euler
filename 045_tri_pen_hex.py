#!/usr/bin/python3

import math

def main():
    found = False
    n = 286
    while not found:
        tri = n*(n+1)//2
        if is_pen(tri) and is_hex(tri):
            found = True
            print("The solution is", tri,"with n equal to", n)
        else:
            n += 1
    return

def is_pen(n):
    return ((math.sqrt(24*n+1)+1)/6).is_integer()

def is_hex(n):
    return ((math.sqrt(8*n+1)+1)/4).is_integer()

if __name__ == '__main__':
    main()
