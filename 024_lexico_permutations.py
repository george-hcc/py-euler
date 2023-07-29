#!/usr/bin/python3

from itertools import permutations, islice

def main(digit_str, position):
    perm_iter = permutations(digit_str)
    pos_perm = next(islice(perm_iter, position-1, position))
    print("Solution: " + ''.join(pos_perm))
    return

if __name__ == '__main__':
    main('0123456789', 1000000)
