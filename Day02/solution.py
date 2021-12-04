def day02():
    with open('./Day02/input.txt') as f:
        content = [i.strip() for i in f.readlines()]

    horizontal = 0
    depth = 0

    for x in content:
        split = x.split(' ')
        if(split[0] == "forward"):
            horizontal += int(split[1])
        elif(split[0] == "down"):
            depth += int(split[1])
        elif(split[0] == "up"):
            depth -= int(split[1])


    print(f'The answer for the distance is: {horizontal * depth}')

    horizontal = 0
    depth = 0
    aim = 0

    for x in content:
        split = x.split(' ')
        x = int(split[1])
        if(split[0] == "forward"):
            horizontal += x
            depth += aim * x
        elif(split[0] == "down"):
            aim += x
        elif(split[0] == "up"):
            aim -= x

    print(f'The answer for the distance is: {horizontal * depth}')