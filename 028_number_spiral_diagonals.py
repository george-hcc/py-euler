#!/usr/bin/python3

def main(mtx_size):
    diag_sum = 1
    last_int = 1
    ring_size = 3
    while ring_size <= mtx_size:
        diag_sum += 4*last_int+10*(ring_size-1)
        last_int += 4*(ring_size-1)
        ring_size += 2

    print("The solution is {}".format(diag_sum))
    return

if __name__ == '__main__':
    main(1001)
