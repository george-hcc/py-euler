#!/usr/bin/python3

def main():
    square = lambda x : x**2
    num_iter = range(1, 101)
    print(square(sum(num_iter)) - sum(map(square, num_iter)))

if __name__ == "__main__":
    main()
