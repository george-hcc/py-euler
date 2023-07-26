#!/usr/bin/python3

def main():
    print(larg_pali_prod(100, 999))

def larg_pali_prod(minor_n, major_n):
    largest_pali = 0
    for a in range(major_n, minor_n-1, -1):
        for b in range(a, minor_n-1, -1):
            prod = a*b
            if prod <= largest_pali:
                break
            if is_palindrome(prod):
                largest_pali = prod
    return largest_pali 

def is_palindrome(number):
    str_number = str(number)
    return str_number == str_number[::-1]
    
if __name__== '__main__':
    main()
