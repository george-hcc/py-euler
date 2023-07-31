#!/usr/bin/python3

triangle_set = {n*(n+1)//2 for n in range(1, 30)}

def main():
    solution_list = []
    with open("inputs/0042_words.txt", 'r') as f:
        input_list = f.read().rstrip().split(',')

        for word in input_list:
            word_value = sum((letter_value(letter) for letter in word))
            if word_value in triangle_set:
                solution_list.append(word)

    print(solution_list)
    print("The solution is:", len(solution_list))
    return

def letter_value(letter):
    if letter == '"':
        return 0
    return ord(letter)-64

if __name__ == '__main__':
    main()
