#!/usr/bin/python3

def main():
    solution_dict = {}
    for m in range(2, 22):
        for n in range(1, m):
            a = m**2 - n**2
            b = 2*m*n
            c = m**2 + n**2
            p = a+b+c

            k = 1
            kp = k*p
            while kp <= 1000:
                if kp in solution_dict:
                    solution_dict[kp].add(tuple(sorted([k*a, k*b, k*c])))
                else:
                    solution_dict[kp] = {tuple(sorted([k*a, k*b, k*c]))}
                k += 1
                kp += p
    
    max_len = 0
    max_key = 0
    for key in solution_dict:
        if len(solution_dict[key]) > max_len:
            max_len = len(solution_dict[key])
            max_key = key

    return max_key 

if __name__ == '__main__':
    print("The solution is:", main())
