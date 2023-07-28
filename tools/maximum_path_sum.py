def maximum_path_sum(solution_arr):
    for j, row in enumerate(solution_arr[1:]):
        for i, item in enumerate(row):
            if i == 0:
                solution_arr[j+1][i] = item + solution_arr[j][i]
            elif i == j+1:
                solution_arr[j+1][i] = item + solution_arr[j][i-1]
            else:
                local_route_a = item + solution_arr[j][i]
                local_route_b = item + solution_arr[j][i-1]
                solution_arr[j+1][i] = max(local_route_a, local_route_b)
    return solution_arr

def print_triangle(triangle):
    for i, row in enumerate(triangle):
        print(i, row)
    return
