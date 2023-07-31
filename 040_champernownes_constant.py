#!/usr/bin/python3

from functools import reduce

def main(input_list):
    idx_list = sorted([i-1 for i in input_list])
    solution_list = []
    low_bound = 0
    high_bound = 9
    digits = 1
    for idx in idx_list:
        while True:
            if idx >= high_bound:
                low_bound = high_bound
                high_bound += 9*(10**digits)*(digits+1)
                digits += 1
            else:
                target_number = ((idx - low_bound) // digits) + 10**(digits-1)
                target_idx = (idx - low_bound) % digits
                solution_list.append(get_digit(target_number, digits, target_idx))
                break
    print(solution_list)
    print("The solution is:", reduce((lambda x,y: x*y), solution_list))
    return

def get_digit(n, size, idx):
    return (n // (10**(size-idx-1))) % 10

if __name__ == '__main__':
    input_list = [1, 10, 100, 1000, 10000, 100000, 1000000]
    main(input_list)
