#!/usr/bin/python3

def main(upper_limit):
    lof_divsets = [{0}, {0}]+[{1} for _ in range(2, upper_limit)]
    for i in range(2, upper_limit//2):
        for j in range(2*i, upper_limit, i):
            lof_divsets[j].add(i)

    lof_sums = [sum(item) for item in lof_divsets]

    sof_amicables = set()
    for n in range(2, upper_limit):
        possible_amicable = lof_sums[n]
        if possible_amicable >= upper_limit:
            continue
        if n == lof_sums[possible_amicable] and n != possible_amicable:
            sof_amicables.add(n)

    print("List of amicables: " + str(sof_amicables))
    print("Solution: " + str(sum(sof_amicables)))

if __name__ == '__main__':
    main(10000)
