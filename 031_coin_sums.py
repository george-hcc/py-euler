#!/usr/bin/python3

coin_list = [1, 2, 5, 10, 20, 50, 100, 200]
dyn_table = {}

def main():
    return coin_sum(200, 7)

def coin_sum(n, max_idx):
    if n < 2:
        return 1
    if max_idx == 0:
        return 1

    fixed_idx = max_idx
    while n < coin_list[fixed_idx]:
        fixed_idx -= 1

    aux = 10*n + fixed_idx
    
    if aux in dyn_table:
        return dyn_table[aux]
    else:
        ans = 0
        for i in range(fixed_idx+1):
            ans += coin_sum(n-coin_list[i], i)
        dyn_table[aux] = ans
        return ans

if __name__ == '__main__':
    print("The solution is:", main())
