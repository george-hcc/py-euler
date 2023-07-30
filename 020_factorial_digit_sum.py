#!/usr/bin/python3

factorial = lambda x: 1 if x<2 else x*factorial(x-1)

def main():
    print("The solution is", sum(map(int, str(factorial(100) ) ) ) )

if __name__ == '__main__':
    main()
