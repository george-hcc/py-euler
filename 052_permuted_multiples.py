#!/usr/bin/python3

from itertools import count

def main():
    return alt()
    for i in count(start=1):
        digits = sorted(str(i))
        if all((sorted(str(k*i))==digits for k in range(6, 1, -1) )):
            print(i, 2*i, 3*i, 4*i, 5*i, 6*i)
            break
    return

def alt():
    lower_bound = 1
    upper_bound = 2
    found = False
    while not found:
        lower_bound = 10*(lower_bound)
        upper_bound = 10*(upper_bound-1) + 7
        for i in range(lower_bound, upper_bound):
            digits = sorted(str(i))
            if all((sorted(str(k*i))==digits for k in range(6, 1, -1) )):
                found = True
                print(i, 2*i, 3*i, 4*i, 5*i, 6*i)
                break


if __name__ == '__main__':
    main()
