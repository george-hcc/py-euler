#!/usr/bin/python3

def main():
    with open("./inputs/0022_names.txt", 'r') as f:
        str_arr = f.read().rstrip().replace('"','').split(',')
        str_arr.sort()
        a_one = ord('A') - 1
        total_value = 0
        for pos, name in enumerate(str_arr):
            name_value = 0
            for letter in name:
                name_value += (ord(letter) - a_one)
            total_value += name_value * (pos+1)

        # Print-it
        print("Solution: "+str(total_value))

if __name__ == '__main__':
    main()
