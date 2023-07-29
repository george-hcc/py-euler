#!/usr/bin/python3

factorial = lambda n: 1 if n<2 else n*factorial(n-1)
fact_map = {num: factorial(num) for num in range(10)}

def main(upper_limit):
    solution_list = []
    for n in range(3, upper_limit):
        if digit_factorials_sum(n) == n:
            solution_list.append(n)
    print(solution_list)
    print("The solution is {}".format(sum(solution_list)))
    return

def digit_factorials_sum(n):
    total_sum = 0  
    while n > 0:
        total_sum += fact_map[n % 10]
        n = n // 10
    return total_sum

if __name__ == '__main__':
    main(10**5)
