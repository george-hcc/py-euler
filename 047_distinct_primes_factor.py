#!/usr/bin/python3

def main(comp_factor, limit):
    factor_list = [0]*(limit)
    count = 0
    for n in range(2, limit):
        if factor_list[n] == 0:
            count = 0
            for i in range(2*n, limit, n):
                factor_list[i] += 1
        elif factor_list[n] == comp_factor:
            count += 1
            if count == comp_factor:
                print("The solution is:", n-comp_factor+1)
                break
        else:
            count = 0
    return

if __name__ == '__main__':
    main(4, 10**6)
