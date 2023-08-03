#!/usr/bin/python3

def main(starting_year, starting_day, ending_year):
    leap_months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    nonleap_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    solution = 0
    week_day = starting_day
    for year in range(starting_year, ending_year+1):
        leap = is_leap_year(year)
        for i in range(12):
            if leap:
                week_day = (week_day+leap_months[i]) % 7
            else:
                week_day = (week_day+nonleap_months[i]) % 7
            
            if week_day == 0:
                solution += 1

    return solution

def is_leap_year(n):
    if n % 4 != 0:
        return False
    if n % 100 == 0:
        if n % 400 == 0:
            return True
        else:
            return False
    return True

if __name__ == '__main__':
    starting_year = 1901
    starting_day = 2
    ending_year = 2000
    solution = main(starting_year, starting_day, ending_year)
    print("The solution is:", solution)
