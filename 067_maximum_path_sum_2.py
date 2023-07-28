#!/usr/bin/python3

from tools.maximum_path_sum import maximum_path_sum, print_triangle

def main():
    with open("./inputs/0067_triangle.txt", 'r') as f:
        str_arr = f.read().rstrip().split('\n')
        triangle_arr = [list(map(int, row.split())) for row in str_arr]
        solution_arr = maximum_path_sum(triangle_arr)
        # Print-it
        print_triangle(solution_arr)
        print("Solution: "+str(max(solution_arr[-1])))

if __name__ == '__main__':
    main()
