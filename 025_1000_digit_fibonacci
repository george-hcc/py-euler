#!/usr/bin/python3

def main(max_nof_digits):
    nof_digits = 1
    threshold = 10
    idx = 2
    a, b = 1, 1
    while nof_digits < max_nof_digits:
        a, b = b, (a+b)
        idx += 1
        if b > threshold:
            nof_digits += 1
            threshold *= 10

    print("The first fibonacci number with {} digits is {} and has index {}".format(max_nof_digits, b, idx))

    return

def next_fibo(a, b):
    return a+b

if __name__ == '__main__':
    main(1000)
