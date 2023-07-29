#!/usr/bin/python3

def main(upper_limit):
    distinct_terms = set()
    for a in range(2, upper_limit+1):
        for b in range(2, upper_limit+1):
            distinct_terms.add(a**b)
    print(len(distinct_terms))
    return

if __name__ == '__main__':
    main(100)
