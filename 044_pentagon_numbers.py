#!/usr/bin/python3

def main(upper_limit):
    #return alt()
    pentagon_list = [n*(3*n-1)//2 for n in range(1, upper_limit)]
    pentagon_set = set(pentagon_list)
    
    solution = 0
    found = False
    for idx, pj in enumerate(pentagon_list):
        for pk in pentagon_list[idx+1:]:
            if (pk+pj in pentagon_set) and (pk-pj in pentagon_set):
                solution = pk-pj
                found = True
                break
        if found:
            break
    
    print("The solution is:", solution)
    return

if __name__ == '__main__':
    main(2500)
