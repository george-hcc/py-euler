#!/usr/bin/python3

def main(max_n):
    dof_periodics = generate_periodics_dict(max_n)

    max_period = 0
    max_numbers = 0
    for k in dof_periodics:
        period = 1
        while (10**period) % k != 1:
            period += 1
        if period > max_period:
            max_period = period
            max_numbers = dof_periodics[k]

    print("The list of solutions with d<{} is: {}".format(max_n, max_numbers))
    print("The periodicity of the fraction is {}".format(max_period))
    return

#This function finds the integers n that has repeating decimals after 1/n 
#and generate a special dictionary that is going to be used to discover the periodicity of the each n
def generate_periodics_dict(max_n):
    dof_periodics = {}
    for n in range(2, max_n):
        k = n
        while k % 2 == 0:
            k = k // 2
        while k % 5 == 0:
            k = k // 5
        if k != 1:
            if k in dof_periodics:
                dof_periodics[k].append(n)
            else:
                dof_periodics[k] = [n]
    return dof_periodics


if __name__ == '__main__':
    main(1000)
