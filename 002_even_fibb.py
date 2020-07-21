def main():
    flist = fibb_list_gen(4000000)
    is_even = lambda x : x % 2 == 0
    filtered_flist = list(filter(is_even, flist))
    print(flist)
    print(filtered_flist)
    print(sum(filtered_flist))

def fibb_list_gen(max_number):
    fibb_list = [0, 1]
    while fibb_list[-1] < max_number:
        fibb_list.append( fibb_list[-1] + fibb_list[-2] )
    return fibb_list[:-1]

if __name__== '__main__':
    main()
