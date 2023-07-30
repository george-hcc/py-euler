#!/usr/bin/python3

pow2_map = {n:2**n for n in range(20)}

def main(upper_limit):
    solution_set = set()
    for n in range(1, upper_limit):
        if is_palindrome(str(n)) and is_palindrome(convert_to_rev_b2(n)):
            solution_set.add(n)
    print(solution_set)
    print("The solution is:", sum(solution_set))
    return

def convert_to_rev_b2(n):
    rev_b2 = []
    while n > 0:
        rev_b2.append(n%2)
        n = n // 2
    return rev_b2

def is_palindrome(iterable):
    return iterable == iterable[::-1]

if __name__ == '__main__':
    main(10**6)
