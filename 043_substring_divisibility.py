#!/usr/bin/python3

from itertools import permutations

def main():
    solution_list = []
    for d1 in [1,2,3,4,5,6,7,8,9]:
        for d4 in [0, 2, 4, 6, 8]:
            if d1 == d4:
                continue
            for d6 in [0, 5]:
                if d6 == d1 or d6 == d4:
                    continue

                base = [d for d in [0,1,2,3,4,5,6,7,8,9] if d!=d1 and d!=d4 and d!=d6]
                for item in permutations(base):
                    if ((item[1]+d4+item[2]) % 3) != 0:
                        continue
                    if (100*item[2]+10*d6+item[3]) % 7 != 0:
                        continue
                    if (100*d6+10*item[3]+item[4]) % 11 != 0:
                        continue
                    if (100*item[3]+10*item[4]+item[5]) % 13 != 0:
                        continue
                    if (100*item[4]+10*item[5]+item[6]) % 17 != 0:
                        continue

                    solution_list.append(d1*(10**9) 
                            + item[0]*(10**8)
                            + item[1]*(10**7)
                            + d4*(10**6)
                            + item[2]*(10**5)
                            + d6*(10**4)
                            + item[3]*(10**3)
                            + item[4]*(10**2)
                            + item[5]*(10)
                            + item[6])

    return sum(solution_list)

if __name__ == '__main__':
    print("The solution is:", main())
