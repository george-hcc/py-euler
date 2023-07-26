#!/usr/bin/python3

def main(max_number):
    longest_seq = 0
    longest_num = 0
    count_dict = {}
    for n in range(max_number//2, max_number):
        seq_size = collatz_count(n, count_dict)
        if seq_size > longest_seq:
            longest_seq = seq_size
            longest_num = n
    return longest_seq, longest_num

def collatz_count(n, count_dict):
    if count_dict.get(n) is not None:
        return count_dict[n]
    if n == 1:
        return 1
    if n % 2 == 0:
        count_dict[n] = 1 + collatz_count(n//2, count_dict)
    else:
        count_dict[n] = 2 + collatz_count((3*n+1)//2, count_dict)
    return count_dict[n]

if __name__ == "__main__":
    print(main(1000000))
