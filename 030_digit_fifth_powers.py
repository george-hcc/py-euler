#!/usr/bin/python3

fifth_map = {num: num**5 for num in range(10)}

def main():
    solution_list = []
    for n in range(2, 200000):
        if int_to_sum(n) == n:
            solution_list.append(n)
    print(solution_list)
    print("The solution is {}".format(sum(solution_list)))
    return

def int_to_sum(n):
    digit_fifth_sum = 0  
    while n > 0:
        digit_fifth_sum += fifth_map[n % 10]
        n = n // 10
    return digit_fifth_sum

if __name__ == '__main__':
    main()
