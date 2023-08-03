#!/usr/bin/python3

def main():
    solution = 0
    for i in range(1, 1001):
        solution += len(convert_to_word(i).replace(' ', ''))
    print("The solution is:", solution)
    return

def convert_to_word(n):
    if n < 1:
        return ''
    base_0 = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
              'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen',
              'seventeen', 'eighteen', 'nineteen']
    base_10 = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    if n < 20:
        return base_0[n-1]
    if n < 100:
        if n % 10 == 0:
            return base_10[(n//10)-2]
        else:
            return base_10[(n//10)-2] + ' ' + base_0[(n%10)-1]
    if n < 1000:
        if n%100 == 0:
            return base_0[(n//100)-1] + ' hundred'
        else:
            return base_0[(n//100)-1] + ' hundred and ' + convert_to_word(n%100)
    if n == 1000:
        return 'one thousand'

if __name__ == '__main__':
    main()
