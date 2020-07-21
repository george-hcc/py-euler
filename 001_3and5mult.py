def main():
    ans_list = multiple_finder(1000, 5, 3)
    print(ans_list)
    print(sum(ans_list))


def multiple_finder(max_number, *factors):
    int_list = range(min(factors), max_number)
    multiple_list = []
    for integer in int_list:
        for factor in factors:
            if integer % factor == 0:
                multiple_list.append(integer)
                break
    return multiple_list

if __name__== '__main__':
    main()
