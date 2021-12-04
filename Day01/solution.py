def day01():
    with open('./Day01/input.txt') as f:
        content = [int(i.strip()) for i in f.readlines()]

    conLen = len(content)
    increased = 0

    for i in range(1, conLen):
        increased += content[i] > content[i-1]

    print(f'The answer for the increased is: {increased}')

    increased = 0

    for i in range(3, conLen):
        increased += content[i] > content[i - 3]

    print(f'The answer for the triple is: {increased}')