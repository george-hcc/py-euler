#!/usr/bin/python3

def main():
    for b in range(500):
        a = 500*(1000-2*b)/(1000-b)
        if a.is_integer():
            c = (a**2 + b**2) ** 0.5
            print(int(a), b, int(c), int(a*b*c))

if __name__ == "__main__":
    main()
